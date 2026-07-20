#prime numbers in given range
n=int(input('enter range='))
count=0
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
        count+=1
print(f"\ncount={count}")