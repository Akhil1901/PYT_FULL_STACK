'''num= int(input("enter the number "))
if(num>0):
    print("positive") '''
'''string= input ("enter the string: ")
if (string == ""):
    print("empty string")'''
'''num=int(input("enter a num:"))
if(num>0):
    print("positive")
if(num<0):
    print("negative")
if(num==0):
    print("zero")'''
'''num=int(input("enter a num:"))
if(num%3==0 and num%5==0):
    print("divisible by both 3 and 5")'''
'''num=int(input("enter a num:"))
if(num%2==0 and num%3==0):
    print("divisible both 2 and 3")'''
'''num=int(input("enter a num : "))
if(num%4==0):
    print("multiple of 4")'''
'''num = int(input("enter an num :"))
root = num ** 0.5
if num == root**2:
    print("perfect square")'''
'''year = int(input("enter a year:"))
if((year%4==0 and year%100!=0) or (year%400==0)):
    print("leap year")'''
list=['a','e','i','o','u']
''''character=input("enter a character:")'''
'''if (character in list):
    print("vowel")
else:
    print("consonants")'''
'''num=int(input("enter a num : "))
one=1
if(num%one==0 and num%num==0 and num%2!=0 and num%3!=0):
    print("prime number")
else:
    print("not prime number")'''
'''year=int(input("enter a year:"))
if(year%100==0):
    print("century year")
else:
    print("not century year")'''
'''num=int(input("enter a num: "))
if(num<=0):
    print("non positive")
else:
    print("positive")'''
'''num1=int(input("enter a num:"))
num2=int(input("enter a num:"))
if(num1>num2):
    print("the largest one is:",num1)
else:
    print("the largest one is:",num2)'''
'''letter=input("enter a letter:")
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if (letter in alphabets and letter in Alphabets):
    print("characteris a letter")
else:
    print("character is not a letter")'''
'''num1=int(input("enter a num:"))
num2=int(input("enter a num:"))
num3=int(input("enter a num:"))'''
'''sum=0
i=1
while(i<=100):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)'''
'''import random
random_number=random.randint(1,10)
while(True):
    num=int(input("enter a num:"))
    if(num<random_number):
        print("too low")
    elif(num>random_number):
        print("high")
    else:
        print("guess correct")
        break'''
'''num=int(input("enter a number:"))
fact=1
while(num!=1):
    fact=fact*(num)
    num=num-1
print(fact)'''
'''num=int(input("enter a number:"))
while(num>=1):
    print(num)
    num=num-1'''
'''sum=0
i=1
while(i<=100):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)'''
'''i=1
while(i<=50):
    if(i%2==0):
        print(i)
    i=i+1'''
'''num=int(input("enter a number:"))
i=1
sum=0
while(i<=num):
    sum=sum+i
    i=i+1
print(sum)'''
'''num=int(input("enter a number:"))
product=1
i=1'''
'''while(i<=100):
    product=num*i
    print(num,"*",i,"=",product)
    i=i+1'''
'''num=int(input("enter a number:"))
i=1
while(i<=num):
    if(num%i==0):
        print(i,"divisor of ",num)
    i=i+1'''
'''password=input("enter your password :")
while(True):
    give_password=input("enter your password")
    if(give_password==password):
        print("correct password")
        break'''
'''num=int(input("enter the n value:"))
i=0
first=0
second=0
while(i<=num):
    print(first)'''
'''num=int(input("enter a number: "))
i=1
count=0
while(i<=num):
    if(num%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("prime number")
else:
    print("not prime")'''
'''num=int(input("enter the number: "))
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print(reverse)'''
num = 100
i = 1

while i <= num:
    j = 1
    count = 0

    while j <= i:
        if i % j == 0:
            count += 1
        j += 1

    if count == 2:
        print(i)

    i += 1