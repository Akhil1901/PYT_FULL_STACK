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

