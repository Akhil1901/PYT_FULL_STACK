'''num=int(input("enter a number:"))
if(num>0):
    print("positive ")'''
'''num=int(input("enter a number:"))
if(num%5==0):
    print("divisible by 5")'''
'''age=int(input("enter your age :"))
if(age>=18):
    print("eligible for vote")'''
'''num=int(input("enter a number:"))
if(num%2==0):
    print("even number")'''
'''num=int(input("enter a number:"))
if(num>=35):
    print("student passed")'''
'''year=int(input("enter a year:"))
if(year%100==0):
    print("century year")'''
'''num=int(input("enter a number:"))
if(num%10==0):
    print("multiple of 10")'''
'''string=input("enter a password:")
if(len(string)>=8):
    print("password is atleast 8")'''
'''num=int(input("enter a number:"))
if(num>99 and num<1000):
    print("three digit number")'''
'''num=int(input("enter a number:"))
if(num%2==0):
    print("even number")
else:
    print("odd number")'''
'''num=int(input("enter a number:"))
if(num>0):
    print("positive")
else:
    print("negavtive")'''
'''num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
if(num1>num2):
    print(num1,"is greater")
else:   
    print("num2 is greater")'''
'''num=int(input("enter the num : "))
count=0
while(num>0):
    num=num//10
    count=count+1
print("no of digits",count)'''
'''num=int(input("enter a number: "))
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print("Sum of digits = ", sum)'''
'''num=int(input("enter a number:"))
largest=0
while(num>0):
    digit = num %10
    if digit>largest:
        largest=digit
    num=num//10
print("Largest digit = ", largest)'''
'''num=int(input("enter an number: "))
smallest=9
while(num>0):
    digit=num%10
    if digit<smallest:
        smallest=digit
    num=num//10
print("smallest digit=",smallest)'''
'''num=int(input("enter a number : "))
count=0
while(num>0):
    digit=num%10
    if(digit%2!=0):
        count=count+1
    num=num//10
print("odd digits: ",count)'''
'''num=int(input("enter an number:"))
sum=0
odd_sum=0
while(num>0):
    digit=num%10
    if(digit%2==0):
        sum=sum+digit
    elif(digit%2!=0):
        odd_sum=odd_sum+digit
    num=num//10
print("sum of even digits",sum)
print("sum of odd digits",odd_sum)'''
'''num=int(input("enter an number:"))'''
'''i=1
count=0
while(i<=num):
    if(num%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime number")
else:
    print("not prime number")
'''
'''num = int(input("Enter a number: "))

fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print("Factorial =", fact)'''
'''num=int(input("enter a number"))
original=num
sum=0
while(num>0):
    digit=num%10
    sum=sum+(digit**3)
    num=num//10

if(original==sum):
    print("armstrong number")
else:
    print("not an amstrong number")'''
'''num=int(input("enter a number"))
original=num
i=1
fact=1
sum=0
while(num>0):
    digit=num%10

    while(i<=num):
        fact=fact*i
        i=i+1

    sum=sum+fact
    num=num//10

if(original==sum):
    print("strong number")
else:
    print("not strong")'''
'''num=int(input("enter an number: "))
i=1
j=0
while(i<=(num-1)):
    if(num%i==0):
        largest=0
        j=i
        if(j>largest):
            largest=j
    i=i+1
print(largest)'''
""" num=int(input("enter an number: "))
i=1
sum=0
while(i<=(num-1)):
    if(num%i==0):
        sum=sum+i
    i=i+1

if(sum==num):
    print("perfect number")
else:
    print("not perfect number") """
'''num=int(input("enter a number:"))
i=1
while(i<=num):
    j=1
    sum=0
    while(j<=(i-1)):
        if(i%j==0):
            sum=sum+j
        j=j+1
    if(sum==i):
        print(i)
    i=i+1'''
'''num=int(input("enter an number: "))
i=1
counter=0
while(i<=num):
    j=1
    count=0
    while(j<=i):
        if(i%j==0):
            count=count+1
        j=j+1
    if(count==2):
        counter=counter+1
    i=i+1
print(counter)'''
''''num=int(input("enter an number: "))
i=1
sum=0
while(i<=num):
    j=1
    count=0
    while(j<=i):
        if(i%j==0):
            count=count+1
        j=j+1
    if(count==2):
        sum=sum+i
    i=i+1
print(sum)'''
'''num1=int(input("enter a number:"))
num2=int(input("enter the number : "))
if(num2>num1):
    smallest=num1
else:
    smallest=num2
i=1
gcd=1
while(i<=smallest):
    if(num1%i==0 and num2%i==0):
        gcd=i
    i=i+1
if(gcd==1):
    print("co prime")
else:
    print("not co-prime")'''
'''num1=int(input("enter a number : "))
num2=int(input("enter a number: "))
num3=int(input("enter the number: "))
if(num1>num2 and num1>num3):
    smallest = num3
elif(num3>num2 and num3>num1):
    smallest=num1
else:
    smallest=num2
i=1
hcf=1
while(i<=smallest):
    if(num1%i==0 and num2 % i == 0 and num3 % i == 0):
        hcf=i
    i=i+1
print(hcf)'''
'''num1=int(input("enter an number:"))
num2=int(input("enter the number: "))
num3=int(input("enter the number: "))
if(num1>num2 and num1>num3):
    lcm = num1
elif(num3>num2 and num3>num1):
    lcm=num3
else:
    lcm=num2
i=1
while(i<=lcm):
    if(lcm % num1 ==0 and lcm % num2 == 0 and lcm % num3 == 0):
        break
    lcm=lcm+1
print(lcm)'''
'''num=int(input("enter the number: "))
original=num
square=num*num
sum=0
while(square>0):
    digit=square%10
    sum=sum+digit
    square=square//10
if(sum==original):
    print("neon number")
else:
    print("not neon number")'''
'''num=int(input("enter a number"))
sum=0
product=1
while(num>0):
    digit=num%10
    sum=sum+digit
    product=product*digit
    num=num//10
if(product==sum):
    print("spy number")
else:
    print("not a spy number")'''
'''num=int(input("enter a number"))
sum=0
product=1
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
if(num%sum==0):
    print("harshad number")
else:
    print("not a harshad number")'''
'''num=int(input("enter an number: "))
while(num>0):
    digit=num%10
    if(digit==0):
        print("duck number")
        break
    num=num//10'''
'''num1=int(input("enter an number"))
num2=int(input("enter an number"))
if(num2>num1):
    small=num1
else:
    small=num2
i=2
while(small>=i):
    if(num1%small==0 and num2%small==0):
        print("gcd is",small)
        break
    small=small-1
else:
    print("no gcd")'''
'''num=int(input("enter a number: "))
search=int(input("enter a number to search "))
frequency = 0
while(num>0):
    digit=num%10
    if(digit==search):
        frequency=frequency+1
    num=num//10
if(frequency==0):
    print("enter a number present in the num ")
else:
    print("frequency:",frequency)'''
'''num=int(input("enter a number: "))
while(num>0):
    digit=num%10
    if(digit%2==0):
        print("not all are odd")
        break
    num=num//10
else:
    print("all are odd")'''
'''num1=int(input("enter a number 1 : "))
num2=int(input("enter the number 2 : "))
reverse=0
while(num1>0):
    digit=num1%10
    reverse = reverse*10+digit 
    num1=num1//10
if(reverse==num2):
    print("reverse of each other ")
else:
    print("not reverse of each other ")'''
'''num=int(input("enter the number: "))
replace = 0
original=0
while(num>0):
    digit=num%10
    if(digit==0):
        digit=1
    replace=replace*10+digit
    num=num//10
while(replace>0):
        digit1=replace%10
        original=original*10+digit1
        replace=replace//10
print(original)
'''
'''num = int(input("Enter a number: "))

i = 2

while num > 1:
    if num % i == 0:
        print(i, end=" ")
        num = num // i
    else:
        i = i + 1'''
'''num=int(input("enter a number: "))
while(num>0):
    digit=num%10
    if(digit==5):
        print("num contains 5")
        break
    num=num//10
else:
    print("num doesnot contain 5")'''
'''num = int(input("Enter a number: "))

binary = 0

while num > 0:
    remainder = num % 2
    binary = binary * 10 + remainder
    num = num // 2

reverse = 0

while binary > 0:
    digit = binary % 10
    reverse = reverse * 10 + digit
    binary = binary // 10

print("Binary =", reverse)'''
'''num = int(input("Enter a number: "))
while num >= 10:
    num = num // 10
print("First digit =", num)'''
"""num=int(input("enter the number : "))
original=num
search=0
while(search<=9):
    temp=original
    count=0
    while(temp>0):
        digit=temp%10
        if(digit == search):
            count=count+1
        temp=temp//10
    print(search,":",count)
    search=search+1"""