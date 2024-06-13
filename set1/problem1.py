from base64 import b64decode, b64encode

# hex to base 64
def b642hex(x):
    b64 = b64encode(bytes.fromhex(x)).decode()
    return b64
    
# base 64 to hex
def hex2base64(y):
    hexa = b64decode(y.encode()).hex()
    return hexa

# This exists as a proof that it works, I have commented it out as I am lazy
#s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
#print(s)
#
#newthing = str(b642hex(s))
#print(newthing)
#
#oldthing = hex2base64(newthing)
#print(oldthing)