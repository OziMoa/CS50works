def main():
    inp = input ('what time is it ? ')
    ctime = convert(inp)
    if 7 <= ctime and ctime <= 8:
        print ('breakfast time')
    elif 12 <= ctime and ctime <= 13:
        print ('lunch time')
    elif 18 <= ctime and ctime <= 19:
        print ('dinner time')

dc camel


def convert(time):
    h , m = time.split(':')
    h, m = float(h), float(m)
    m = m/60
    return h+m
    ...


if __name__ == "__main__":
    main()