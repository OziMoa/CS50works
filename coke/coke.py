#coke machine

amount = 0

while amount < 50:
    insert = int(input ('please insert coin: '))
    if insert in [5, 10, 25]:
        amount += insert
        if amount < 50:
            print (f'Amount due: {50-amount}')
        else:
            print (f'Change owed: {amount-50}')
    else:
        print (f'Amount due: {50-amount}')
        continue
