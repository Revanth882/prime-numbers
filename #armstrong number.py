#armstrong number
num=int(input('enter number='))
temp=num
sum=0
l=len(str(num))
while num!=0:
    r=num%10
    sum+=r**l
    num//=10
if sum==temp:
    print('armstrong number')
else:
    print('not armstrong')