s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = s.split()
for c in [",", "."]:
    words = list(map(lambda s : s.replace(c, ""), words))

l = []
for i, w in enumerate(words):
    if i == 0 or 4 <= i <= 8 or i == 14 or i == 15 or i == 18:
        l.append(w[:1])
    else:
        l.append(w[:2])

d = {w: s.find(w) for w in l}
print(d)
