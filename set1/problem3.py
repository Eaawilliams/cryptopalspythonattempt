from binascii import hexlify, unhexlify
from problem2 import hexor
from otherfunctions import asciiratio

def bitwisexor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))



def hexcaesercipher(A):
    
    #the problem mentions that the plaintext has been xor'd against one character, but really means one character repeated for the whole length
    #would help to convert to int and xor in the function itself
    highestratio = 0
    for i in range(256):
        key = i.to_bytes(1, 'big')  #bytes() doesn't work, for some reason does not iterate, found this alternative
        longkey = len(A)*key        #matches length with ciphertext
        bxor = bitwisexor(unhexlify(A), longkey)    #produces the bitwise xor and prints it
        if (asciiratio(bxor.decode('utf-8', errors='ignore')) > highestratio):
            highestratio = asciiratio(bxor.decode('utf-8', errors = 'ignore'))
            newbxor = bxor
        

        #this part of the function checks if it is a sentence
    return(newbxor)



#s = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#print(hexcaesercipher(s).decode('utf-8',errors='ignore'))