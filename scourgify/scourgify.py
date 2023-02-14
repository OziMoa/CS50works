import csv, sys

def main ():
    foldname, writename = phase()
    informations = csvread(foldname)
    csvwriter(informations, writename)

def csvread(filename):
    nlist = []
    with open(filename, 'r') as f:
        for line in csv.DictReader(f):
            sap = line['name'].split(', ')
            nlist.append({'first': sap[1], 'last': sap[0], 'house': line['house'] })
    return nlist

def csvwriter(data, writename ='after.csv' ):

    with open(writename, 'w') as after:
        writer = csv.DictWriter(after, fieldnames =['first', 'last', 'house'])
        writer.writerow({'first':'first', 'last': 'last', 'house':'house'})
        for row in data:
            writer.writerow({'first':row['first'], 'last': row['last'], 'house':row['house']})


def phase():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line argumant')

    elif len(sys.argv) > 3 :
        sys.exit('Too many command-line arguments')

    elif len(sys.argv) == 3 :
        try:
            vals = sys.argv[1].split('.')
            vals2 = sys.argv[2].split('.')
            if vals[1] == 'csv' and vals2[1] =='csv' :
                return sys.argv[1], sys.argv[2]
            else:
                sys.exit('Not a CSV file')
        except FileNotFoundError:
            sys.exit(f'Could not read {sys.argv[1]}')


if __name__== "__main__":
    main()