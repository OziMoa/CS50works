#Fuel gauge

while True:
    inn = input('please enter value in division : ')
    try:
        x,y = inn.split('/')
        x,y = int(x), int(y)
        if x/y <= 0.01 :
            print ('E')

        elif x > y:
            continue

        elif x/y >= 0.99 and x/y<=100 :
            print ('F')

        else:
            val=round((x/y)*100)
            print ( f'{val}%' )

        break

    except ValueError:
        print ('Values must be integer!')
    except ZeroDivisionError:
        print ("Y value cant be '0' ")
