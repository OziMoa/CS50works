import inflect

p = inflect.engine()

base = 'Adieu, adieu, to '
olist = []


while True:
    try:
        to = input('')
        olist.append(to)
        tlist = p.join(olist)


    except EOFError:
        print(base+tlist)
        break
