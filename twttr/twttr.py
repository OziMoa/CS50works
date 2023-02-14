#twitter to twttr

snt = input('input your sentence: ')
out = []
for o in snt:
    if o.lower() in ['a','e','i','o','u']:
        continue
    else:
        out.append(o)

print(''.join(out))