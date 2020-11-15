import unittest
from unittest import mock

from loan.loan import MaxDefaultRateCovenant, Loan, GeoLocationCovenant, Facility, Bank, LoanApplication, \
    LoanAssignment


class CovenantTest(unittest.TestCase):

    def test_MaxDefaultRateCovenant(self):
        c = MaxDefaultRateCovenant(1, 1, .04)
        self.assertTrue(c.can_apply(Loan(1, 123, .1, .03, 'CA')))
        self.assertTrue(c.can_apply(Loan(1, 123, .1, .04, 'CA')))
        self.assertFalse(c.can_apply(Loan(1, 123, .1, .05, 'CA')))
        self.assertFalse(c.can_apply(Loan(1, 123, .1, .06, 'CA')))

    def test_GeoLocationCovenant(self):
        c = GeoLocationCovenant(1, 1, 'CA')
        self.assertTrue(c.can_apply(Loan(1, 123, .1, .03, 'LA')))
        self.assertTrue(c.can_apply(Loan(1, 123, .1, .04, 'TN')))
        self.assertFalse(c.can_apply(Loan(1, 123, .1, .05, 'CA')))


class FacilityTest(unittest.TestCase):

    def test_apply_loan__valid_loan__success(self):
        f = Facility(1, 1, .01, 1000)
        loan = Loan(1, 100, .05, .01, 'CA')

        appl = f.get_loan_application(loan)
        assignment = f.apply_loan(appl)

        self.assertIsNotNone(assignment)
        self.assertEqual(f.facility_id, assignment.facility_id)
        self.assertEqual(loan.id, assignment.loan_id)
        self.assertEqual(900, f.amount)
        self.assertEqual(2.95, f.expected_yield)

    def test_apply_loan__state_changed__ignore(self):
        f = Facility(1, 1, .01, 1000)
        loan = Loan(1, 100, .05, .01, 'CA')

        appl = f.get_loan_application(loan)
        f.add_covenant(
            mock.Mock(bank_id=1, facility_id=1, can_apply=mock.Mock(return_value=True))
        )
        assignment = f.apply_loan(appl)

        self.assertIsNone(assignment)

    def test_apply_loan__negative_yield__ignore(self):
        f = Facility(1, 1, .02, 1000)
        loan = Loan(1, 100, .01, .01, 'CA')

        appl = f.get_loan_application(loan)

        self.assertIsNone(appl)

    def test_apply_loan__covenant_not_met__ignore(self):
        f = Facility(1, 1, .01, 1000)
        covenant = mock.Mock(bank_id=1, facility_id=1, can_apply=mock.Mock(return_value=False))
        f.add_covenant(covenant)
        loan = Loan(1, 100, .05, .01, 'CA')

        appl = f.get_loan_application(loan)

        self.assertIsNone(appl)
        covenant.can_apply.assert_called_once_with(loan)

    def test_apply_loan__insufficient_amount__ignore(self):
        f = Facility(1, 1, .01, 10)
        loan = Loan(1, 100, .05, .01, 'CA')

        appl = f.get_loan_application(loan)

        self.assertIsNone(appl)


class BankTest(unittest.TestCase):

    def test_apply_loan__two_valid_loan__pick_best_one(self):
        bank = Bank(1, 'Test Bank')
        loan = Loan(1, 100, .05, .01, 'CA')
        best_assign = LoanAssignment(loan_id=12, facility_id=34)
        best_facility = mock.Mock(
            bank_id=1,
            apply_loan=mock.Mock(return_value=best_assign)
        )
        best_application = LoanApplication(loan, best_facility, 123.45, 1, None)
        best_facility.get_loan_application = mock.Mock(
            return_value=best_application
        )
        bank.add_facility(best_facility)
        bank.add_facility(mock.Mock(
            bank_id=1,
            get_loan_application=mock.Mock(
                return_value=LoanApplication(loan, None, 12.34, 1, None)
            )
        ))

        appl = bank.get_loan_application(loan)
        assn = bank.apply_loan(appl)

        self.assertEqual(best_application.loan, appl.loan)
        self.assertEqual(best_application.facility, appl.facility)
        self.assertEqual(best_application.expected_yield, appl.expected_yield)
        self.assertEqual(best_application.facility_state_version, appl.facility_state_version)
        self.assertEqual(best_assign, assn)


