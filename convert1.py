import math
import base64

def splitWord(s):
    return [char for char in s]
def splitNum(s):
    return s.split(' ')
excp = ['None','None','None','None','None','None']

def Decimal(decNumList): 
    try:
        if type(decNumList) is not list:
            decNumList = str(decNumList).split(" ")
        # print(type(decNumList))
        final = []
        resultA = []
        resultD = []
        resultB = []
        resultH = []
        resultO = []
        resultB64 = []
        for decNum in decNumList:
            result = []
            decNum = int(decNum)
            if decNum>127: 
                asc = bas = 'None'   
            else: 
                asc = chr(decNum)
            resultA.append(asc)
            resultD.append(str(decNum))
            resultB.append(bin(decNum)[2:])
            resultH.append(hex(decNum)[2:])
            resultO.append(oct(decNum)[2:])
        final.append(''.join(resultA))
        final.append(' '.join(resultD))
        final.append(' '.join(resultB))
        final.append(' '.join(resultH))
        final.append(' '.join(resultO))

        message_bytes = final[0].encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        bas = base64_bytes.decode('ascii')
        final.append(bas)

        return final
    except:
        return 'Error'

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

def Binary(num):
    try:
        listStr = splitNum(num)
        listNum = []
        for i in listStr:
            i = int(i,2)
            listNum.append(i)
        return Decimal(listNum)
    except:
        return 'Error'

def Heximal(num):
    try:
        listStr = splitNum(num)
        listNum = []
        for i in listStr:
           i= int(i,16)
           listNum.append(i)
        return Decimal(listNum)
    except:
        return 'Error'

def Octimal(num):
    try:
        listStr = splitNum(num)
        listNum = []
        for i in listStr:
            i = int(i,8)
            listNum.append(i)
        return Decimal(listNum)
    except:
        return 'Error'

def Base64(basNum):
    try:
        ascNum = base64.b64decode(basNum).decode('ascii')
        return Ascii(ascNum)
    except:
        return 'Error'

if __name__ == '__main__':
    # print(Ascii('quang tran yeu ninh ngoc'))
    # print(Decimal('113 117 97 110 103 32 116 114 97 110 32 121 101 117 32 110 105 110 104 32 110 103 111 99'))
    # print(Binary('01110001 01110101 01100001 01101110 01100111 00100000 01110100 01110010 01100001 01101110 00100000 01111001 01100101 01110101 00100000 01101110 01101001 01101110 01101000 00100000 01101110 01100111 01101111 01100011'))
    # print(Heximal('71 75 61 6e 67 20 74 72 61 6e 20 79 65 75 20 6e 69 6e 68 20 6e 67 6f 63'))
    # print(Octimal('161 165 141 156 147 040 164 162 141 156 040 171 145 165 040 156 151 156 150 040 156 147 157 143'))
    print(Base64('cXVhbmcgdHJhbiB5ZXUgbmluaCBuZ29j'))