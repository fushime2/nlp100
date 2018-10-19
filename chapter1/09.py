
def f(s):
    def myshuffle(s):
        from random import sample
        return "".join(sample(s, len(s)))

    if len(s) <= 4:
        return s
    return s[0] + myshuffle(s[1:-1]) + s[-1]

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(f(text))
