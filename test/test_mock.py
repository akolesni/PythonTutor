import unittest.mock as mock
import random

from src.calculator import Calculator


# https://www.yourtodo.ru/posts/37/
def test_sum(mocker):
    sum_mocker = mocker.patch.object(Calculator, "sum", return_value=9)
    calculator = Calculator()

    assert calculator.sum(2, 3) == 9
    assert calculator.sum(0, 0) == 9

    assert sum_mocker.call_count == 2
    calls = [mock.call(2, 3), mock.call(0, 0)]
    sum_mocker.assert_has_calls(calls, any_order=False)


def test_get_random(mocker):
    mocker.patch('random.randint')
    Calculator.get_random(0, 9)
    random.randint.assert_called_once_with(0, 9)


def test_magic_mock():
    calculator = Calculator()
    calculator.sum = mock.MagicMock(return_value=3)
    calculator.sum(0, 9)
    calculator.sum.assert_called_with(0, 9)
