## encryption code

def caesar_encryption():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    final = ''
    myinput = "we need help asap"
    key = 343
    myinput = myinput.lower()
    for x in myinput:
        if (x in alpha):
            pos = alpha.find(x)
            pos = (pos + key) % 26
            final += (alpha[pos])
        else:
            final += final[:0]
    return final.upper()

#---------------------------------------------------------------#
def railfence_encryption():
    msg = "thanos is coming"
    rails = 2
    msg = msg.replace(" ", "")

    # creating an empty matrix
    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('')
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1

    encryp_text = ""
    for i in range(rails):
        for j in range(len(msg)):
            encryp_text += railMatrix[i][j]
    return  encryp_text.upper()

#---------------------------------------------------------------#
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vigenere_encryption():
    myMessage = "thanos has purple skin"
    myKey = 'AVENGERS'
    translated = encryptMessage(myKey, myMessage).upper()
    return translated

def encryptMessage(key, message):
    return translateMessage(key, message)

def translateMessage(key, message):
    translated = []  # stores the encrypted/decrypted message string
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num += LETTERS.find(key[keyIndex])
            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            keyIndex += 1

            if keyIndex == len(key):
                keyIndex =0
        else:
            translated +=translated[:0]
    return ''.join(translated)

vigenere_encryption()