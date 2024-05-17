from calculator import square
import sys
import pytest

# def main():
#     test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
# if __name__ == "__main__":
#     main()
