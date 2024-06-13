




def hexor(x1, x2):
    x11 = int(x1, 16)
    x22 = int(x2, 16)
    xord = x11^x22
    return hex(xord)
#another proof, ignore
#s = "1c0111001f010100061a024b53535009181c"
#key = "686974207468652062756c6c277320657965"
#
#xordstring = hexor(s, key)
#print(xordstring)