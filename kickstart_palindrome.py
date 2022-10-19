#https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b54d3b

ina=int(input())
for mi in range(ina):
    ma=input()
    q=int(ma.split()[1])
    maina=input()
    ans=0
    for i in range(q):
        mb=input()
        pa,pb=int(mb.split()[0]),int(mb.split()[1])
        a=maina[pa-1:pb]
        l=len(a)

        flag=1
        oddflag=0

        if l%2==0:
            lst=list(set(list(a)))
            for j in lst:
                if a.count(j)%2!=0:
                    flag=0 #Not Palindrome
                    break
        else:
            lst=list(set(list(a)))
            for j in lst:
                if a.count(j)%2!=0:
                    oddflag+=1
            
        if flag==1 and oddflag==0:
            #print("Palindrome")
            ans+=1
        elif oddflag<=1 and l%2!=0:
            #print("Palindrome")
            ans+=1
        else:
            #print("Not Palindrome")
            pass

    print(f"Case #{mi+1}: {ans}")

#I am getting TLE on this code. Can anyone help me to optimize this code?
