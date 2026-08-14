"""1. Write a Python program to create a new list containing only the elements that are greater than the average of the given list.
Input:
[10, 20, 30, 40, 50]
Output:
[40, 50]"""

"""num=[10,20,30,40,50]
out=[]
avg=sum(num)//len(num)
for i in num:
    if(i>avg):
       out.append(i)
print(out) """

"""2. Write a Python program to create a new list containing only the numbers whose reverse is divisible by the original number.
Input:
[12, 22, 25, 44, 13]
Output:
[22, 44]"""
"""num=[12,22,25,44,13]
out=[]
for i in num:
    temp=i
    reverse=0
    while(temp>0):
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10
    if(reverse%i==0):
        out.append(i)
print(out)"""

"""3. Write a Python program to create a new list containing only the numbers whose sum of digits is greater than the product of their digits.
Input:
[12, 22, 111, 24, 123]
Output:
[111]"""

"""num=[12,22,111,24,123]
out=[]
for i in num:
    temp=i
    sum=0
    product=1
    while(temp>0):
        digit=temp%10
        sum=sum+digit
        product=product*digit
        temp=temp//10
    if(sum>product):
        out.append(i)
print(out)"""

"""
    4. Write a Python program to create a new list containing only the elements that are divisible by the sum of their digits.
Input:
[12, 18, 20, 25, 27, 30]
Output:
[12, 18, 20, 27, 30]"""

"""num=[12,18,20,25,27,30]
out=[]
for i in num:
    temp=i
    sum=0
    while(temp>0):
        digit=temp%10
        sum=sum+digit
        temp=temp//10
    if(i%sum==0):
        out.append(i)
print(out)"""


"""5. Write a Python program to create a new list containing only the numbers whose first digit is equal to the last digit.
Input:
[11, 23, 44, 57, 99, 101]
Output:
[11, 44, 99, 101]"""

"""num=[11,23,44,57,99,101]
out=[]
for i in num: 
    temp=i
    org=i
    count=0
    while(temp>0):
        temp=temp//10
        count=count+1
    d=10**(count-1)
    first=org//d
    last=org%10
    if(first==last):
        out.append(i)
print(out)"""

"""1. Write a Python program to find the difference between the largest and smallest elements in a given list.
Input:
[18, 7, 25, 12, 30]
Output:
23"""

"""num=[18,7,25,12,30]
largest=0
smallest=num[0]
for i in num:
    if(i>largest):
        largest=i
    if(i<smallest):
        smallest=i
difference=largest-smallest
print(difference)"""

"""2. Write a Python program to create a new list containing only the numbers whose sum of factors is a Perfect Square.
Input:
[1, 3, 22, 66, 70, 81, 94]
Output:
[1, 3, 22, 66, 70, 81, 94]"""

"""num=[1,3,22,66,70,81,94]
out=[]
for i in num:
    temp=i
    j=1
    sum=0
    while(j<=temp):
        if(temp%j==0):
            sum=sum+j
        j=j+1
    root=sum**0.5
    value=root**2
    if(value==sum):
        out.append(i)
print(out)"""

"""3. Write a Python program to create a new list containing only the numbers for which the difference between the number and its reverse is divisible by 9.
Input:
[12, 15, 23, 41, 56]
Output:
[12, 15, 23, 41, 56]"""

"""num=[12,15,23,41,56]
out=[]
for i in num:
    temp=i
    reverse=0
    while(temp>0):
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10
    difference=i-reverse
    if(difference%9==0):
        out.append(i)
print(out)"""

"""4. Write a Python program to print the list excluding the first and last elements using slicing.
Input:
[10, 20, 30, 40, 50, 60, 70]
Output:
[20, 30, 40, 50, 60]"""


"""num=[10,20,30,40,50,60,70]
print(num[1:6:1])"""


"""5. Write a Python program to print the list in reverse order using slicing.
Input:
[10, 20, 30, 40, 50, 60]
Output:
[60, 50, 40, 30, 20, 10]
"""

"""num=[10,20,30,40,50,60]
print(num[::-1])
"""

"""6. Write a Python program to print every second element of the given list using slicing.
Input:
[10, 20, 30, 40, 50, 60, 70, 80]
Output:
[10, 30, 50, 70]"""

"""num=[10,20,30,40,50,60,70,80]
print(num[0::2])"""

"""7. Write a Python program to print the list from the 3rd element to the 6th element using slicing.
Input:
[10, 20, 30, 40, 50, 60, 70, 80]
Output:
[30, 40, 50, 60]"""

"""num=[10,20,30,40,50,60,70,80]

print(num[2:6])"""

"""1. Write a Python program to print the list starting from the second element up to the second last element, taking every third element using slicing.

Input:
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Output:
[20, 50, 80]"""

"""num=[10,20,30,40,50,60,70,80,90,100]
print(num[1:9:3])"""


"""2. Write a Python program to print the list from the third last element to the beginning in reverse order using slicing.

Input:
[10, 20, 30, 40, 50, 60, 70, 80]

Output:
[60, 50, 40, 30, 20, 10]"""

"""num=[10,20,30,40,50,60,70,80]
print(num[5::-1])
"""
"""3. Write a Python program to divide the given list into two equal halves and swap the halves using slicing.

Input:
[10, 20, 30, 40, 50, 60, 70, 80]

Output:
[50, 60, 70, 80, 10, 20, 30, 40]
 """


# 3. Write a Python program to divide the given list into two equal halves and swap the halves using slicing.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]

# Output:
# [50, 60, 70, 80, 10, 20, 30, 40]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
mid = len(li)//2
li = li[mid:]+  li[:mid]
print(li) """







