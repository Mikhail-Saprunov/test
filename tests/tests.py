import pytest

import self

from app.Calc import Calculator

def test_adding():
    assert Calculator.adding(self, 1, 1) == 2

def test_multiply():
    assert Calculator.multiply(self, 2, 2) == 4

def test_division():
    assert Calculator.division(self, 2, 2) == 1

def test_subtraction():
    assert Calculator.subtraction(self, 2, 1) == 1
