# import pytest
from plates import is_valid

def test_no_numbers():
    assert is_valid("HELLO") == True

def test_wo_numbers():
    assert is_valid("CS05") == False

def test_no_numbers2():
    assert is_valid("CS50P") == False

def test_no_numbers3():
    assert is_valid("PI3.14") == False

def test_no_numbers4():
    assert is_valid("H") == False

def test_no_numbers43():
    assert is_valid("55CS50") == False

def test_no_numbers44():
    assert is_valid("554450") == False

def test_no_numbers4():
    assert is_valid("OUTATIME") == False
