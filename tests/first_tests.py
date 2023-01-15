import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_division(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_multiply_calculate_subtraction(self):
        assert self.calc.subtraction(self, 7, 6) == 1

    def test_multiply_calculate_adding(self):
        assert  self.calc.adding(self, 2, 8) == 10
        