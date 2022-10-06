def SpiralPrint(a):
    n1=len(a)
    n2=len(a[0])
    
    i1=0
    i2=0

    d="->" # Direction
    l=0 #Loop Number

    lst=[] #Output List

    #Looping the input for each element
    for i in range(n2*n1):
        lst.append(a[i1][i2]) #Adding the Number to the Output List

        if i2<n2-1-l and d=="->": #Right Direction
            i2+=1
            if i2==n2-1-l:
                d="v"
        elif i1<n1-1-l and d=="v": #Down Direction
            i1+=1
            if i1==n1-1-l:
                d="<-"
        elif i2>0+l and d=="<-": #Left Direction
            i2-=1
            if i2==0+l:
                d="^"
        elif i1>0+l and d=="^": #Up Direction
            i1-=1
            if i1==1+l:
                d="->"
                l+=1

    return lst


#Test Case 1
a=[ [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]

print(SpiralPrint(a))


#Test Case 2
a=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

print(SpiralPrint(a))

