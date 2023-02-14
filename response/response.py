from validator_collection import validators

def main():

    mail = input('please enter your email: ')

    if mail_check(mail):
        print('Valid')
    else:
        print('Invalid')



def mail_check(mail):

    try:
        result = validators.email(mail, allow_empty = False)
    except:
        result  = False

    return result



if __name__ == '__main__':
    main()
