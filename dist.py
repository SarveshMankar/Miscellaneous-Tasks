def to_and_from(a, b, t):
    steps=a-b
    aa=(t-(t%steps))/(steps)
    if aa%2==0:
        return a-(t%(steps))
    else:
        return b+(t%(steps))


print(to_and_from(2, 4, 3)) #3
print(to_and_from(1, 10, 8)) #9
print(to_and_from(10, 4, 8)) #6
print(to_and_from(2, 4, 5)) #3
print(to_and_from(42, 150, 548)) #142

def to_and_from_1(a, b, t):
    st=1
    ini=1
    if a>b:
        lst=[i for i in range(b,a+1)][::-1]
    else:
        lst=[i for i in range(a,b+1)]

    pos=lst[0]
    while st!=t:
        if ini==len(lst)-1:
            ini=0
            lst=lst[::-1]
        st+=1
        ini+=1
        pos=lst[ini]

    return pos

def to_and_from_2(a, b, t):
    if a>b:
        lst=[i for i in range(b,a+1)][::-1]
    else:
        lst=[i for i in range(a,b+1)]

    pos=lst[0]
    steps=len(lst)-1
    a=(t-(t%steps))/(steps)
    if a%2==0:pos=lst[t%(steps)]
    else:
        lst=lst[::-1]
        pos=lst[t%(steps)]

    return pos