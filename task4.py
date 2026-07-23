"""num=int(input("enter an number : "))
count=0
while(num>0):
    digit=num%10
    if(digit%2==0):
        count=count+1
    num=num//10
print(count)"""

"""num=2
while(num<=100):
    d=2
    while(d<=num//2):
        if(num%d==0):
            break
        d=d+1
    else:
        print(num)
    num+=1"""
"""num=int(input("enter an number : "))
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)"""
"""num=int(input("enter an number : "))
largest=0
while(num>0):
    digit=num%10
    if(digit>largest):
        largest=digit
    num=num//10
print(largest)
"""
"""num=int(input("enter an number "))
sum=0
product=1
while(num>0):
    digit=num%10
    sum=sum+digit
    product=product*digit
    num=num//10
if(sum==product):
    print("given number is spy number")
else:
    print("not spy number ")"""

"""num=int(input("enter an number: "))
count=0
i=1
while(i<=num):
    if(num%i==0):
        count+=1
    i=i+1
if(count==2):
    print("prime number")
else:
    print("not prime")"""



"""num=int(input("enter an number:  "))
i=1
while(i<=100):
    j=1
    count=0
    while(j<=i):
        if(i%j==0):
            count=count+1
        j=j+1
    if(count==2):
        print(i)
    i=i+1
"""
"""n = int(input("Enter value: "))

a = 0
b = 1
count1 = 0

while T:

    c = a + b

    # Prime check
    count = 0
    i = 1

    while i <= c:
        if c % i == 0:
            count += 1
        i += 1

    if count == 2:
        count1 += 1

        if count1 == n:
            print(c)
            break

    a = b
    b = c
"""
"""n=int(input("enter an number : "))
i=1
count2=0
while(True):
    j=1
    count=0
    while(j<=i):
        if(i%j==0):
            count=count+1
        j=j+1
    if(count==2):
        count2=count2+1
        if(count2==n):
            print(i)
            break
    i=i+1"""
