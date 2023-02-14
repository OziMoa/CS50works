import random as r

val = 0

while True:
    try:
        n = int(input('level: '))
        if n < 1 or 100 < n:
            continue
        else:
            val= r.randint(1,n)
            break
    except ValueError:
        continue

while True:
    try:
        guess = int(input('Guess: '))
        if guess < 1 or 100 < guess:
            continue
        if guess == val:
            print ('Just right!')
            break
        elif guess < val:
            print ('Too small!')
        elif guess > val:
            print ('Too large!')

    except ValueError:
        continue
    except EOFError:
        break

