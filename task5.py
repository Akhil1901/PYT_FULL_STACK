#plaindrome given number
"""num=int(input("enter an number: "))
reverse=0
original=num
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if(reverse==original):
    print("plaindrome")
else:
    print("not palindrome")"""
"""2. Write a Python program to repeatedly find the sum of the digits of a given number using a while loop until a single-digit number is obtained.
Input: 4589
Output: 8

Explanation:
4589 → 4 + 5 + 8 + 9 = 26
26 → 2 + 6 = 8"""
""""num=int(input("enter an number: "))
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)
sum2=0
if(sum>9):
    num=sum
    while(num>0):
        digit=num%10
        sum2=sum2+digit
        num=num//10
print(sum2)"""
"""num=int(input("enter an number: "))
temp=num
bkp=num
count=0
while(temp>0):
    temp=temp//10
    count=count+1
print(count)
sum=0
while(num>0):
    digit=num%10
    cube=digit**count
    sum=sum+cube
    num=num//10
if(bkp==sum):
    print("armstrong number")
else:
    print("not armstrong number")"""
"""num=int(input("enter an number : "))
a=0
b=1
print(a)
print(b)
i=1
while(i<=(num-2)):
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1"""
num=int(input("enter an number"))
square=0
square=num*num
sum=0
while(square>0):
    digit=square%10
    sum=sum+digit
    square=square//10
if(sum==num):
    print("neon number")
else:
    print("not an number")