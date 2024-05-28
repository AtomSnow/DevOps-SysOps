import pytest
from CI import addition, soustraction, multiplication, division

def test_add():
    assert addition(2,4) == 6
    #assert addition(1,3) == 5

def test_sous():
    assert soustraction(4,3) == 1
    #assert soustraction(3,3) == 1

def test_mul():
    assert multiplication(7,5) == 35
    #assert multiplication(1,1) == 3

def test_div():
    assert division(10,2) == 5
    #assert division(5,0) == 1