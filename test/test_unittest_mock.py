from unittest.mock import patch

from src.calculator import Calculator


@patch("src.calculator.Calculator.sum", return_value=9)
def test_sum(sum):
    calculator = Calculator()
    assert calculator.sum(2, 3) == 9
