#armstrong numbers from 1 to 1000
for num in range(1,1000000):
    power=len(str(num))
    temp=num
    sum=0
    while num!=0:
        r=num%10
        sum+=r**power
        num//=10
    if sum==temp:
        print(temp,end=' ')