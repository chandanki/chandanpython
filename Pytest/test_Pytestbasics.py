import pytest

def test_m1():
    name = "pytest"
    print(name)
    assert name == "pytest", "test passed"

def test_m2():
    b = 2
    a = 1
    assert a+1 == b ,"test passed"
    #assert a == b , "test failed"