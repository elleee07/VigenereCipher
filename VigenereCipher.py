# ELLA MARIE A. MALLARI
# BSCPE 1-4

# PROBLEM 3 - THE VIGENÉRE CIPHER

#ask user to input their name
name = input(Please enter your name: )

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

if __name__ == "__main__":
# ask the user to type any message, keyword in all capital letters with no spaces
    print("=" * 80) 
    print("Kindly type any message in capital letters and no spaces: ")
    textMessage = input() 
    print("=" * 80) 
    print("Kindly type your chosen keyword also in capital letters: ")
    keyword = input() 
# added some colors
    cyan = '\033[36m' 
    reset = '\033[0m'
#print output
    key = generateKeyword(textMessage, keyword) 
    cipher_text = cipherText(textMessage, key)
    print("=" * 80) 
    print(cyan + "CIPHERTEXT: " + reset + cipher_text)