# ELLA MARIE A. MALLARI
# BSCPE 1-4

# PROBLEM 3 - THE VIGENÉRE CIPHER

#define to generate the key
def generateKeyword(textMessage, key):
    key = list(key)
    if len(textMessage) == len(key):
        return key
    else:
        for i in range(len(textMessage) - len(key)):
            key.append(key[i % len(key)])
        return("".join(key))  
# define the cipher text
def cipherText(textMessage, key):
    cipher_text = []
    for i in range(len(textMessage)):
        x = (ord(textMessage[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x)) 
    return("" .join(cipher_text))


# ask the user to type any message, keyword in all capital letters with no spaces
# added some colors