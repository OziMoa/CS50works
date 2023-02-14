import random as r


def main():
    level = get_level()
    tcount = generate_integer(level)
    print(f'Score: {tcount}')

def get_level():
    while True:
        try:
            linp = int(input('Level: '))
            if linp in [1,2,3]:
                return linp
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    count = 11
    num1 = 0
    num2 = 0
    tcount = 0
    fcount = 0

    while 1 < count:
        if level == 1:
            num1 = r.randint(0,9)
            num2 = r.randint(0,9)
        elif level == 2:
            num1 = r.randint(10,99)
            num2 = r.randint(10,99)
        elif level == 3:
            num1 = r.randint(100,999)
            num2 = r.randint(100,999)
        while fcount < 4 and 1 < count :
            try:
                total = int(input(f'{num1} + {num2} = '))
                if total == num1 + num2:
                    tcount += 1
                    count -= 1
                    break
                else:
                    if fcount < 2:
                        fcount += 1
                        print ('EEE')
                        continue
                    else:
                        print ('EEE')
                        print (f'{num1} + {num2} = {num1+num2}')
                        fcount = 0
                        count -= 1
                        break
            except ValueError:
                print('EEE')
                if fcount < 2:
                    fcount += 1
                    continue
                else:
                    print (f'{num1} + {num2} = {num1+num2}')
                    fcount = 0
                    count -= 1
                    break



    return(tcount)

if __name__ == "__main__":
    main()