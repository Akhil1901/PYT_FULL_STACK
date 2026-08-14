"""1. Write a Python program to find all indices where a given element occurs in a list.
Input:
[10, 20, 30, 20, 40, 20]
Target = 20
Output:
[1, 3, 5]"""
"""list = [10,20,30,20,40,20]
output=[]
Target=20
i=0
while(i<len(list)):
    if(list[i]==Target):
        output.append(i)
    i=i+1
print(output)
"""
"""2. Write a Python program to find all the missing numbers in a list.
Input:
[1, 2, 4, 6, 7, 9]
Output:
[3, 5, 8]
"""
"""list=[1,2,4,6,7,9]
output=[]
for i in range(1,10):
    if i not in list:
        output.append(i)
print(output)"""

"""3. Write a Python program to find the last occurrence of a target element in a list.
Input:
[2, 4, 4, 4, 6, 8, 10]
Target = 4
Output:
3"""

"""list=[2,4,4,4,6,8,10]
Target=4
count=0
for i in list:
    if(i==Target):
        count=count+1
print(count)
"""
"""4. Write a Python function to return a new list containing only the elements whose indices are Fibonacci numbers.
Input:
[10, 20, 30, 40, 50, 60, 70, 80, 90]
Output:
[10, 20, 30, 40, 60, 90]"""

""""list=[10,20,30,40,50,60,70,80,90]
output=[]
a=0
b=1
i=0
output.append(list[a])
while i<= len(list):
    c=a+b
    output.append(c)
    a=b
    b=c
    i=i+1
print(output)"""
"""5. Write a Python program to print all elements in a list that are equal to the product of all previous elements.
Input:
[2, 3, 6, 36, 5]
Output:
6 36
Explanation:
6 = 2 × 3
36 = 2 × 3 × 6"""


"""list=[2,3,6,36,5]
product=1
for i in list:
    if(i==product):
        print(i)
    product=product*i"""

"""6. Write a Python program to split a list into groups of 3 elements using slicing and print only the groups in which every element is greater than 10.
Input:
[12, 15, 18, 5, 20, 25, 30, 35, 40]
Output:
[12, 15, 18]
[30, 35, 40]
Explanation:
Split the list into groups of 3 elements and print only those groups where every element is greater than 10."""

list=[12,15,18,5,20,25,30,35,40]
i=0
while(i<len(list)):
    test=list[i:(i+3):1]
    for x in test:
        
    
    i=i+3