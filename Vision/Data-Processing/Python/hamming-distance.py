#hamming distance module
#uses 4 space notation
import array

actual = open('actual.bin', 'r')
theoretical = open('theoretical.bin', 'r') 
def hamming(actual, theoretical):
    x, y = actual.split(''), theoretical.split('')
    if x is y:
        return 0
    else:
        

actual.close()
theoretical.close()
