import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^.+src=.+youtube\.com.+>.+$",s):
        saperation = s.split('/embed/')
        lastpart =''
        for ch in saperation[1]:
            if ch == "'" or ch == '"':
                break
            else:
                lastpart += ch
        if lastpart =='':
            return None
        else:
            return (f'https://youtu.be/{lastpart}')




if __name__ == "__main__":
    main()