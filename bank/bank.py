#greet with hello
#bank etc

def main():
    word = input('say something: ')
    out = value(word)
    print (f"${out}")


def value(greeting):
    says = greeting.lower().strip()
    if 'hello' in says:
        return 0
    elif says[0] == 'h':
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()