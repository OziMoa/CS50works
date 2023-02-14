from plates import is_valid

def test_without_alphabetical():
    assert is_valid('11') == False
    assert is_valid('123456') == False

def test_without_length():
    assert is_valid('5A') == False
    assert is_valid('22') == False
    assert is_valid('AA') == True
    assert is_valid('OUTOFTIME') == False
    assert is_valid('A2') == False
    assert is_valid('OUTTIME') == False

def test_number_placement():
    assert is_valid('CS50P') == False
    assert is_valid('CS50') == True

def test_zero_placement():
    assert is_valid('CS05') == False
    assert is_valid('ABC012') == False
    assert is_valid('ABC012') == False

def test_alphanumeric_char():
    assert is_valid('PI3.14') == False
    assert is_valid('PB3.14') == False

