#Testing AI, written by Vincent Pugliese
#note to Vincent: use 4 space convention in code
import random, array
import randomgen as rgen

def MonteCarlo():
    h = 0
    q = []
    while h <= 100:
        testset = rgen.randomtestgen()
        q.append(testset)
        h = h + 1
    #print 'TEST COMPLETE'
    #print q
    return q

MonteCarlo()

