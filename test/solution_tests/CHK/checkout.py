from lib.solutions.CHK import checkout


class TestSum():
    def test_checkout_valid(self):
        assert checkout("A") == 50

    def test_checkout_invalid(self):
        assert checkout("PA") == 50
