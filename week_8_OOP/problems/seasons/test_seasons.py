from seasons import validate, res_dates
import pytest

def test_correct_date_format():
    assert validate("1996-05-10") == "1996-05-10"

def test_wrong_date_format():
    with pytest.raises(ValueError):
        validate("1996/05/10")

def test_correct_diff_dates():
    assert res_dates("1996-05-10") == "Fourteen million, seven hundred twenty-six thousand, eight hundred eighty minutes"

def test_wrong_diff_dates():
    with pytest.raises(ValueError):
        res_dates("1996/05/10")
