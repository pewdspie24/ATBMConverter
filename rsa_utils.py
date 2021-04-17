from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def genKey(keysize):
    key2 = RSA.generate(keysize)
    pubKey = key2.publickey()
    pub = pubKey.export_key().decode('ascii')
    pri = key2.export_key().decode('ascii')
    res = []
    res.append(pub)
    res.append(pri)
    return res

def encryption(text, key):
    try:
        text = text.encode()
        # key = "-----BEGIN PUBLIC KEY-----\n"+key+"\n-----END PUBLIC KEY-----"
        key = key.encode()
        key = RSA.import_key(key)
        encryptor = PKCS1_OAEP.new(key)
        encrypted = encryptor.encrypt(text)
        return binascii.hexlify(encrypted).decode('ascii')
    except ValueError:
        return 'Error'

def decryption(text, key):
    try:
        text = binascii.unhexlify(text.encode())
        # print(text)
        key = key.encode()
        key = RSA.import_key(key)
        decryptor = PKCS1_OAEP.new(key)
        decrypted = decryptor.decrypt(text)
        return decrypted.decode('ascii')
    except ValueError:
        return 'Error'

if __name__ == '__main__':
    a = genKey(1024)
    b = encryption('quang',a[0])
    # print(b)
    print(decryption(b, a[1]))