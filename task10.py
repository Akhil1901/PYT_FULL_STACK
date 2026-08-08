"""1. Write a Python program using a for loop to find the Largest Prime Factor of a given number.
Input:
84
Output:
7"""
"""num=int(input("enter an number : "))
largest=0
for i in range(1,num+1):
    if(num%i==0):
        number =i
        count=0
        for j in range(1,number+1):
            if(number%j)==0 :
                count=count+1
    if(count==2):
        if(number>largest):
            largest=number
print(largest)"""
"""2. Write a Python program using a for loop to print all numbers from 1 to N whose last digit is a Prime Number (2, 3, 5, or 7).
Input:
30
Output:
2 3 5 7 12 13 15 17 22 23 25 27
"""
"""num=int(input("enter an number "))
for i in range(1,num+1):
    number=i
    last=number%10
    if(last==2 or last==3 or last==5 or last==7):
        print(i)"""
""". Write a Python program using a for loop to print all Perfect Square Numbers from 1 to N.
Input:
50
Output:
1 4 9 16 25 36 49
Explanation:
A Perfect Square Number is a number that can be expressed as the square of an integer."""

"""num=int(input("enter an number: "))
for i in range(1,num+1):
    root=i**0.5
    if(root**2==i):
        print(i)
"""
""". Write a Python program using nested for loops to print the following Alphabet Triangle Pattern.
Input:
5
Output:
A
AB
ABC
ABCD
ABCDE
"""
"""row=int(input("enter an number: "))

for row_no in range(1,row+1):
    for i in range(1,row_no+1):
        print(chr(64+i),end="")
    print()"""

"""5. Write a Python program using nested for loops to print the following Repeated Alphabet Pattern.
Input:
5
Output:
A
BB
CCC
DDDD
EEEEE
"""
"""rows=int(input("enter an number : "))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(chr(64+row_no),end="")
    print() """

"""6. Write a Python program using nested for loops to print the following Continuous Number Triangle Pattern.
Input:
5
Output:
1
23
456
78910
1112131415
"""
"""rows=int(input("enter no of rows: "))
count=1
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(count,end="")
        count=count+1
    print()
"""
