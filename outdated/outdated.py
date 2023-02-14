monthlist= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input('Date: ')
    try:
        m, d, y = date.split('/')
        if int(d) <= 31 and int(m) <= 12:
            print(int(y), f"{int(m):02}", f"{int(d):02}", sep='-')
            break
        else:
            continue
    except (TypeError,ValueError) :
        try:
            dm, y = date.split(', ')
            m, d = dm.split(' ')
            if m in monthlist and int(d) <= 31:
                print(int(y), f"{monthlist.index(m)+1:02}", f"{int(d):02}", sep='-')
                break
            else:
                continue
        except (TypeError,ValueError):
            continue


