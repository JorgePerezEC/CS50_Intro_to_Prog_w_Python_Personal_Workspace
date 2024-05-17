from numb3rs import validate

def test_incorrect_values():
    assert validate("256.256.0.0") == False

def test_correct_values():
    assert validate("255.255.0.1") == True

def test_correct2_values():
    assert validate("ipAddress") == False

def test_incorrect_values():
    assert validate("255.256.0.0") == False

