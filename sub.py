from string import ascii_letters

def encode(text, cipher_alpha):
    try:
        trans = str.maketrans(ascii_letters, cipher_alpha)
        res = text.translate(trans)
        return res
    except ValueError:
        return 'Error'

def decode(text, cipher_alpha):
    try:
        trans = str.maketrans(cipher_alpha, ascii_letters)
        return text.translate(trans)
    except ValueError:
        return 'Error'

if __name__ == '__main__':
    print(encode("abc", 'nzghqkcdmyfoialxevtswrupjb'+'NZGHQKCDMYFOIALXEVTSWRUPJB'))