import math
S = int(input())
for i in range(S):
    N = input()
    temp = N.split(" ")
    nthround = temp[0]
    num = int(temp[1])
    lines =math.ceil(num/20)-1
    templist = set()
    for n in temp[2:(num+2)]:
        if(int(n) > 0):
            templist.add(int(n))
    setinput = list(templist)
    if(len(setinput)<3):
        print(i+1,'na')
    else:
        for k in range(3):
            minn = 1001
            for j in setinput:
                if(j < minn):
                    minn = j
            setinput.remove(minn)
        print(i+1, minn)
            
    