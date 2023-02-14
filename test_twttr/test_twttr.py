from twttr import shorten

def main():
    test_upper_lover_case()
    test_capitalized_vowel_replacement()
    test_without_lowercase_vowel_replacement()
    test_printing_in_uppercase()


def test_upper_lover_case():
    assert shorten('twitter') == 'twttr'

def test_capitalized_vowel_replacement():
    assert shorten('TwiTtEr') == 'TwTtr'

def test_without_lowercase_vowel_replacement():
    assert shorten('Twitter') == 'Twttr'

def test_printing_in_uppercase():
    assert shorten('TWITTER') == 'TWTTR'

def test_omitting_number():
    assert shorten('123456') == '123456'

def test_omitting_punctuation():
    assert shorten ('..,!!?') == '..,!!?'



if __name__ == "__main__":
    main()