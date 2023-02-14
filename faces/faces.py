def main():
    word = input('write something includes face: ')
    print (convert(word))

def convert(word):
    return word.replace(':(', '🙁').replace(':)', '🙂')


main()