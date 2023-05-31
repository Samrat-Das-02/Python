#Prime number generator 
r=int(input("Enter range for prime numbers : "))
for i in range(2,r):
    flag=0
    for j in range(2,i):
        if(i%j==0):
            flag=1
            break
    if(flag==0):
        print(i)