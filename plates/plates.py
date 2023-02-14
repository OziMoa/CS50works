def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or 7 < len(s):
        return False
    counta = 0
    countb = 0
    i = 0
    while i < len(s):

        if s[i].isalpha():
            counta += 1
            i += 1
        elif s[i].isdigit():
            countb += 1
            i += 1
        else:
            i += 1
            return False

    front = s[0:counta]
    end = s[counta:counta+countb]
    if len(end)>0:
        if end[0]=='0':
            return False
        elif len(front)<2:
            return False
        elif end.isalpha():
            return False
        elif  front+end == s:
            return True
    else:
        if not front.isalpha():
            return False
        else:
            return True


if __name__ == '__main__':
    main()