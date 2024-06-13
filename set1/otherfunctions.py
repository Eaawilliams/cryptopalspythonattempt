# this only exists for me to make functions that I felt didn't exactly fit in the problems

def asciiratio(x):
    validchars = r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
    ratio = 0

    for element in x:
        if element in validchars:
            ratio += 1
        else:
            ratio += 0
    return ratio/(len(x)+0.0001)
            

