#list

itlist = {}

while True:

    try:
        obj = input().strip().upper()
        if obj in itlist:
            itlist[obj] = itlist[obj]+1
        else:
            itlist[obj] = 1

    except EOFError:
        for i in sorted(itlist.keys()):
            print(itlist[i], i)
        break