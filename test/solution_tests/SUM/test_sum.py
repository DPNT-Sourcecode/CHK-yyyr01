from lib.solutions.CHK import checkout_solution
import pytest


class TestCheckout():
    def test_checkout_valid(self):
        assert checkout_solution.checkout("A") == 50

    def test_checkout_invalid(self):
        assert checkout_solution.checkout("3A") == -1

    def test_checkout_valid_multiple_without_offer(self):
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("ADA") == 115

    def test_checkout_valid_multiple_with_offer(self):
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("ADA") == 115
        assert checkout_solution.checkout("ABAB") == 145
        assert checkout_solution.checkout("AABAB") == 175
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout_get_free_B_with_offer(self):
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEBB") == 110
        assert checkout_solution.checkout("EABB") == 135
        assert checkout_solution.checkout("EBB") == 85
        assert checkout_solution.checkout("EABD") == 135

    def test_checkout_get_free_F_with_offer(self):
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("EEBFB") == 120
        assert checkout_solution.checkout("FFFFFFF") == 50
        assert checkout_solution.checkout("EAFF") == 110
        assert checkout_solution.checkout("FFFF") == 30

    def test_checkout_new_items(self):
        assert checkout_solution.checkout("EEBZ") == 130
        assert checkout_solution.checkout("RRRQ") == 150
        assert checkout_solution.checkout("RRRR") == 200
        assert checkout_solution.checkout("HERB") == 130
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("AAANNNM") == 250
        assert checkout_solution.checkout("HHHHH") == 45
        assert checkout_solution.checkout("HHHHHHHHHH") == 80
