from bank import value

def main():
     test_incorrect_value()
     test_case_intensitivity()
     test_entire_phrase()
     test_blank()
     test_other_words()


def test_entire_phrase():
    assert value('Hello there,') == 0
    assert value('Hello how can i help') == 0

def test_case_intensitivity():
    assert value('HELLO') == 0
    assert value('HelLO') ==0

def test_incorrect_value():
    assert value ('whats up') == 100
    assert value ('Welcome') == 100

def test_blank():
    assert value('Hello') == 0
    assert value ('yo') == 100

def test_other_words():
    assert value('hi') == 20
    assert value('how are your') == 20



if __name__ == '__main__':
    main()
