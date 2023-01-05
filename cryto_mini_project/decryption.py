import re

## decryption code
def caesar_decryption():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    final = ''
    myinput = "WAIIXIJJSVXWEVIFIXXIVXLERWAIIXASVHW"
    key = 4
    myinput = myinput.lower()
    for x in myinput:
        if (x in alpha):
            pos = alpha.find(x)
            pos = (pos - key) % 26
            final += (alpha[pos])
        else:
            final += final[:0]
    return final.lower()

#---------------------------------------------------------------#
def railfence_decryption():
    msg = "IOEOTREHUADLVYUHETOSN"
    rails = 2
    msg = msg.replace(" ", "")

    railMatrix = []
    for i in range(rails):
        railMatrix.append([])
    for row in range(rails):
        for column in range(len(msg)):
            railMatrix[row].append('.')
    row = 0
    check = 0
    for i in range(len(msg)):
        if check == 0:
            railMatrix[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
                # inner if
        elif check == 1:
            row -= 1
            railMatrix[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1

    ordr = 0
    for i in range(rails):
        for j in range(len(msg)):
            temp = railMatrix[i][j]
            if re.search("\\.", temp):
                # skipping '.'
                continue
            else:
                railMatrix[i][j] = msg[ordr]
                ordr += 1
    check = 0
    row = 0
    decryp_text = ""
    for i in range(len(msg)):
        if check == 0:
            decryp_text += railMatrix[row][i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
            # inner if
        elif check == 1:
            row -= 1
            decryp_text += railMatrix[row][i]
            if row == 0:
                check = 0
                row = 1

    decryp_text = re.sub(r"\.", "", decryp_text)
    return decryp_text.lower()

#---------------------------------------------------------------#
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vigenere_decryption():
    myMessage = "NCPTTWJOLSESDFYPVXJOHRCCRHIVCERVS"
    myKey = 'COUPLE'
    translated = decryptMessage(myKey, myMessage).lower()
    return translated

def decryptMessage(key, message):
    return translateMessage(key, message)

def translateMessage(key, message):
    translated = []  # stores the encrypted/decrypted message string
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[keyIndex])
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
