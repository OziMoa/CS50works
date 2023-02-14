import requests as req
import sys


if len(sys.argv) <= 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number" )
    except IndexError:
        sys.exit("Missing command-line argument   " )

else:
    print ('too many input argument ')


try:
    r = req.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    jas = r.json()
    rate = jas["bpi"]["USD"]["rate"]
    rate = float(rate.replace(',',''))
    amount = n*rate
    print(f"${amount:,.4f}")

except req.RequestException:
    print ("Request problem ")

