__name__ = 'RuleLogic'

def decide(prob):
    out = 0
    if prob == 1:
        out = 1
    elif (prob < 1) and (prob > .25):
        out = 0
    else:
        out = -1
    return out
