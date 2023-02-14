import sys

def main():
    check_CLargs()

def check_CLargs():
    arg = len(sys.argv)
    if arg == 1:
        sys.exit('Too few command-line arguments')
    elif arg == 2:
        if '.py' in sys.argv[1]:
            try:
                with open(f'{sys.argv[1]}','r') as code:
                    linecount = 0
                    for line in code:
                        if line.isspace():
                            continue
                        elif line.lstrip().startswith('#') :
                            continue
                        else:
                            linecount += 1
                    print (linecount)
            except FileNotFoundError:
                sys.exit('File does not exist')

        else:
            sys.exit('Not a Python file')
    else:
        sys.exit('Too many command-line arguments')


if __name__ == '__main__':
    main()