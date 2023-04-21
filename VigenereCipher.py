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
    
# define the cipher text to generate it and will add modulo 26 to complete the alphabet
# ask the user to type any message, keyword in all capital letters with no spaces
# added some colors