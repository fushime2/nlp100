s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = s.split()
for c in [",", "."]:
    words = list(map(lambda w : w.replace(c, ""), words))

lens = list(map(len, words))
print(lens)
