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

def utest():
    assert(ngram(["114"], 1) == ["1","1","4"])
    assert(ngram(["1","1","4"], 2) == ["11","14"])
    assert(ngram(["1","1","4"], 3) == ["114"])
    assert(ngram(["1","1","4"], 4) == [])
    

def main():
    s = "I am an NLPer"
    words = s.split()
    print(ngram(words, 1))
    print(ngram(words, 2))

utest()
main()
