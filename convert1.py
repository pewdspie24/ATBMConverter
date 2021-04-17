import math
import base64

def splitWord(s):
    return [char for char in s]
excp = ['None','None','None','None','None','None']

def Decimal(decNum): 
    try:
        result =[]
        decNum = int(decNum)
        if decNum>127: 
            asc = bas = 'None'   
        else: 
            asc = chr(decNum)
            message_bytes = asc.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            bas = base64_bytes.decode('ascii')
        result.append(asc)
        result.append(str(decNum))
        result.append(bin(decNum)[2:])
        result.append(hex(decNum)[2:])
        result.append(oct(decNum)[2:])
        result.append(bas)
        return result
    except:
        return 'Error'


def splitWord(s):
    return [char for char in s]

def Ascii(asciiNum):
    try:
        result =[]
        d = []
        b = []
        h = []
        o = []
        b64 = []
        asc = splitWord(asciiNum)
        for i in asc:
            d.append(ord(i))
            b.append(bin(ord(i))[2:])
            h.append(hex(ord(i))[2:])
            o.append(oct(ord(i))[2:])
        result.append(asciiNum)
        result.append(' '.join(str(e) for e in d))
        result.append(' '.join(str(e) for e in b))
        result.append(' '.join(str(e) for e in h))
        result.append(' '.join(str(e) for e in o))
        message_bytes = asciiNum.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        result.append(base64_message)
        return result
    except:
        return 'Error'

def Binary(binNum):
    try:
        decNum = int(binNum,2)
        return Decimal(decNum)
    except:
        return 'Error'

def Heximal(hexNum):
    try:
        decNum = int(hexNum,16)
        return Decimal(decNum)
    except:
        return 'Error'

def Octimal(octNum):
    try:
        decNum = int(octNum,8)
        return Decimal(decNum)
    except:
        return 'Error'

def Base64(basNum):
    try:
        ascNum = base64.b64decode(basNum).decode('ascii')
        return Ascii(ascNum)
    except:
        return 'Error'

if __name__ == '__main__':
    # print(Ascii('ab'))
    print(Decimal(273))
    # print(Binary('100010001'))
    # print(Heximal('111'))
    # print(Octimal('421'))
    print(Base64('vlxx'))