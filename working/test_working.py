from working import convert
import pytest


def main():
    test_correct()
    test_incorrect_hour()
    test_incorrect_minute()
    test_invalidFormat()


def test_correct():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'

def test_incorrect_hour():
    with pytest.raises(ValueError):
        convert('18:10 AM to 14:10 PM')
        convert('21 AM to 24 PM')
def test_incorrect_minute():
    with pytest.raises(ValueError):
        convert('8:60 AM to 4:60 PM')
        convert('12:80 AM to 12:00 PM')

def test_invalidFormat():
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("9:72 to 6:30")

if __name__ == "__main__":
    main()