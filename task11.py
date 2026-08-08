"""1. Write a Python program to find the largest element in a given list.
Input:
[12, 45, 7, 89, 23]
Output:
89"""
"""list=[12,45,7,89,23]
largest=0
for i in list:
    if(i>largest):
        largest=i
print(largest)"""

"""2. Write a Python program to print all the elements present at even indices of a given list.
Input:
[10, 20, 30, 40, 50, 60, 70]
Output:
[10, 30, 50, 70]"""
"""list=[10,20,30,40,50,60,70]
even_list=[]
for i in list:
    index=list.index(i)
    if(index%2==0):
        even_list.append(list[index])
print(even_list)"""
"""3. Write a Python program to find the sum of all elements in a given list.
Input:
[5, 10, 15, 20]
Output:
50"""
"""list=[5,10,15,20]
sum=0
for i in list:
    sum=sum+i
print(sum)"""
"""4. Write a Python program to create a new list containing only the numbers whose sum of factors is a Prime Number.
Input:
[9, 16, 20, 25]
Output:
[9, 16, 25]
"""
"""list=[9,16,20,25]
new_list=[]
for i in list:
    number=i
    sum=0
    for j in range(1,number+1):
        if(number%j==0):
            sum=sum+j
    count=0
    for k in range(1,sum+1):
        if(sum%k==0):
            count=count+1
    if(count==2):
        new_list.append(i)
print(new_list)
"""
"""5. Write a Python program to create a new list containing only the numbers for which the sum of the number and its reverse is a Palindrome Number.
Input:
[12, 15, 19, 23, 28]
Output:
[12, 15, 23]
"""
"""list=[12,15,19,23,28]
new_list=[]

for i in list:
    temp=i
    org=i
    sum=0
    rev=0
    while(temp>0):
        digit=temp%10
        sum=sum+digit
        temp=temp//10
    num=sum
    while(num>0):
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if(sum==rev):
        new_list.append(org)
print(new_list)"""