from Crypto.Cipher import AES
from hashlib import md5
import binascii
import random

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encryption(text, key, mode):
    try:
        if mode == 'ECB':
            key = md5(key.encode('utf8')).hexdigest().encode('utf8')
            text = pad(text).encode()
            cipher = AES.new(key, AES.MODE_ECB)
            msg = cipher.encrypt(text)
            return binascii.hexlify(msg).decode('ascii')
        else:
            iv = key[0:16]
            iv = iv.encode()
            key = key.encode()
            text = text.encode()
            cipher = AES.new(key, AES.MODE_CFB, iv = iv)
            res = cipher.encrypt(text)
            # print(res)
            return binascii.hexlify(res).decode('ascii')
    except ValueError:
        return 'Error'

def decryption(text, key, mode):
    try:
        if mode == 'ECB':
            text = binascii.unhexlify(text.encode())
            key = md5(key.encode('utf8')).hexdigest().encode('utf8')
            decipher = AES.new(key, AES.MODE_ECB)
            msg = decipher.decrypt(text)
            return unpad(msg).decode()
        else:
            text = binascii.unhexlify(text.encode())
            iv = key[0:16]
            # print(text)
            key = key.encode()
            iv = iv.encode()
            decipher = AES.new(key, AES.MODE_CFB, iv = iv)
            return decipher.decrypt(text).decode()
    except ValueError:
        return 'Error'

if __name__=='__main__':
    a = encryption('abc', '1234567890123456acbetngh', 'ECB')
    print(a)
    print(decryption(a, '1234567890123456acbetngh', 'ECB'))