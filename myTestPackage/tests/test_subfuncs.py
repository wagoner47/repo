
from ..subfuncs import function_b, subfunction_b

def test_function_b_neg() :
    assert function_b(-1) == -2

def test_function_b_zero() :
    assert function_b(0) == 10

def test_function_b_small() :
    assert function_b(1) > 10
    assert function_b(1) < 100

def test_function_b_big() :
    assert function_b(2) > 100