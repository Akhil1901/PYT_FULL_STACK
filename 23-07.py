"""num=int(input("enter an number : "))
n=int(input("enter an number "))
position=0
count=0
while(num>0):
    digit=num%10
    position=position+1
    if(digit==n):
        count=count+1
    num=num//10"""

"""num=int(input("enter an number"))
count=0
while(num>0):
    digit=num%10
    if(digit%2==0):
        count=count+1
    num=num//10
print(count)"""

"""num=int(input("enter an number : "))
largest=0
while(num>0):
    digit=num%10
    if(digit>largest):
        largest=digit
    num=num//10
print(largest)"""

"""num=int(input("enter an number: "))
bkp=num
temp=num
odd_cnt=0
while(num>0):
    digit=num%10
    if(digit%2!=0):
        odd_cnt=odd_cnt+1
    if(odd_cnt==1):
        print(digit)
        break
    num=num//10"""

"""num=int(input("enter an number : "))
bkp=num
temp=num
count=0
while(num>0):
    num=num//10
    count=count+1
d=10**(count-1)
num=bkp
odd_cnt=0
while(num>0):
    digit=num//d
    if(digit%2!=0):
        odd_cnt=odd_cnt+1
    if(odd_cnt==1):
        print(digit)
        break
    num=num%d
    d=d//10
"""

"""num=int(input("enter a number"))
i=1
count=0
while(i<=num):
    if(num%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime number")
else:
    print("not prime number")"""

"""num=int(input("enter an number"))
count2=0
while(num>0):
    digit=num%10
    i=1
    count=0
    while(i<=digit):
        if(digit%i==0):
            count=count+1
        i=i+1
    if(count==2):
        count2=count2+1
    num=num//10
print(count2)
"""
"""num=int(input("enter an number: "))
n=int(input("enter an number : "))
bkp=num
temp=num
count=0
while(bkp>0):
    bkp=bkp//10
    count=count+1
print(count)
d=10**(count-1)
position=0
count2=0
sum=0
while(temp>0):
    digit=temp//d
    position=position+1
    if(position%2==0):
        sum=sum+digit
    temp=temp%d
    d=d//10
print(sum)
"""

num=int(input("enter an number : "))
temp=num
bkp=num
count=0
while(temp>0):
    temp=temp//10
    count=count+1
div=10**(count-1)
sum=0
past_digit=0
while(bkp>0):
    digit=bkp//div
    print(digit)
    present_digit=digit
    if(past_digit>0 and present_digit%2==0):
        sum=sum+past_digit
    past_digit=digit
    bkp=bkp%div
    div=div//10
print(sum)























