import math

def encode(text, shift):
    shift = int(shift)
    enc = ""
    for c in text:
        if c.isalpha():
            c_uni = ord(c)
            c_idx = c_uni - ord('a') if c.islower() else c_uni - ord('A')
            new_idx = (c_idx + shift) % 26
            new_uni = new_idx + ord('a') if c.islower() else new_idx + ord('A')
            new_char = chr(new_uni)
            enc += new_char
        else:
            return "Error"
    return enc

def decode(text, shift):
    enc = ''
    shift = int(shift)
    for c in text:
        if c.isalpha():
            c_uni = ord(c)
            c_idx = c_uni - ord('a') if c.islower() else c_uni - ord('A')
            new_idx = (c_idx - shift) % 26
            new_uni = new_idx + ord('a') if c.islower() else new_idx + ord('A')
            new_char = chr(new_uni)
            enc += new_char
        else:
            return "Error"
    return enc

if __name__ == '__main__':
    print(decode("aAa", "3"))
    print(encode("aaa", "3"))