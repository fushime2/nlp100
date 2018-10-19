import string

def cipher(s):
    def crypt(c):
        return chr(219 - ord(c))

    t = ""
    for c in s:
        if c.islower():
            t += crypt(c)
        else:
            t += c
    return t

s = string.ascii_letters
crypted = cipher(s)
decrypted = cipher(crypted)
print(crypted)
print(decrypted)
assert(decrypted == s)
