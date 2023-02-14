import sys
from pyfiglet import Figlet
import random

fig=Figlet()

flist = fig.getFonts()
leno = len(sys.argv)

if leno not in [1, 3]:
    sys.exit('Invalid usage')

elif leno == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '-font' :
        if sys.argv[2] in flist:
            fig.setFont(font = sys.argv[2])
            word = input()
            print(fig.renderText(word))
        else:
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')

elif leno == 1:
    ranfont = random.choice(flist)
    fig.setFont(Font=ranfont)
    word = input()
    print(fig.renderText(word))


