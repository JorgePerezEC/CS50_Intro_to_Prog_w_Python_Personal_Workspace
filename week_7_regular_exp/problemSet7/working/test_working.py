from working import convert
import pytest

def test_correctFormatHour():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_wrongFormatHour():
    with pytest.raises(ValueError):
        convert('9:00 AM - 5:00 PM')

def test_wrongMinutesValue():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:61 PM')

