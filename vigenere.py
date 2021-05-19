alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encode(message, key):
    try:
        encrypted = ""
        key = key.lower()
        tmp = message
        message = message.lower()
        split_message = [
            message[i : i + len(key)] for i in range(0, len(message), len(key))
        ]
        count = 0
        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                if tmp[count].isupper():
                    encrypted += index_to_letter[number].upper()
                    # print(tmp[count])
                else:
                    encrypted += index_to_letter[number]
                i += 1
                count += 1

        return encrypted
    except KeyError:
        return 'Error'


def decode(cipher, key):
    try:
        decrypted = ""
        tmp = cipher
        key = key.lower()
        cipher = cipher.lower()
        split_encrypted = [
            cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
        ]
        count = 0
        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                if tmp[count].isupper():
                    decrypted += index_to_letter[number].upper()
                else:
                    decrypted += index_to_letter[number]
                i += 1
                count+=1

        return decrypted
    except KeyError:
        return 'Error'

if __name__ == "__main__":
    string = "Quang Ngoc"
    key = "e c"
    cipher_text = encode(string,key)
    print(cipher_text)