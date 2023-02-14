import sys
from PIL import Image as img
from PIL import ImageOps



def main():
    firim, secim =argvcheck()
    shirtimply(firim, secim)

def shirtimply(inp, out):
    try:
        imfile = img.open(inp)
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirt = img.open('shirt.png', mode= 'r')
    size = shirt.size
    muppet = ImageOps.fit(imfile, size)

    muppet.paste(shirt,shirt)
    muppet.save(out)


def argvcheck():

    if len(sys.argv) == 3:
        validext = ['jpg', 'jpeg', 'png']

        firim = sys.argv[1].split('.')
        secim = sys.argv[2].split('.')
        if firim[1] not in validext:
            sys.exit('Invalid input')
        elif secim[1]  not in validext:
            sys.exit('Invalid output')
        elif firim[1] != secim[1]:
            sys.exit('Input and output have different extensions')
        else:
            return sys.argv[1], sys.argv[2]

    elif len(sys.argv) <3:
        sys.exit('Too few commaand-line argumants')

    else:
        sys.exit('Too many command-line argumants ')


if __name__ == "__main__":
    main()