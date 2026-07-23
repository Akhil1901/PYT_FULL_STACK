
"""#Count the number of digit#"""
"""num=int(input("enter an number : "))
bkp=num
count=0
while(num>0):
    num=num//10
    count=count+1
print(count)"""
"""Find the sum of digits.
"""
"""num=int(input("enter an number : "))
bkp=num
count=0
while(num>0):
    num=num//10
    count=count+1
d=10**(count-1)
num=bkp
sum=0
while(num>0):
    digit=num//d
    sum=sum+digit
    num=num%d
    d=d//10
print(sum)"""

"""*** Find the product of digits. ****"""
""""num=int(input("enter an number: "))
bkp = num
count=0
while(num>0):
    num=num//10
    count=count+1
print(count)
d=10**(count-1)
print(d)
num=bkp
product=1
while(num>0):
    digit=num//d
    product=product*digit
    num=num%d
    d=d//10
print(product)
"""

"""****  Find the largest digit.   ***"""

"""num=int(input("enter an number: "))
temp=num
count=0
while(num>0):
    num=num//10
    count=count+1
print(count)
d=10**(count-1)
num=temp
largest=0
while(num>0):
    digit=num//d
    if(digit>largest):
        largest=digit
    num=num%d
    d=d//10
print(largest)
"""
""" *** Find the smallest digit ****."""

"""num=int(input("enter an number : "))
temp=num
count=0
while(num>0):
    num=num//10
    count=count+1
d=10**(count-1)
num=temp
smallest=9
while(num>0):
    digit=num//d
    if(digit<smallest):
        smallest=digit
    num=num%d
    d=d//10
print(smallest)"""

""" *** Count even digits *** """


"""num=int(input("enter an number : "))
bkp=num
count=0
while(num>0):
    num=num//10
    count=count+1
d=10**(count-1)
num=bkp
count2=0
while(num>0):
    digit=num//d
    if(digit%2==0):
        count2=count2+1
    num=num%d
    d=d//10
print(count2)"""

"""*** Count prime digits *** """

"""num=int(input("enter an number :  "))
temp=num
count1=0
while(num>0):
    num=num//10
    count1=count1+1
d=10**(count1-1)
num=temp
count3=0
while(num>0):
    digit=num//d
    i=1
    count2=0
    while(i<=digit):
        if(digit%i==0):
            count2=count2+1
        i=i+1
    if(count2==2):
        count3=count3+1
    num=num%d
    d=d//10
print(count3)"""

"""****     Sum of prime digits.   ***"""

"""num=int(input("enter an number : "))
temp=num
cnt1=0
while(num>0):
    num=num//10
    cnt1=cnt1+1
d=10**(cnt1-1)
num=temp
cnt3=0
sum=0
while(num>0):
    digit=num//d
    i=1
    cnt2=0
    while(i<=digit):
        if(digit%i==0):
            cnt2=cnt2+1
        i=i+1
    if(cnt2==2):
        sum=sum+digit
    num=num%d
    d=d//10
print(sum)"""

"""num=int(input("enter an number : "))
temp=num
cnt1=0
while(num>0):
    num=num//10
    cnt1=cnt1+1
d=10**(cnt1-1)
cnt3=0
j=1
largest=0
num=temp
while(num>0):
    digit=num//d
    i=1
    cnt2=0
    while(i<=digit):
        if(digit%i==0):
            cnt2=cnt2+1
        i=i+1
    if(cnt2==2):
        if(digit>largest):
            largest=digit
    num=num%d
    d=d//10
print(largest)
"""
"""num=int(input("enter an number : ")) #153
largest=-1
second=-1

while(num>0):# 153 15 1
    digit=num%10 # 3 5 1
    if(digit>largest):
        third=second
        second=largest
        largest=digit
    elif(digit>second and digit!=largest):
        third=second
        second=digit 
    elif(digit>third and digit !=second and digit != largest):
         third=digit
    num=num//10   # 15  1
if(third == -1):
    print("third largest didn't found")
else:
    print("third largest", third)"""
"""num=int(input("enter an number: "))
temp=num
temp1=num
cnt=0
while(temp>0):
    temp=temp//10
    cnt=cnt+1
d=10**(cnt-1)
d1=d
evn_count=0
while(temp1>0):
    digit=temp1//d
    if(digit%2==0):
        evn_count=evn_count+1
    temp1=temp1%d
    d=d//10
print(d)
print(evn_count)
print(num)
count=0
while(num>0):
    digit=num//d1
    if(digit%2==0):
        count=count+1
    if(count==evn_count):
        print(digit)
        break
    num=num%d1
    d1=d1//10

"""
"""num=int(input("enter an number: "))
temp1=num
temp2=num
temp3=num
cnt=0
last_prime=-1
while(temp1>0):
    temp1=temp1//10
    cnt=cnt+1
d=10**(cnt-1)
d1=d
while(temp2>0):
    digit=temp2//d
    i=1
    count=0
    while(i<=digit):
        if(digit%i==0):
            count=count+1
        i=i+1
    if(count==2):
        last_prime=digit
    temp2=temp2%d
    d=d//10

print(last_prime)

"""
num=int(input("enter number: "))
position=0
while(num>0):
    digit=num%10
    position=position+1
    if(position%2==0):
        print(digit)
    num=num//10