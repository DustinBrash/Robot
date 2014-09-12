import combinations
#a is n from number of elements
#b is r from number of elements
#c is n from number in state space
#d is r from number in state space
#probability is n(e)/n(s), weighted prob is k(n(e)/n(s)) where k is certainty
def wProb(a, b, c, d, k):
    a, b, c, d = float(a), float(b), float(c), float(d)
    e, s, k = float(combinations.nCr(a, b)), float(combinations.nCr(c, d)), float(k)
    return k*(e/s)

