"""num=int(input("enter an number : "))
count=0
while(num>0):
    num=num//10
    count=count+1
print(count)"""
"""num=int(input("enter an number "))
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)"""
"""num=int(input("enter an number: "))
product=1
while(num>0):
    digit=num%10
    product=product*digit
    num=num//10
print(product)
"""
"""num=int(input("enter an number: "))
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)"""
"""num=int(input("enter an number : "))
last=0
while(num>0):
    digit=num%10
    if(digit==0):
        last=digit
    elif(digit<=9 and num!=0):
        last=digit
        print(last)
        break
    num=num//10"""
"""num=int(input("enter an number : "))
largest=0
while(num>0):
    digit=num%10
    if(digit>largest):
        largest=digit
    num=num//10
print(largest)"""

"""num=int(input("enter an number : "))
smallest=9
while(num>0): 
    digit=num%10
    if(digit<smallest):
        smallest=digit
    num=num//10
print(smallest)
"""
"""num=int(input("enter an number : "))
count=0
while(num>0):
    digit=num%10
    if(digit%3==0):
        count=count+1
    num=num//10
print(count)"""
#Find the First Even Digit (from the Left)
"""num=int(input("enter an number : "))
temp=num
evn_cnt=0
while(num>0):
    digit=num%10
    if(digit%2==0):
        evn_cnt=evn_cnt+1
    num=num//10
while(temp>0):
    digit=temp%10
    if(digit%2==0):
        evn_cnt=evn_cnt-1
        if(evn_cnt==0):
            print(digit)
            break
    temp=temp//10"""
"""num=int(input("enter an number"))
count=0
past_digit=0
present_digit=0
while(num>0):
    digit=num%10
    present_digit=digit
    if(present_digit==past_digit):
        count=count+1
    past_digit=digit
    num=num//10
print(count)"""

num=int(input("enter an number: "))
count2=0
product=1
while(num>0):
    digit=num%10
    i=1
    count=0
    while(i<=digit):
        if(digit%i==0):
            count=count+1
        i=i+1
    if(count==2):
        product=product*digit
    num=num//10
print(product)



























