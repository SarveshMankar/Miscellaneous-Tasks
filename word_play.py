# Sam Tech Op :)
def sortGrid(a):
    n = []
    m = []
    for i in a.split("\n"):
        n.append(i)
        c = []
        for j in i.split("   "):
            c.append(j)
        if c != [""]:
            m.append(c)
    return m


def wordPlay(word):
    temp = []
    words = []
    ranges = []

    i = word[0]
    for x in range(0, len(m)):
        for y in range(0, len(m[x])):
            if i == m[y][x]:
                temp.append([x, y])

    words = []
    ranges = []

    for i in temp:
        i1 = i[0]
        i2 = i[1]
        w1 = ""
        w2 = ""
        w3 = ""
        w4 = ""
        w5 = ""
        w6 = ""
        w7 = ""
        w8 = ""
        r1 = []
        r2 = []
        r3 = []
        r4 = []
        r5 = []
        r6 = []
        r7 = []
        r8 = []
        for j in range(0, len(word)):
            try:
                w1 = w1 + m[i2 + j][i1]
                r1.append((i1, i2 + j))
            except:
                pass
            try:
                w2 = w2 + m[i2][i1 + j]
                r2.append((i1 + j, i2))
            except:
                pass
            try:
                w3 = w3 + m[i2 + j][i1 + j]
                r3.append((i1 + j, i2 + j))
            except:
                pass
            try:
                if i2 - j > 0 and i1 - j > 0:
                    w4 = w4 + m[i2 - j][i1 - j]
                    r4.append((i1 - j, i2 - j))
            except:
                pass
            try:
                w5 = w5 + m[i2 - j][i1]
                r5.append((i1, i2 - j))
            except:
                pass
            try:
                w6 = w6 + m[i2][i1 - j]
                r6.append((i1 - j, i2))
            except:
                pass
            try:
                w7 = w7 + m[i2 + j][i1 - j]
                r7.append((i1 - j, i2 + j))
            except:
                pass
            try:
                w8 = w8 + m[i2 - j][i1 + j]
                r8.append((i1 + j, i2 - j))
            except:
                pass

        words.append(w1)
        ranges.append(r1)
        words.append(w2)
        ranges.append(r2)
        words.append(w3)
        ranges.append(r3)
        words.append(w4)
        ranges.append(r4)
        words.append(w5)
        ranges.append(r5)
        words.append(w6)
        ranges.append(r6)
        words.append(w7)
        ranges.append(r7)
        words.append(w8)
        ranges.append(r8)

    try:
        n = words.index(word)
        print("Main Answer of ", words[n], "=", ranges[n])
    except:
        print("The Word ", word, " Doesn't Exsist!")


a = """
U   N   D   E   R   S   T   A   T   E   M   E   N   T   S   J
I   J   A   Q   Z   O   A   D   R   H   Z   X   Y   I   F   L
U   L   T   X   H   K   U   W   V   X   W   N   L   N   H   E
R   U   B   A   A   N   A   O   Y   J   R   M   Y   F   I   J
Q   E   Y   T   E   R   E   S   A   S   H   H   P   L   B   T
U   F   K   P   V   I   F   I   S   L   K   F   H   E   V   E
E   O   G   E   F   M   U   K   A   G   I   N   U   C   E   A
O   Y   E   J   T   K   Q   S   L   M   I   C   M   T   H   C
X   M   W   S   H   N   R   S   T   R   J   O   C   I   D   H
I   L   P   B   J   E   W   J   C   B   Z   D   I   O   T   I
V   O   O   F   L   U   Y   P   E   E   B   F   Q   N   A   N
J   S   G   I   C   V   L   I   L   A   Y   X   Q   S   G   G
H   H   U   C   L   C   R   Y   L   N   Z   A   N   I   A   S
L   A   D   E   D   T   M   S   A   E   D   B   O   Q   G   N
W   J   J   M   O   H   S   A   R   Y   Q   X   A   P   V   J
T   G   U   Y   Q   H   S   P   M   L   W   M   P   M   W   D
"""

m = sortGrid(a)

# Case 1
word = "TJDCCUW"
wordPlay(word)

# Case 2
word = "AXARFKLR"
wordPlay(word)

# Case 3
word = "MQELIYE"
wordPlay(word)

# Case 4
word = "ALKSFP"
wordPlay(word)
