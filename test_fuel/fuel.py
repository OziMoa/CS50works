def main():
    inn = input('please enter value in division : ')
    firstcheck = convert(inn)
    print (gauge(firstcheck))

def convert(fraction):
    while True:
        try:
            x,y = fraction.split('/')
            x,y = int(x), int(y)
            p = x/y
            if p >= 0 and p <= 1:
                return (round(p*100))
            else:
                fraction = input("please enter value in division : ")
                continue

        except (ValueError, TypeError, ZeroDivisionError):
            raise


def gauge(percentage):

        if percentage <= 1 :
            return ('E')

        elif percentage >= 99:
            return ('F')

        else:
            return ( f'{percentage}%' )


if __name__ == "__main__":
    main()