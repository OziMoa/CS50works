from tabulate import tabulate as tab
import sys
import csv


def main():
    filename = readlne()
    menu = listread(filename)
    print(tab(menu,headers="keys",tablefmt="grid"))

def listread(listname):
    pzz =[]
    try:
        name= listname.split(".")
        if name[1] != 'csv':
            sys.exit('Not a CSV file')
        else:
            with open(listname, 'r') as file:
                lidi = csv.DictReader(file)
                for row in lidi:
                    pzz.append(row)
            return pzz

    except FileNotFoundError:
        sys.exit('File does not exist')

def readlne():
    num = len(sys.argv)

    if num == 1:
        sys.exit('Too few command-line arguments')
    elif num > 2:
        sys.exit('Too many command-line arguments')
    else:
        return sys.argv[1]


if __name__ =="__main__":
    main()