#Micah Russell Text Encrypter

#method:
#take plain text string and encryption string ('key')
#convert plain text to ascii
#convert key to ascii
#repeatedly apply key to plain text ascii by summing ascii values mod 127


import string

alpha = string.printable

##for char in alpha:
##    print char



def encrypt(plain, key):
    #parse plain and key into lists of ascii ords
    plain_ords = []
    for char in plain:
        plain_ords.append(alpha.find(char))
    key_ords = []
    for char in key:
        key_ords.append(alpha.find(char))
    
    #translate plain_ords by key_ords
    enc_chars = []
    for i in range(len(plain_ords)):
        k_n = i % len(key)
        enc_chars.append(alpha[((plain_ords[i]+key_ords[k_n])%100)])
    
    #combine a return chars
    return "".join(enc_chars)
        
        
        
def decrypt(enc, key):
    #parse enc and key into list of ascii ords
    enc_ords = []
    for char in enc:
        enc_ords.append(alpha.find(char))
    key_ords = []
    for char in key:
        key_ords.append(alpha.find(char))
        
    #translate enc_ords by -key_ords
    plain_ords = []
    for i in range(len(enc)):
        k_n = i % len(key)
        plain_ords.append(alpha[(enc_ords[i]-key_ords[k_n])%100])
    
    #combine a return chars
    return "".join(plain_ords)
        
        
        
        
def main():
    print("Encrypt or Decrypt?")
    choice = raw_input("").lower()

    if choice in ["encrypt","e"]:
        print "Encrypted text: \n" + encrypt(raw_input("Plain text:\n"),raw_input("Key:\n"))
    elif choice in ["decrypt","d"]:
        print "Plain text: \n" + decrypt(raw_input("Encrypted text:\n"),raw_input("Key:\n"))
    else:
        print("Please enter a real choice.")
    
    
        
main()







