"""1. Write a Python program using a for loop to print all even numbers from 1 to N.
Input:
20
Output:
2 4 6 8 10 12 14 16 18 20"""
"""
num=int(input("enter an number : "))
"""
"""for i in range(1,num+1):
    if(i%2==0):
        print(i)"""

"""". Write a Python program using a for loop to print all Prime Numbers from 1 to N.
Input:
30
Output:
2 3 5 7 11 13 17 19 23 29
"""
"""num=int(input("enter an number: "))
for i in range(2,num+1):
    number =i
    count=0
    for j in range(2,(number//2)+1):
        if(number%j==0):
            count=count+1
    if(count==0):
        print(number)"""
"""3. Write a Python program using a for loop to print all Perfect Numbers from 1 to N.
Input:
30
Output:
6  28
Explanation:
A Perfect Number is a number that is equal to the sum of its proper divisors (excluding the number itself)."""

"""num=int(input("enter an number : "))

for i in range(1,num+1):
    number=i
    sum=0
    for j in range(1,(number-1)+1):
        if(number%j==0):
            sum=sum+j
    if(sum==i):
        print(i)"""

"""4. Write a Python program using nested for loops to print the following Number Triangle Pattern.
Input:
5
Output:
1
12
123
1234
12345
"""
"""rows=int(input("enter an number: "))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(i,end="")
    print()"""

"""5. Write a Python program using nested for loops to print the following Repeated Number Pattern.
Input:
5
Output:
1
22
333
4444
55555
"""
"""rows=int(input("enter number of rows :  "))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(row_no,end="")
    print()"""

"""6. Write a Python program using nested for loops to print the following Right Angle Triangle Star Pattern.
Input:
5
Output:
*
**
***
****
*****"""

rows=int(input("enter number of rows: "))
for row_cnt in range(1,rows+1):
    print("*"*row_cnt,end="")
    print()