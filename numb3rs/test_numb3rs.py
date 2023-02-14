from numb3rs import validate


def main():
    test_format()
    test_range()

def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1') == False
    assert validate(r'1.5.3.2') == True
    assert validate(r'1.8.5') == False

def test_range():
    assert validate(r'1.1.1.1') == True
    assert validate(r'512.58.62.48') == False
    assert validate(r'256.256.256.256') == False
    assert validate(r'75.456.76.65') == False
    assert validate(r'500.200.100.28') == False

if __name__ == "__main__":
    main()
