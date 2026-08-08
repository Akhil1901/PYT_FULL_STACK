""""🟢 Basic
Print numbers from 1 to 10.
Print numbers from 10 to 1.
Print numbers from 1 to n.
Print all even numbers from 1 to n.
Print all odd numbers from 1 to n.
Print multiples of 5 up to n.
Print numbers divisible by both 3 and 5.
Print squares of numbers from 1 to n.
Print cubes of numbers from 1 to n.
Print the multiplication table of a given number."""

"""for i in range(1,11):
    print(i)
"""
"""for i in range(10,0,-1):
    print(i)"""
"""n=int(input("enter an number : "))
for i in range(1,n+1):
    print(i)"""
"""n=int(input("enter a numbers : "))
for i in range(1,n+1):
    if(i%2==0):
        print(i)"""
"""n=int(input("enter an number: "))
for i in range(1,n+1):
    if(i%2!=0):
        print(i)"""
"""n=int(input("enter an number : "))
for i in range(1,n+1):
    if(i%5==0):
        print(i)"""
"""num=int(input("enter an number : "))
for i in range(1,num+1):
    if(i%3==0 and i%5==0):
        print(i)
else:
    print("number not found that divisible by both 3 and 5")"""
"""num=int(input("enter an number: "))
for i in range(1,num+1):
    print(i,":",i*i)"""
"""num=int(input("enter an number : "))
for i in range(1,num+1):
    print(i,":", i**3)"""
"""num=int(input("enter an number : "))
for i in range(1,num+1):
    print(num,"*",i,"=",i*num)"""
"""🟡 Sum and Product
Find the sum from 1 to n.
Find the sum of even numbers from 1 to n.
Find the sum of odd numbers from 1 to n.
Find the sum of numbers divisible by 3.
Find the sum of squares from 1 to n.
Find the factorial of a number.
Find the product of even numbers from 1 to n."""

"""num=int(input("enter an number : "))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)"""

"""num = int(input("enter an number: "))
sum=0
for i in range(1,num+1):
    if(i%2==0):
        sum=sum+i
print(sum)"""

"""num=int(input("enter an number: "))
sum=0
for i in range(1,num+1):
    if(i%2!=0):
        sum=sum+i
print(sum)"""

"""num=int(input("enter an number: "))
sum=0
for i in range(1,num+1):
    square=i*i
    sum=sum+square
print(sum)"""
"""num=int(input("enter an number: "))
fact=1
for i in range(1,num+1):
    if(i==0):
        fact=1
        print(i)
    elif(i>0):
        fact=fact*i
print(fact)"""

"""num=int(input("enter an number : "))
product=1
for i in range(1,num+1):
    if(i%2==0):
        product=product*i
print(product)"""
rows=6
for i in range(1,row+1):
    for 