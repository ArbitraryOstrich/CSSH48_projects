import calculator
import pytest


def test_two_plus_two():
    """
    Asserts that given the parameters 2 and 2, the add function should return 4
    """
    assert calculator.add(2, 2) == 4


def test_three_plus_two():
    """
    Asserts that given the parameters 3 and 2, the add function should return 5
    """
    assert calculator.add(3, 2) == 5


def test_three_plus_two_plus_twenty():

    """
    Asserts that given the parameters 3, 2 and 20, the add function should
    return 5
    """

    assert calculator.add(3, 2, 20) == 25


def test_no_parameters():
    """
    Asserts that when no parameters are provided, 0 should be returned.
    """
    assert calculator.add() == 0


def test_decimal_addition_case():
    """
    Asserts that .1 + .2 =~ .3
    """
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)
