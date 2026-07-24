"""*** write a python program to find the nth prime number ***
Input n=6
output=13"""

"""n=int(input("enter an number : "))
i=1
prime_count=0
while(True):
    j=1
    count=0
    while(j<=i):
        if(i%j==0):
            count=count+1
        j=j+1
    if(count==2):
        prime_count=prime_count+1
        if(prime_count==n):
            print(i)
            break
    i=i+1"""

""" ***Write a python program to print all spy numbers from 1 to 200 using while loop ***"""

"""num=int(input("enter the number : "))
i=1
while(i<=200):
    number=i
    temp=number
    sum=0
    product=1
    while(temp>0):
        digit=temp%10
        sum=sum+digit
        product=product*digit
        temp=temp//10
    if(sum==product):
        print(number)
    i=i+1"""

"""write a python program to print all palindrome numbers from 1 to 200 using while loop """

"""num=int(input("enter an number "))
i=1
while(i<=num):
    number=i
    reverse=0
    while(number>0):
        digit=number%10
        reverse=reverse*10+digit
        number=number//10
    if(reverse==i):
        print(i)
    i=i+1
"""
""" write a python program to print the first and last digit of a given number using a while loop """

"""num=int(input("enter an number: "))
temp=num
count=0
while(temp>0):
    temp=temp//10
    count=count+1
div=10**(count-1)
first=num//div
last=num%10
print("first:",first)
print("last",last)
"""