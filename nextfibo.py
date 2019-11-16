def calculate(n):
    count = 0
    while True:
        if(n == 1):
            return count+1
        elif(n%2 == 0):
            n = n/2
            count+=1
        else:
            n = 3*n+1
            count+=1
        
D = int(input())
for i in range(D):
    n = int(input())
    count = calculate(n)
    print(i+1, n, count)
