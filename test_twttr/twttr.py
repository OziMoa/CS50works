#twitter to twttr
def main():
    snt = input('input your sentence: ')
    out = shorten(snt)
    return out



def shorten(word):
        out = []
        for o in word:
            if o.lower() in ['a','e','i','o','u']:
                continue
            else:
                out.append(o)
        newword = ''.join(out)
        return newword



if __name__ == "__main__":
    main()