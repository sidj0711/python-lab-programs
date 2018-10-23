n=int(input())
for i in range(1,int(n)):
    for j in range(2,(i+1)):
        if i%j==0:
            if i==j:
                print(i)
            break