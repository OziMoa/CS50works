def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not isinstance(s, str):
        return False 

    if s is int:
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    for l in range(2):
        if s[l].isalpha() == False:
            return False

    c=0
    while c<len(s):
        if s[c].isalpha() == False:
            if s[c] == "0":
                return False
            else:
                break
        c += 1

    for m in range(len(s)):
        if s[m] in [" ", ".", "?", "!",  ",", ":", ";", "(", ")",
        "[", "]", "'", "-", '"', "/", "\\", "`", "@", "#", "*",]:
            return False

        if s[m].isdigit():
            if not s[m:].isdigit():
                return False

    return True


if __name__ == '__main__':
    main()
