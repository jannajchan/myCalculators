from decimal import Decimal
from .basic_calculator import BasicCalculator # Relative import

class FinancialCalculator(BasicCalculator):
    def monthly_interest(self, annual_interest_rate):
        # return self.divide(annual_interest_rate, 12)
        return Decimal(str(annual_interest_rate)) / Decimal("12")

    def months_from_years(self, years):
        # return self.multiply(years, 12)
        return Decimal(str(years)) * Decimal("12")