
from ..code import add_one

def test_add_one_pos():
    assert add_one(5) == 6

def test_add_one_zero() :
    assert add_one(0) == 1

def test_add_one_neg() :
    assert add_one(-5) == -4
