"""
A module to implement the BasicCalcualtor.
"""
from decimal import Decimal

class BasicCalculator:
    """
    A class for arithmetic operations on numbers    
    """
    def add(self, x, y):
        # return np.add(x, y)
        return Decimal(x) + Decimal(y)

    def subtract(self, x, y):
        # return np.subtract(x, y)
        return Decimal(x) - Decimal(y)

    def multiply(self, x, y):
        # return np.multiply(x, y)
        return Decimal(x) * Decimal(y)

    def divide(self, x, y):
        # return np.divide(x, y)
        return Decimal(x) / Decimal(y)

    def power(self, x, y):
        # return np.power(x, y)
        return Decimal(x) ** Decimal(y)