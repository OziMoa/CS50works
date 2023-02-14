x, y, z = input('expression : ').split()
x,z = float(x), float(z)
match y:
    case '+':
        print(round(x+z,1))
    case '-':
        print(round(x-z,1))
    case '*':
        print(round(x*z,1))
    case '/':
        if z != 0:
            print(round(x/z,1))
