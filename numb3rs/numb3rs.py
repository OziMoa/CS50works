import re

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))



def validate(ip):
    if re.search( r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$" , ip ):
        numlist = ip.split('.')
        for n in numlist:
            if int(n) < 0 or int(n) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()