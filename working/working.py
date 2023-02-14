import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r'(^.+(:.+)? AM to .+(:.+)? PM$)|(^.+(:.+)? PM to .+(:.+)? AM$)',s):
        if s[-2:] == 'PM':
            sap = s.split('AM to ')
            am = sap[0]
            pm = sap[1].replace('PM','').strip()
            ver = 1
        else:
            sap = s.split('PM to ')
            pm = sap[0]
            am = sap[1].replace('AM','').strip()
            ver = 2

        if re.search(r'^.+:.+$',am):
            aM=am.split(':')
            if int(aM[1])<60 and int(aM[1])>=0 and int(aM[0])>=0 and int(aM[0])<13 :
                afront = int(aM[0])
                if afront == 12:
                    afront = 0
                aback = int(aM[1].strip())
            else:
                raise ValueError

        else:
            if int(am)>=0 and int(am)<13:
                afront = int(am)
                if afront == 12:
                    afront = 0
                aback = 0

        if re.search(r'^.+:.+$',pm):
            pM=pm.split(':')
            if int(pM[1])<60 and int(pM[1])>=0:
                bfront = int(pM[0])+12
                if bfront == 24:
                    bfront = 12
                bback = int(pM[1])

            else:
                raise ValueError
                
        else:
            bfront= int(pm)+12
            if bfront == 24:
                bfront = 12
            bback=0


        if ver==1:
            return (f'{afront:02}:{aback:02} to {bfront:02}:{bback:02}')
        else:
            return (f'{bfront:02}:{bback:02} to {afront:02}:{aback:02}')

    else:
        raise ValueError


if __name__ == "__main__":
    main()