from seasons import total

def main():
    test_correct()

def test_correct():
    assert total('2022-01-04') == 'Five hundred twenty-five thousand, six hundred minutes'
    assert total('2021-01-04') == 'One million, fifty-one thousand, two hundred minutes'
#    assert total('February 6th, 1998') == None
#    assert total('2021-01-34') == None


if __name__ == '__main__':
    main()