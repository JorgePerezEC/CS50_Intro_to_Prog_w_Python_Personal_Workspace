from twttr import shorten
# from twttr_c import shorten

def test_replaces_vowels():
    assert shorten('Twitter') == 'Twttr'

def test_replaces_vowels_in_capital():
    assert shorten("WHAT's your name?") == "WHT's yr nm?"

def test_replaces_vowels_in_lowercase():
    assert shorten('able') == 'bl'

def test_omits_uppercase():
    assert shorten('CS50') == 'CS50'

def test_omits_numbers():
    assert shorten("123") == '123'

def test_omits_punctuations():
    assert shorten('a,d!') == ',d!'
