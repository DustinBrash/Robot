__name__ = 'ProbGen'

def generate(inputs):
    output = 0.0
    count = 0
    for i in inputs:
        if i and count < 5:
            output = (4.0 - count) / 4.0
            break
        elif count >= 5:
            break
        count += 1
    return output            
