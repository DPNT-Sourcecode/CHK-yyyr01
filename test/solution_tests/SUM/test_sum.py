from lib.solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    def test_checkout_valid(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_invalid(self):
        assert checkout_solution.checkout("PA") == -1

    def test_checkout_valid_multiple(self):
        assert checkout_solution.checkout("AAA") == 100
        assert checkout_solution.checkout("ADA") == 115


