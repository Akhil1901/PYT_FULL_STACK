'''num=int(input("enter a number: "))
cube=(1//3)
print(cube)
root=num**(cube)
print(root)
if((root**3)==num):
    print("perfect cube")
else:
    print("not perfect cube")
'''
'''num=int(input("enter an number : "))
fact=1
i=1
while(i<=num):
    fact=fact*i
    i=i+1
print(fact)'''
'''num=int(input("enter an number: "))
i=1
count=0
while(i<=num):
    if(i>20):
        print(i)
        count=count+1
    i=i+1
print(count)'''
'''num=int(input("enter an number: "))
i=1
while(i<=num):
    if(i%5!=0):
        print(i)
    i=i+1'''
'''num=int(input("enter an number: "))
i=1
sum=0
while(i<=num):
    if(i%4==0):
        sum=sum+i
    i=i+1
print(sum)'''
'''num=int(input("enter an number : "))
i=1
sum=0
while(i<= num):
    if(num%i==0):
        sum=sum+i
    i=i+1
print(sum)'''
'''num=int(input("enter an number "))
i=1
while(i<=num):
    if(num%i==0):
        print(i)
    i=i+1'''
num=int(input("enter an number : "))
i=1
while(i<=num):
    j=1
    count=0
    while(j<=i):
        if(i%j==0):
            count=count+1
        j=j+1
    if(count==2):
        print(i)
    i=i+1
 

 