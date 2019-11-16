Rounds = int(input())
for i in range(Rounds):
    text = input().upper()
    numOfDoc = int(input())
    docDict = {}
    for j in range(numOfDoc):
        doc = input().upper()
        temp = doc.split(" ")
        encode = temp[0] 
        decode = temp[1]
        for index, char in enumerate(encode):
            if((char >= 'A' and char <="Z") and not(char in docDict.keys())):
                docDict[char] = decode[index]
            else:
                continue
    ans = ""
    punc = '''' " , . : ; ? !'''.split(" ")
    punc.append(" ")
    for t in text:
        if(t >= 'A' and t <= 'Z'):
            if(t in docDict.keys()):
                ans+=docDict[t]
            else :
                ans = "CANNOT DECODE"
                break
        elif(t in punc):
            ans+=t
        else:
            ans = "CANNOT DECODE"
            break
    print(i+1,ans)