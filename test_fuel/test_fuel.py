from fuel import convert, gauge
import pytest

def main():
    test_percentage()
    test_full()
    test_empty()
    test_zerodiv()
    test_string()

def test_percentage():
    assert convert('3/5') == 60 and gauge (60) == '60%'
    assert convert('2/5') == 40 and gauge (40) == '40%'

def test_full():
    assert convert('5/5') == 100 and gauge (100) == 'F'
    assert convert('99/100') == 99 and gauge (99) == 'F'

def test_empty():
    assert convert('0/5') == 0 and gauge (0) == 'E'
    assert convert('1/100') == 1 and gauge (1) == 'E'

def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_string():
    with pytest.raises(ValueError):
        convert('cat/dog')


if __name__ == "__main__":
    main()