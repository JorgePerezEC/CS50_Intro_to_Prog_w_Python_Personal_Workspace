from um import count

def test_correctCount():
    assert count("hello, um, world") == 1

def test_wrongWord():
    assert count("yum") == 0

def test_CaseInsensitive():
    assert count("yum Um") == 1

def test_SpaceBetween():
    assert count("yum um ") == 1

def test_Sign():
    assert count("um?") == 1

def test_1():
    assert count("um") == 1

def test_correctCount2():
    assert count("hello, um, world yummy pizza. I'm very humgry") == 1
