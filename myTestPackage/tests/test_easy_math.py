
from myTestPackage import easy_math
import math

def test_function_a_default() :
    default = 180
    expect = math.sin(math.radians(default)/2)/math.sin(math.radians(default))
    assert easy_math.function_a() == expect

def test_function_a() :
    angle = 200
    expect = math.sin(math.radians(angle)/2)/math.sin(math.radians(angle))
    assert easy_math.function_a(angle) == expect