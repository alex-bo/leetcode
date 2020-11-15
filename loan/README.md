# Run the script

Requirements: Python 3.7 runtime

Command line:
```
C:\affirm>python loan.py -h
usage: loan.py [-h]
               banks_path facilities_path covenants_path loans_path
               assignments_path yields_path

Run module in script mode. Supply all data as CSV files to calculate.

positional arguments:
  banks_path        Path to CSV file with banks.
  facilities_path   Path to CSV file with facilities.
  covenants_path    Path to CSV file with covenants.
  loans_path        Path to CSV file with loans.
  assignments_path  Path to CSV file to write assignments.
  yields_path       Path to CSV file to write yields.

optional arguments:
  -h, --help        show this help message and exit
```

# FAQ
1. How long did you spend working on the problem? What did you find to be the most
difficult part?
> 5.5 hours. Since I decided to implement brute-force solution, algorithm was not difficult.
> It took much more time to code all models according to business rules and add checks to comply with them.

2. How would you modify your data model or code to account for an eventual introduction
of new, as-of-yet unknown types of covenants, beyond just maximum default likelihood
and state restrictions?

> It would need a new class derived from `Covenant` that implements `def can_apply(self, loan: Loan) -> bool:` method.
> In addition, `load_covenants_from_csv` should be modified to load new covenants.

3. How would you architect your solution as a production service wherein new facilities can
be introduced at arbitrary points in time. Assume these facilities become available by the
finance team emailing your team and describing the addition with a new set of CSVs.

> I design relational database as a primary persistence storage.
> A separate script would periodically run and load "not yet processed" emails with CSV attachments.
> It will save new facilities to corresponding DB tables.
> The module that does loans applications would be a web service pointed to the same database.

4. Your solution most likely simulates the streaming process by directly calling a method in
your code to process the loans inside of a for loop. What would a REST API look like for
this same service? Stakeholders using the API will need, at a minimum, to be able to
request a loan be assigned to a facility, and read the funding status of a loan, as well as
query the capacities remaining in facilities.

> Service will have these methods:
> 
> [GET] /loan/123
>
> Return loan by ID 123
>
> [POST] /loans [body should be similar to `Loan` tuple]
> 
> Find bank/facility and save loan object to the DB table (`Repository.apply_loan`)
>
> [GET] /bank/123
>
> Get bank by ID (`Repository.find_bank`)
>
> [POST] /bank/
>
> Add bank (`Repository.add_bank`)
>
> [GET] /bank/123/facilities/456
>
> Get facility by ID
>
> [PUT] /bank/123/facilities
>
> Add bank (`Bank.add_facility`)

5. How might you improve your assignment algorithm if you were permitted to assign loans
in batch rather than streaming? We are not looking for code here, but pseudo code or
description of a revised algorithm appreciated.

> Since application is already split in two steps: `get_loan_application` and `apply_loan`
> I would change method signature to `Repository.apply_loan(loans: List[Loan]) -> List[Loan]`
> The logic would call get_loan_application for each loan and choose one with hightest expected_yield.
> Then move best loan to settled list and repeat for the remaining loans. 

6. Discuss your solution’s runtime complexity.

> Complexity of current implementation with one loan at a time is linear to number of facilities.