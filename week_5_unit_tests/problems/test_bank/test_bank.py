from bank import value

def test_incorrect_values():
    assert value("50") == 100

def test_case_insensitivity():
    assert value("Hello George") == 0

def test_incorrect_values():
    assert value("hey") == 20

def test_empty():
    assert value("") == 100
