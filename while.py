#nested loops
'''i=1
while(i<=3):
    j=1
    while(j<=3):
        print(i,j)
        j=j+1
    i=i+1'''
#all factors numbers 1 to 10
'''i=1
while(i<=10):
    j=1
    while(j<=i):
        if(i%j==0):
            print(i,":",j)
        j=j+1
    i=i+1
'''
'''i=2
while(i<=5):
    j=1
    while(j<=10):
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1'''
'''i=1
sum=0
while(i<=9):
    j=1
    while(j<=9):
        sum=i+j
        if(sum==10):
            print("(",i,",",j,")")
        j=j+1
    i=i+1'''
'''i=1
j=1
while(i<=24):
    j=1
    while(j<=24):
        if(i*j==24):
             print("(",i,j,")")
        j=j+1
    i=i+1'''
'''i=1
j=1
while(i<=5):
    j=1
    while(j<=5):
        if(i<j):
            print(i,j)
        j=j+1
    i=i+1'''
'''i=1
while(i<=9):
    j=1
    while(j<=9):
        if(i%2==0 and j%2==0):
            print(i,j)
        j=j+1
    i=i+1'''
'''i=1
while(i<=9):
    j=1
    while(j<=9):
        if((i%2==0 and j%2!=0)or(i%2!=0 and j%2==0)):
            print(i,j)
        j=j+1
    i=i+1'''
'''i=1
j=1
while(i<=9):
    j=1
    while(j<=9):
        if(j%i==0):
            print(i,j)
        j=j+1
    i=i+1'''
'''num1=int(input("enter an number : "))
num2=int(input("enter an number : "))
if(num2>num1):
    smallest=num1
else:
    smallest=num2  
i=1  
while(i<=smallest):
    if(num1%i==0 and num2%i==0):
        print(i)
    i=i+1'''
'''i=1
square=0
while(i<=20):
    j=1
    while(j<=20):
        k=1
        while(k<=20):
            square=i**2+j**2
            if(square==k**2 and i!=j and k!=j and i!=k):
                print(i,j,k)
            k=k+1
        j=j+1
    i=i+1'''
'''num=int(input("enter a number : "))
i=1
while(i<=num):
    j=1
    while(j<=10):
        if(i==j):
            print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
'''
'''num=int(input("enter an number: "))
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
'''num=int(input("enter a number : "))
reverse=0
if(num==0):
    print(1)
else:
    while(num>0):
        digit=num%10
        if(digit==0):
            digit=1
        reverse=reverse*10+digit
        num=num//10
    original=0
    while(reverse>0):
        digit1=reverse%10
        original=original*10+digit1
        reverse=reverse//10
    print(original)'''
'''num=int(input("enter an number : "))
while(num>0):
    digit=num%10
    temp = num
    count=0 
    while(temp>0):
        digit1=temp%10
        if(digit==digit1):
            count=count+1
        temp=temp//10
    if(count==1):
        print(digit)
    num=num//10'''
''''import random
secret=random.randint(1,9)
attempts=0
while(True):
    guess=int(input("enter an number : "))
    if(guess==secret):
        print("correct number")
        print("attempts",attempts)
        break
    elif(guess<secret):
        print("too low")
    elif(guess>secret):
        print("too high")
    attempts=attempts+1'''

'''pin="3005"
balance=1000
while(True):
    print("1.balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.exit")
    ch=input("enter your option")
    if(ch=="balance"):
        print(balance)
    elif(ch=='Deposit'):
        amt=int(input("enter your amount :"))
        entered_pin=input("enter your pin: ")
        if(pin==entered_pin):
            balance=balance+amt
            print("deposit sucessful")
        else:
            print("enter a valid pin")
            print("try again")
    elif(ch=='withdraw'):
        amt=int(input("enter the amount: "))
        if(amt<=balance):
            entered_pin=input("enter your pin ")
            if(pin==entered_pin):
                balance=balance-amt
                print("take the amt",amt)
            else:
                print("enter valid pin")
                print("try again")
        else:
            print("insufficinet balance")
    elif(ch=="exit"):
        print("exiting")
        print("thank you visit again")
        break
    else:
        print("enter valid option")'''
"""import random

# Generate a 2-digit number with different digits
while True:
    secret = random.randint(10, 99)
    secret_tens = secret // 10
    secret_ones = secret % 10

    if secret_tens != secret_ones:
        break

attempts = 0

while True:

    guess = int(input("Enter a 2-digit number: "))

    if guess < 10 or guess > 99:
        print("Enter a valid 2-digit number.")
        continue

    guess_tens = guess // 10
    guess_ones = guess % 10

    if guess_tens == guess_ones:
        print("Digits should not be the same.")
        continue

    attempts = attempts + 1

    bulls = 0
    cows = 0

    # Bulls
    if secret_tens == guess_tens:
        bulls = bulls + 1

    if secret_ones == guess_ones:
        bulls = bulls + 1

    # Count cows only if not already a bull
    if secret_tens != guess_tens and secret_tens == guess_ones:
        cows = cows + 1

    if secret_ones != guess_ones and secret_ones == guess_tens:
        cows = cows + 1

    print("Bulls =", bulls)
    print("Cows =", cows)

    if bulls == 2:
        print("🎉 Congratulations! You guessed the number.")
        print("Attempts =", attempts)
        break"""
"""num=int(input("enter a number : "))
reverse=0
while(num>0):
    digit=num%10
    reverse = reverse*10+digit
    num=num//10
original=0
while(reverse>0):
    digit1=reverse%10
    original=original*10+digit1
    reverse=reverse//10
print(original)"""