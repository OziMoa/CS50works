from datetime import date
import inflect
import operator
import sys
import re



def main():
    datee = input ('please enter date in proper format: ')
    print (total(datee))

def total(datee):
    dattime = datecheck(datee)
    today = date.today()
    passes = operator.__sub__(today, dattime)
    return (converter(passes).capitalize().replace(' and','')+ ' minutes')

def datecheck(datee):
    if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$' , datee):
        try:
            return date.fromisoformat(datee)
        except ValueError:
            sys.exit('Invalid Date')
    else:
        sys.exit('Invalid Format')

def converter(passes):
    inf = inflect.engine()
    return  inf.number_to_words(passes.days*24*60)



if __name__ == "__main__":
    main()