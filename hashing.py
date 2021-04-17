import hashlib
import zlib

def md5(text):
    text = text.encode()
    return hashlib.md5(text).hexdigest()
def rip(text):
    text = text.encode()
    return hashlib.new('ripemd160',text).hexdigest()
def sha_1(text):
    text = text.encode()
    return hashlib.sha1(text).hexdigest()
def sha_256(text):
    text = text.encode()
    return hashlib.sha256(text).hexdigest()
def sha_512(text):
    text = text.encode()
    return hashlib.sha512(text).hexdigest()
def sha_3(text):
    text = text.encode()
    return hashlib.sha3_512(text).hexdigest()
def crc32(text):
    text = text.encode()
    return hex(zlib.crc32(text)& 0xffffffff)[2:]

if __name__ == '__main__':
    print(sha_3('GeeksforGeeks'))
    print(crc32('abc'))