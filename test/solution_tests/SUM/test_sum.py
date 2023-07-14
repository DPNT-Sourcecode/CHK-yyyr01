from lib.solutions.SUM import sum_solution
import pytest


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_params_are_integers(self):
        with pytest.raises(Exception) as err:
            sum_solution("5", [34])
    
    def test_params_are_integers_bewteen_0_100(self):
        with pytest.raises(Exception) as err:
            sum_solution(5, 101)
            sum_solution(1005, 1)
            sum_solution(1005, 101)
