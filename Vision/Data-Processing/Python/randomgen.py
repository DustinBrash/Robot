#Testing AI, written by Vincent Pugliese
#note to Vincent: use 4 space convention in code
import random, array

testset = []
i = 0

def randomtestgen():
    i = 0
    testset = []
    while i < 2: 
        x = random.randint(0, 480) #change 480 to pixel size
        i = i + 1
        testset.append(x)
    return testset



