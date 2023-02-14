from um import count

def main():
    test_inword()
    test_withSpaces()
    test_caseinsensitive()

def test_inword():
    assert count('Umbrella') == 0
    assert count('yummy') == 0
    assert count('sum') == 0
    assert count('um?') == 1

def test_withSpaces():
    assert count(' um ') == 1
    assert count('well um, ') == 1
    assert count('um, hello um ') == 2

def test_caseinsensitive():
    assert count('Um') == 1
    assert count('UM, Hello') == 1
    assert count('hi, uM, my name is ummar') == 1





if __name__ == '__main__':
    main()