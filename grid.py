from pprint import pprint


def grid(s):
    r1 = []
    c1 = []

    for i in s:
        r1.append(i.split(" ")[0])
        c1.append(i.split(" ")[1])

    r = [int(i) for i in r1]
    c = [int(i) for i in c1]

    mr = int(max(r))
    mc = int(max(c))

    # print(mr,mc)

    grid = []
    for i in range(mr):
        l = []
        for j in range(mc):
            l.append(0)
        grid.append(l)

    for i in range(len(r)):
        for j in range(int(r[i])):
            for k in range(int(c[i])):
                grid[j][k] = grid[j][k] + 1
    return grid[::-1]


# Case 1
print(grid(["2 3", "3 7", "4 1", "5 2", "6 1"]))

# Case 2
pprint(grid(["2 3", "3 7", "4 1"]))

# Case 3
print(grid(["18 29", "32 17", "34 9", "38 15", "36 22", "7 14", "5 100"]))
