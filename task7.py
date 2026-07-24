""""
1. Write a Python program to count how many digits in a given number are multiples of 3 using a while loop.
Input: 9362481
Output: 4"""


"""num=int(input("enter an number : "))
count=0
while(num>0):
    digit=num%10
    if(digit%3==0):
        count=count+1
    num=num//10
print(count)"""

"""2. Write a Python program to check whether the first digit of a number is equal to the last digit using a while loop.

Input: 74547
Output: Yes"""


"""num=int(input("enter an number "))
temp=num
count=0
while(num>0):
    num=num//10
    count=count+1
print(count)

first =0
last=0
i=0
num=temp
while(num>0):
    digit=num%10
    i=i+1 
    if(i==1):
        first=digit
    elif(i==count):
        last=digit
    num=num//10
print(first)
print(last)
if(first==last):
    print("digits are equal")
else:
    print("digits are not equal")
"""
"""
5. Write a Python program to print all numbers between 1 and N whose sum of digits is even using a while loop.
Input: 20
Output:
2 4 6 8 11 13 15 17 19 20"""
""" num=int(input("enter an number : "))

i=1 
while(i<=num):
    number=i
    if(number<=9):
        if(number%2==0):
            print(number)
    else:
        temp=number
        sum=0
        while(temp>0):
            digit=temp%10
            sum=sum+digit
            temp=temp//10
        if(sum%2==0):
            print(number )
    i=i+1 """

# 3. Write a Python program to print the following square pattern.
# Input: 5
# Output:

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

""" rows = 5
row_cnt = 1

while row_cnt<=rows:
    print("*"*rows)
    row_cnt+=1 """

# *****
# ****
# ***
# **
# *

rows = 5
row_cnt = 1
while row_cnt<=rows:
    print("*"*(rows-row_cnt+1))
    row_cnt+=1