import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from financial_calculator import FinancialCalculator

# Set precision and rounding for financial accuracy
getcontext().prec = 28
getcontext().rounding = ROUND_HALF_EVEN

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILENAME = "mortgage_report.xlsx"

class MortgageCalculator(FinancialCalculator):
    def __init__(self, loan_amount, annual_interest_rate, years):
        super().__init__() # Initialize the parent attributes and functions by calls the constructor of FinancialCalculator, which itself inherits from BasicCalculator.
        # self.loan_amount = loan_amount
        self.loan_amount = Decimal(str(loan_amount))
        self.annual_interest_rate = Decimal(str(annual_interest_rate))
        self.years = Decimal(str(years))

        self.monthly_interest_rate = self.monthly_interest(self.annual_interest_rate)
        self.num_months = self.months_from_years(self.years)

    """
    🧮 Formula for Monthly Payment:
        M = P  ⋅  r(1+r)^n
            -------------
                (1+r)^n − 1
    Where:
        M = monthly payment
        P = loan amount (self.loan_amount)
        r = monthly interest rate (self.monthly_interest_rate)
        n = number of months (self.num_months)
    """
    def calculate_monthly_payment(self):
        P = self.loan_amount
        r = self.monthly_interest_rate
        n = self.num_months

        if r == 0: # Special case: zero interest loan
            # return self.divide(P, n)
            return P/n
        
        # numerator = self.multiply(r, self.power(self.add(1, r), n))
        # denominator = self.subtract(self.power(self.add(1, r), n), 1)
        # return self.multiply(P, self.divide(numerator, denominator))

        # To avoid redundant calls, which may cause tiny rounding differences. So store it once.
        one_plus_r = Decimal("1") + r
        factor = one_plus_r ** n
        monthly_payment = P * (r * factor) / (factor - Decimal("1"))
        return monthly_payment.quantize(Decimal("0.01"))
    
    def total_payment(self):
        # return self.multiply(self.calculate_monthly_payment(), self.num_months)
        return (self.calculate_monthly_payment() * self.num_months).quantize(Decimal("0.01"))

    def total_interest(self):
        # return self.subtract(self.total_payment(), self.loan_amount)
        return (self.total_payment() - self.loan_amount).quantize(Decimal("0.01"))
    
    """
    Excel Export with pandas or openpyxl? This example use pandas.
    🧾 pandas (easier if you're familiar with DataFrames)
    📊 openpyxl (more control over Excel formatting)
    """
    def export_to_excel(self, filename=EXCEL_FILENAME):
        data = {
            "Loan Amount": [self.loan_amount],
            "Annual Interest Rate": [self.monthly_interest_rate * 12],
            "Monthly Interest Rate": [self.monthly_interest_rate],
            "Loan Term (months)": [self.num_months],
            "Monthly Payment": [self.calculate_monthly_payment()]
        }

        df = pd.DataFrame(data)
        excel_path = os.path.join(BASE_DIR, filename)
        df.to_excel(excel_path, index=False)
        print(f"📁 Exported mortgage report to {excel_path}")

"""
# -Bash (Example)------------------------------------------------------------------------------------
# | python myCalculators\mortgage_calculator.py --loan 300000 --rate 0.05 --years 30                |
# ---------------------------------------------------------------------------------------------------
"""
def main_cli(): # CLI = Command Line Interface
    import argparse
    from decimal import Decimal

    parser = argparse.ArgumentParser(description="Mortgage Calculator CLI")
    parser.add_argument("--loan", type=Decimal, required=True, help="Loan amount (e.g. 300000)")
    parser.add_argument("--rate", type=Decimal, required=True, help="Annual interest rate (e.g. 0.05)")
    parser.add_argument("--years", type=int, required=True, help="Loan term in years (e.g. 30)")

    args = parser.parse_args()

    mortgage = MortgageCalculator(args.loan, args.rate, args.years)
    monthly_payment = mortgage.calculate_monthly_payment()
    total_payment = mortgage.total_payment()
    total_interest = mortgage.total_interest()

    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment:   ${total_payment:.2f}")
    print(f"Total Interest:  ${total_interest:.2f}")

if __name__ == "__main__":
    main_cli()
