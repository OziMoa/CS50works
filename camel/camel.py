#CamelCase

inp = input ('input variable: ')
out = inp

for o in inp:
    if o == o.upper():
        out = out.replace(o, f'_{o.lower()}')

print(out)