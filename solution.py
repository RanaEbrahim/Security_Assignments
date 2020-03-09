import sys

def shiftEncryption(input, output, key):
    o1 = open(input, "r")
    re = o1.read()
    p = ""
    for i in re:
        if i.isalpha() and i.isupper():
            i = chr(((ord(i) - ord('A') + key) % 26)+ord('A'))
            p+=i
        elif i.isalpha() and i.islower():
            i = chr(((ord(i) - ord('a') + key) % 26) + ord('a'))
            p+=i
        else:
            p+=i
        o2 = open(output, "w")
        o2.write(p)
        o2.close()

def shiftDecryption(input, output, key):
    o1 = open(input, "r")
    re = o1.read()
    p = ""
    for i in re:
        if i.isalpha() and i.isupper():
            i = chr(((ord(i) - ord('A') - key + 26) % 26)+ord('A'))
            p+=i
        elif i.isalpha() and i.islower():
            i = chr(((ord(i) - ord('a') - key + 26) % 26) + ord('a'))
            p+=i
        else:
            p+=i
        o2 = open(output, "w")
        o2.write(p)
        o2.close()

def affineEncryption(input, output, a, b):
    o1 = open(input, "r")
    re = o1.read()
    p = ""

    for i in re:
        if i.isalpha() and i.isupper():
            i = chr(((int(a) * (ord(i) - ord('A')) + int(b)) % 26) + ord('A'))
            p+=i
        elif i.isalpha() and i.islower():
            i = chr(((int(a) * (ord(i) - ord('a')) + int(b) % 26) + ord('a')))
            p+=i
        else:
            p+=i
        o2 = open(output, "w")
        o2.write(p)
        o2.close()

def affineDecryption(input, output, a, b):
    o1 = open(input, "r")
    re = o1.read()
    p = ""
    for i in range(0, 25):
        if (i * int(a)) % 26 == 1:
            a = i
            print(a)
            break
    for i in s:
        if i.isalpha() and i.isupper():
            i = chr((((int(a) * ((((ord(i) - ord('A')) - int(b)) + 26) % 26)) % 26) + ord('A')))
            p+=i
        elif i.isalpha() and i.islower():
            i = chr((((int(a) * ((((ord(i) - ord('a')) - int(b)) + 26) % 26)) % 26) + ord('a')))
            p+=i
        else:
            p+=i
        o2 = open(output, "w")
        o2.write(p)
        o2.close()

def vigenereEncryption(input, output, key):
    o1 = open(input, "r")
    re = o1.read()
    p = ""
    ps = ""
    k = len(key)
    for i in range (0, len(s)):
        ps += key[i%k]

    for i in range(0, len(s)):
        if p[i].isalpha() and p[i].isupper():
           xx  = chr(((ord(p[i]) + ord(ps[i]) - 2 * ord('A')) % 26)+ord('A'))
           p+=xx
        elif s[i].isalpha() and s[i].islower():
            xx= chr(((ord(p[i]) + ord(ps[i]) - 2 * ord('a')) % 26) + ord('a'))
            p+= xx
        else:
            p+=s[i]
        o2 = open(output, "w")
        o2.write(p)
        o2.close()

def vigenereDecryption(input, output, key):
    o1 = open(input, "r")
    re = o1.read()
    p = ""
    ps = ""
    k = len(key)
    for i in range (0, len(p)):
        ps += key[i%k]

    for i in range(0, len(p)):
        if p[i].isalpha() and p[i].isupper():
           xx  = chr(((ord(p[i]) - ord(ps[i]) - 2 * ord('A') + 78) % 26)+ord('A'))
           p+=xx
        elif p[i].isalpha() and p[i].islower():
            xx= chr(((ord(p[i]) - ord(ps[i]) - 2 * ord('a') + 78) % 26) + ord('a'))
            p+= xx
        else:
            p+=p[i]
        o2 = open(output, "w")
        o2.write(p)
        o2.close()

p = sys.argv[1]
p = p.lower()
if p[0] == 'a':
    xx = sys.argv[2]
    xx.lower()
    if xx[0] == 'e':
        affineEncryption(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    elif xx[0] == 'd':
        affineDecryption(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else: print("Check arguments")
elif p[0] == 's':
    xx = sys.argv[2]
    xx.lower()
    if xx[0] == 'e':
        shiftEncryption(sys.argv[3], sys.argv[4], sys.argv[5])
    elif xx[0] == 'd':
        shiftDecryption(sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Check arguments")
elif  p[0] == 'v':
    xx = sys.argv[2]
    xx.lower()
    if xx[0] == 'e':
        vigenereEncryption(sys.argv[3], sys.argv[4], sys.argv[5])
    elif xx[0] == 'd':
        vigenereDecryption(sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        print("Check arguments")


