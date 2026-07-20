#prime number check
n=int(input("enter number="))
for i in range(2,n):
    if n%i==0:
        print("not prime")          # this program prints 0 and 1 also prime
        break
else:
    print("prime")        


#
n=int(input("enter number="))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1    
if count==0:
    print("prime")                   # this program prints 0 and 1 also prime
else:
    print('not prime')       

n=int(input('enter a number='))
for i in range(2,int(n**0.5)+1):     # here also same but program executes and finishes fast because we used square root
    if n%i==0:
        print('not a prime')
        break
else:
    print('prime')



num=int(input('enter a number='))   # the main thing is if it is a number like 97 the loop checks from 2 to 96 
if num<2:
    print('not a prime')                #but if we use square root then it  checks only n**0.5+1 times only
else:
    for i in range(2,num):
        if num%i==0:
            print('not a prime')
            break
    else:
        print('prime')