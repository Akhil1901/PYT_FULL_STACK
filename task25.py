"""Write a Python program to find the first row containing the maximum number of even elements.
Input:
x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
Output:
[8, 12, 14, 5]
Even Count: 3"""
"""x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
high=0
for i in range(len(x)):
    temp=x[i]
    count=0
    for j in temp:
        if j%2==0:
            count=count+1
    if(count>high):
        high=count
        a=temp
print(a)"""
"""Write a Python program to find all elements that appear exactly once in the entire nested list, while maintaining their original order.
Input:
x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
Output:
[10, 40, 50, 60, 70]"""

"""x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
y=[]
z=[]
for i in x:
    y.extend(i)
for i in y:
    if y.count(i)==1:
        z.append(i)
print(z)"""

"""Write a Python program to find the row having the maximum difference between its largest and smallest elements.
Input:
x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
Output:
[8, 50, 15]
Difference: 42"""
"""x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
max_difference=0
for i in x:
    temp=i
    difference=abs(max(temp)-min(temp))
    if(difference>max_difference):
        max_difference=difference
        a=temp   
print(a)"""

""".Write a Python program to reverse only those tuples whose sum of elements is odd.
Input:
x = ((1, 2, 3),(4, 5, 2),(7, 8, 9),(10, 11, 12))
Output:
((1, 2, 3), (2, 5, 4), (7, 8, 9), (12, 11, 10))"""

"""x = ((1, 2, 3),(4, 5, 2),(7, 8, 9),(10, 11, 12))
y=[]
for i in x:
    temp=i
    s=sum(temp)
    if(s%2!=0):
       a=i[::-1]
       y.append(a)
    else:
        y.append(i) 
print(tuple(y))"""

"""Write a Python program to find the student who has the highest total marks from a nested dictionary.
Input:
students = {"Ravi": {"Math": 85, "Science": 78, "English": 90}, 
            "Priya": {"Math": 92, "Science": 88, "English": 84},
            "Arjun": {"Math": 76, "Science": 95, "English": 89}}
Output:
Student: Priya
Total Marks: 264"""
"""students = {"Ravi": {"Math": 85, "Science": 78, "English": 90}, 
            "Priya": {"Math": 92, "Science": 88, "English": 84},
            "Arjun": {"Math": 76, "Science": 95, "English": 89}}
t=0
for i in students:
    total =students[i]["Math"]+students[i]["Science"]+students[i]["English"]
    if total > t:
        t=total
        a=i
print(a)
print(t)"""



"""Write a function that returns True if a number is a Perfect Number, otherwise returns False.
Input:
n = 28
Output:
True"""

"""def is_perfect_number(num):
    sum=0
    for i in range(1,(num//2)+1):
        if(num%i==0):
            sum=sum+i
    if(sum==num):
        return True
    else:
        return False

s=28
res=is_perfect_number(s)
print(res)
"""
"""Write a function that takes a number as an argument and returns the number of digits without converting the number into a string.

Input:
n = 507080
Output:
6"""
""" n=507080

def count(num):
    count=0
    while(num>0):
        num=num//10
        count=count+1
    return count

res=count(n)
print(res) """