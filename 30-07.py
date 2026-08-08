"""4. Write a Python program using nested for loops to print the following Continuous Alphabet Triangle Pattern.
Input:
5
Output:
A
BC
DEF
GHIJ
KLMNO
"""
"""rows=int(input("enter an number :"))
count=1
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(chr(64+count),end="")
        count=count+1
    print()"""
"""5. Write a Python program using nested for loops to print the following Reverse Alphabet Triangle Pattern.
Input:
5
Output:
ABCDE
ABCD
ABC
AB
A"""
"""rows=int(input("enter an number :"))
for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+2):
        print(chr(64+i),end="")
    print()"""
"""Write a Python program using nested for loops to print the following Reverse Descending Alphabet Pattern.
Input:
5
Output:
EDCBA
EDCB
EDC
ED
E
"""
"""rows=int(input("enter no of rows: "))
for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+2):
        print(chr(64+(rows-i)+1),end="")
    print()"""

"""1. Write a Python program using a for loop to print all numbers from 1 to N that have exactly 3 factors.
Input:
30
Output:
4 9 25________________________________________"""

"""num=int(input("enter an number"))
for i in range(1,num+1):
    number=i
    fact=0
    for i in range(1,number+1):
        if(number%i==0):
            fact=fact+1
    if(fact==3):
        print(i)"""
"""2. Write a Python program using a for loop to print all numbers from 1 to N whose product of digits is an even number.
Input:
25
Output:
2 4 6 8 10 12 14 16 18 20 21 22 23 24 25________________________________________"""
"""num=int(input("enter an number: "))

for i in range(1,num+1):
    number=i
    product=1
    while(number>0):
        digit=number%10
        product=product*digit
        number=number//10
    if(product%2==0):
        print(i)"""

""" Write a Python program using a for loop to print all numbers from 1 to N that are divisible by the sum of their digits.
Input:
30
Output:
1 2 3 4 5 6 7 8 9 10 12 18 20 21 24 27 30________________________________________"""

"""num=int(input("enter an number: "))
for i in range(1,num+1):
    number=i
    sum=0
    while(number>0):
        digit=number%10
        sum=sum+digit
        number=number//10
    if(i%sum==0):
        print(i)"""
"""
*
**
***
****
*****
"""
"""rows=int(input("enter no of rows: "))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print("*",end="")
    print()"""
"""
*****
****
***
**
*
"""
"""rows=int(input("enter no of rows: "))
for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+2):
        print("*",end="")
    print()"""

"""
*****
 ****
  ***
   **
    *
    """
"""rows=int(input("enter no of rows: "))

for row_no in range(1,rows+1):
    for i in range(1,row_no):
        print(" ",end="")
    for j in range(1,rows-row_no+2):
        print("*",end="")
    print()"""

"""n=int(input(""))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))"""

"""n=int(input("enter no of rows: "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,2*i):
        print("*",end="")
    print()"""
"""n=int(input("enter of rows: "))
for i in range(1,n+1):
    print(" "*(i-1) +"*"*(2*(n-i)+1))"""
