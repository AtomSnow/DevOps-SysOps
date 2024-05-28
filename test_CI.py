import pytest
from CI import addition, soustraction, multiplication, division

def test_add():
    assert addition(2,4) == 6

def test_sous():
    assert soustraction(4,3) == 1

def test_mul():
    assert multiplication(7,5) == 35

def test_div():
    assert division(10,2) == 5
