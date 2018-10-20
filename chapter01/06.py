def ngram(seq, n):
    '''
    >>> ngram(['0123'], 1)
    ['0', '1', '2', '3']
    >>> ngram(['0123'], 2)
    ['01', '12', '23']
    '''
    text = ''.join(seq)
    tn = len(text)
    r = []
    for i in range(tn - n + 1):
        r.append(text[i : i + n])
    return r

def bigram(seq):
    return ngram(seq, 2)

def main():
    s = "paraparaparadise"
    t = "paragraph"
    X = set(bigram(s))
    Y = set(bigram(t))
    j = X | Y
    m = X & Y
    d = X - Y
    print(X)
    print(Y)
    print(j)
    print(m)
    print(d)
    print("se" in X)

main()
