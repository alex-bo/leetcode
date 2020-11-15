import argparse
import csv
import logging
import sys
from collections import namedtuple
from typing import Optional, List


class LoggingMixin:

    @property
    def logger(self) -> logging.Logger:
        return logging.getLogger(type(self).__name__)


class Error(Exception):
    pass


class ArgumentError(Error):
    pass


class BaseModel(LoggingMixin):

    def __init__(self):
        pass


Loan = namedtuple('Loan', ['id', 'amount', 'interest_rate', 'default_likelihood', 'state'])
LoanApplication = namedtuple('LoanApplication',
                             ['loan', 'facility', 'expected_yield', 'facility_state_version', 'bank_state_version'])
LoanAssignment = namedtuple('LoanAssignment', ['loan_id', 'facility_id'])


class Covenant(BaseModel):

    def __init__(self, bank_id: int, facility_id: Optional[int]):
        super(Covenant, self).__init__()
        self.bank_id = bank_id
        self.facility_id = facility_id

    def can_apply(self, loan: Loan) -> bool:
        raise Error('Attempt to invoke abstract method.')

    def __str__(self):
        return '{}(bank_id={}, facility_id={})'.format(type(self).__name__, self.bank_id, self.facility_id)


class MaxDefaultRateCovenant(Covenant):

    def __init__(self, bank_id: int, facility_id: Optional[int], max_default_likelihood: float):
        super(MaxDefaultRateCovenant, self).__init__(bank_id, facility_id)
        self.max_default_likelihood = max_default_likelihood

    def can_apply(self, loan: Loan) -> bool:
        return loan.default_likelihood <= self.max_default_likelihood


class GeoLocationCovenant(Covenant):

    def __init__(self, bank_id: int, facility_id: Optional[int], banned_state: str):
        super(GeoLocationCovenant, self).__init__(bank_id, facility_id)
        self.banned_state = banned_state

    def can_apply(self, loan: Loan) -> bool:
        return loan.state != self.banned_state


class Facility(BaseModel):

    def __init__(self, bank_id: int, facility_id: int, interest_rate: float, amount: int):
        """
        Instance of bank facility that contains covenants that apply to this facility.

        Note: `__state_version` reflects internal state of the Facility. It helps to track cases like this:
        1. Loan application issued (get_loan_application method).
        2. New covenant is added or another loan applied (that changes available funds).
        3. User applies for the loan issued on step #1.
        Loan application may become non-optimal or even not valid anymore.

        :param bank_id:
        :param bank_name: Name of the Bank
        :param bank_id: Bank ID
        :param facility_id: Facility ID
        :param interest_rate: Interest rate of this Facility
        :param amount: Available funds.
        """
        super(Facility, self).__init__()
        self.bank_id = bank_id
        self.facility_id = facility_id
        self.interest_rate = interest_rate
        self.amount = amount
        self.covenants = []
        self.accepted_loans = []
        self.__state_version = 0
        self.expected_yield = 0.0

    def add_covenant(self, covenant: Covenant):
        if covenant.facility_id != self.facility_id:
            raise ArgumentError(
                'Cannot add covenant with facility_id={} to facility with id={}'.format(
                    covenant.facility_id, self.facility_id
                )
            )
        if covenant.bank_id != self.bank_id:
            raise ArgumentError(
                'Cannot add covenant with bank_id={} to facility with bank_id={}'.format(
                    covenant.bank_id, self.bank_id
                )
            )
        self.covenants.append(covenant)
        self.__state_version += 1
        self.logger.info('%s added to %s.', covenant, self)

    def get_loan_application(self, loan: Loan) -> Optional[LoanApplication]:
        if loan.amount > self.amount:
            self.logger.debug('%s rejected by %s because of insufficient amount.', loan, self)
            return None
        for covenant in self.covenants:
            if not covenant.can_apply(loan):
                self.logger.debug('%s rejected by %s because of %s.', loan, self, covenant)
                return None
        loan_appl = LoanApplication(loan, self, self.calculate_expected_yield(loan), self.__state_version, None)
        if loan_appl.expected_yield <= 0:
            self.logger.debug('%s has non-positive yield, ignore.', loan_appl)
            return None
        self.logger.debug('%s issued by %s.', loan_appl, self)
        return loan_appl

    def apply_loan(self, application: LoanApplication) -> Optional[LoanAssignment]:
        if application.facility != self:
            raise ArgumentError('Cannot settle application from a different facility.')
        if application.facility_state_version != self.__state_version:
            self.logger.info('%s rejected by %s because facility internal state version has changed.',
                             application, self
                             )
            return None
        if application.loan.amount > self.amount:
            self.logger.warning('Unexpected attempt to apply %s with less amount than %s has. '
                                'Should have been rejected on application stage.',
                                application, self)
            return None
        loan_assign = LoanAssignment(application.loan.id, self.facility_id)
        self.amount -= application.loan.amount
        self.expected_yield += application.expected_yield
        self.__state_version += 1
        self.logger.info('%s issued by %s.', loan_assign, self)
        return loan_assign

    def calculate_expected_yield(self, loan: Loan) -> float:
        return (
            (1 - loan.default_likelihood) * loan.interest_rate * loan.amount
            - loan.default_likelihood * loan.amount
            - self.interest_rate * loan.amount
        )

    def __str__(self):
        return '{}(facility_id={}, amount={}, __state_version={})'.format(
            type(self).__name__, self.facility_id, self.amount, self.__state_version
        )


class Bank(BaseModel):

    def __init__(self, bank_id: int, bank_name: str):
        """
        Instance of a bank that contains facilities and covenants that apply to this bank.

        Note: `__state_version` reflects internal state of the Bank. It helps to track cases like this:
        1. Loan application issued (get_loan_application method).
        2. New facility or covenant is added.
        3. User applies for the loan issued on step #1.
        Loan application may become non-optimal or even not valid anymore.

        :param bank_id: Bank ID
        :param bank_name: Name of the Bank
        """
        super(Bank, self).__init__()
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.facilities = {}
        self.covenants = []
        self.__state_version = 0

    def add_facility(self, facility: Facility):
        if facility.bank_id != self.bank_id:
            raise ArgumentError(
                'Cannot add facility with bank_id={} to bank with bank_id={}'.format(
                    facility.bank_id, self.bank_id
                )
            )
        if facility.facility_id in self.facilities:
            raise ArgumentError('Facility with the same id already exists, got {}, existing {}.'.format(
                facility, self.facilities[facility.facility_id]
            ))
        self.facilities[facility.facility_id] = facility
        self.__state_version += 1
        self.logger.info('%s added to %s.', facility, self)

    def add_covenant(self, covenant: Covenant):
        if covenant.bank_id != self.bank_id:
            raise ArgumentError(
                'Cannot add covenant with bank_id={} to bank with bank_id={}'.format(
                    covenant.bank_id, self.bank_id
                )
            )
        if covenant.facility_id:
            facility = self.facilities.get(covenant.facility_id)
            if not facility:
                raise ArgumentError(
                    'Cannot add covenant to facility id={}, cannot find facility.'.format(
                        covenant.facility_id
                    )
                )
            facility.add_covenant(covenant)
        else:
            self.covenants.append(covenant)
            self.__state_version += 1
            self.logger.info('%s added to %s.', covenant, self)

    def get_loan_application(self, loan: Loan) -> Optional[LoanApplication]:
        for covenant in self.covenants:
            if not covenant.can_apply(loan):
                return None
        best_appl = None
        for fac in self.facilities.values():
            curr_appl = fac.get_loan_application(loan)
            if not curr_appl:
                continue
            if not best_appl:
                best_appl = curr_appl
            else:
                if curr_appl.expected_yield > best_appl.expected_yield:
                    best_appl = curr_appl
        if best_appl:
            best_appl = LoanApplication(
                best_appl.loan,
                best_appl.facility,
                best_appl.expected_yield,
                best_appl.facility_state_version,
                self.__state_version
            )
        return best_appl

    def apply_loan(self, application: LoanApplication) -> Optional[LoanAssignment]:
        if application.facility.facility_id not in self.facilities:
            raise ArgumentError(
                'Cannot apply loan to facility with id={} that does not belong to bank {}.'.format(
                    application.facility.facility_id, self.bank_name
                )
            )
        return application.facility.apply_loan(application)

    def __str__(self):
        return '{}(bank_id={}, bank_name="{}", __state_version={})'.format(
            type(self).__name__, self.bank_id, self.bank_name, self.__state_version
        )


class Repository(LoggingMixin):

    def __init__(self, banks: List[Bank] = None):
        # banks is a dictionary with "bank_id" as key and bank itself as value
        self.banks = {}
        self.loan_assignments = []
        for b in banks or []:
            self.add_bank(b)

    def apply_loan(self, loan: Loan) -> bool:
        """
        Application process consists of the following steps:
        1. Get loan application from each bank with calculated yield (see named tuple LoanApplication).
        2. Choose the best application among all banks (maximum expected_yield).
        3. Apply for the loan offer if any.

        :param loan: Loan to apply
        :return: True if applied successfully, False - if not
        """
        best_appl = None
        best_bank = None
        for bank in self.banks.values():
            curr_appl = bank.get_loan_application(loan)
            if not curr_appl:
                continue
            if not best_appl or curr_appl.expected_yield > best_appl.expected_yield:
                best_appl = curr_appl
                best_bank = bank
        if best_appl:
            loan_assig = best_bank.apply_loan(best_appl)
            if loan_assig:
                self.loan_assignments.append(loan_assig)
                self.logger.info('%s approved by %s.', loan_assig, best_bank)
                return True
            else:
                self.logger.debug('%s rejected by %s.', best_appl, best_bank)
        self.logger.debug('Did not find bank for %s.', loan)
        return False

    def add_bank(self, bank: Bank):
        if bank.bank_id in self.banks:
            raise ArgumentError('Bank with the same id already exists, got {}, existing {}.'.format(
                bank, self.banks[bank.bank_id]
            ))
        self.banks[bank.bank_id] = bank
        self.logger.info('%s added.', bank)

    def find_bank(self, bank_id: int) -> Optional[Bank]:
        return self.banks.get(bank_id)


def build_repo_from_csv(banks_path: str, facilities_path: str, covenants_path: str) -> Repository:
    """
    Build Repository instance with banks, facilities, and covenants loaded from CSV files.
    """
    logger = logging.getLogger('build_repo_from_csv')
    repo = Repository()
    for bank in load_banks_from_csv(banks_path):
        try:
            repo.add_bank(bank)
        except ArgumentError:
            logger.warning('Cannot add %s.', bank, exc_info=True)
    for fa in load_facilities_from_csv(facilities_path):
        try:
            bank = repo.find_bank(fa.bank_id)
            if bank:
                bank.add_facility(fa)
            else:
                logger.warning('Cannot find bank to add %s.', fa)
        except ArgumentError:
            logger.warning('Cannot add %s.', fa, exc_info=True)
    for co in load_covenants_from_csv(covenants_path):
        try:
            bank = repo.find_bank(co.bank_id)
            if bank:
                bank.add_covenant(co)
            else:
                logger.warning('Cannot find bank to add %s.', co)
        except ArgumentError:
            logger.warning('Cannot add %s.', co, exc_info=True)
    return repo


def load_banks_from_csv(file_path: str) -> List[Bank]:
    return [
        Bank(bank_id=int(raw['id']), bank_name=raw['name'])
        for raw in read_csv(file_path)
    ]


def load_facilities_from_csv(file_path: str) -> List[Facility]:
    return [
        Facility(
            bank_id=int(raw['bank_id']), facility_id=int(raw['id']),
            interest_rate=float(raw['interest_rate']), amount=int(float(raw['amount']))
        )
        for raw in read_csv(file_path)
    ]


def load_covenants_from_csv(file_path: str) -> List[Covenant]:
    covenants = []
    for raw_covenant in read_csv(file_path):
        if raw_covenant['max_default_likelihood']:
            covenants.append(MaxDefaultRateCovenant(
                int(raw_covenant['bank_id']),
                int(raw_covenant['facility_id']) if raw_covenant['facility_id'] else None,
                float(raw_covenant['max_default_likelihood'])
            ))
        if raw_covenant['banned_state']:
            covenants.append(GeoLocationCovenant(
                int(raw_covenant['bank_id']),
                int(raw_covenant['facility_id']) if raw_covenant['facility_id'] else None,
                raw_covenant['banned_state']
            ))
    return covenants


def load_loans_from_csv(loans_path: str) -> List[Loan]:
    return [
        Loan(
            id=int(raw['id']),
            amount=int(raw['amount']),
            interest_rate=float(raw['interest_rate']),
            default_likelihood=float(raw['default_likelihood']),
            state=raw['state']
        ) for raw in read_csv(loans_path)
    ]


def read_csv(file_path: str) -> List[dict]:
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


def write_csv(file_path: str, fieldnames: List[str], rows: List[dict]):
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main(banks_path: str, facilities_path: str, covenants_path: str, loans_path: str, assignments_path: str,
         yields_path: str):
    """
    Main entry function when executed in script mode.
    """
    repo = build_repo_from_csv(banks_path, facilities_path, covenants_path)
    loans = load_loans_from_csv(loans_path)
    for loan in loans:
        repo.apply_loan(loan)
    write_csv(
        assignments_path,
        ['loan_id', 'facility_id'],
        [a._asdict() for a in sorted(repo.loan_assignments, key=lambda i: i.loan_id)]
    )
    exp_yields = []
    for b in repo.banks.values():
        for f in b.facilities.values():
            exp_yields.append({'facility_id': f.facility_id, 'expected_yield': round(f.expected_yield)})
    write_csv(
        yields_path,
        ['facility_id', 'expected_yield'],
        sorted(exp_yields, key=lambda i: i['facility_id'])
    )
    logging.getLogger('main').info('Assigned %s loans of total %s in %s banks.',
                                   len(repo.loan_assignments), len(loans), len(repo.banks))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Run module in script mode. Supply all data as CSV files to calculate.'
    )
    parser.add_argument('banks_path',
                        help='Path to CSV file with banks.')
    parser.add_argument('facilities_path',
                        help='Path to CSV file with facilities.')
    parser.add_argument('covenants_path',
                        help='Path to CSV file with covenants.')
    parser.add_argument('loans_path',
                        help='Path to CSV file with loans.')
    parser.add_argument('assignments_path',
                        help='Path to CSV file to write assignments.')
    parser.add_argument('yields_path',
                        help='Path to CSV file to write yields.')
    args = vars(parser.parse_args())
    logging.basicConfig(
        level=logging.INFO, stream=sys.stdout,
        format='%(asctime)s\t[%(levelname)s]\t%(name)s\t%(message)s'
    )
    main(**args)


