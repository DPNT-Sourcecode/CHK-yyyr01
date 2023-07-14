from lib.solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_params_are_integers(self):
        with pytest.raises(Exception):
            assert sum_solution("5", [34])



