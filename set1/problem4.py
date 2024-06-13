from binascii import hexlify, unhexlify
from problem2 import hexor
from problem3 import hexcaesercipher, bitwisexor
from otherfunctions import asciiratio
from pathlib import Path

def hexfilecaesercheck(filepath):
    txtfolder = Path("C:/Users/Liter/OneDrive/Documents/cryptopals/pythonver/set1")
    candidateratio = 0
    with open (txtfolder / filepath ) as lines:
        for line in lines:
            newstring = hexcaesercipher(line.strip())
            if len(newstring.decode('utf-8', errors='ignore')) < 10:    #This should probably be in a previous function, specifically disincludes strings with lower lengths since they're more likely to have higher ratios
                continue
            if (asciiratio(newstring.decode('utf-8', errors='ignore')) > candidateratio):
                candidateratio = asciiratio(newstring.decode('utf-8', errors='ignore'))
                candidatestring = newstring
                
    lines.close()
    return(candidatestring)
            
            

#print(hexfilecaesercheck('4.txt').decode('utf-8',errors='ignore'))