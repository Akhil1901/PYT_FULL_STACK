"""nums=[11,8,6,10,12,9,15,20,18]
output=[]
temp=[]
i=0
while(i<len(nums)):
    start=i
    last=i+2
    temp=nums[start:last+1:1]
    length=len(temp)
    j=0
    for j in range(0,length):
            if(length==2 or length==1):
                 break
            else: 
                org=temp[length-2]
                previous_element=temp[j]
                next_element=temp[length-1]
                if(org>previous_element and org<next_element):
                    if org not in output:
                         output.append(org)
    i=i+1
print(output)"""

"""t1=(10,20,30,20,40,50,30)
t2=(30,40,60,20,70)
out=[]
for i in t1:
    for j in t2:
        if(i==j):
            if i not in out:
                out.append(i)
print(tuple(out))"""

"""t=(12,5,18,7,20,15)
l_a_d=0
for i in range(0,len(t)-1):
    first=t[i]
    second=t[i+1]
    if(second>first):
        difference=second-first
        if(difference>l_a_d):
            l_a_d=difference
print(l_a_d)

"""
"""
Write a Python program to create a new list containing only the elements that are smaller than both their neighboring elements.

Input:


nums = [15, 8, 20, 5, 18, 4, 22]


Output:


[8, 5, 4]"""



"""nums=[15,8,20,5,18,4,22]
output=[]
for i in range(0,len(nums)-2):
    previous=nums[i]
    current=nums[i+1]
    next_element=nums[i+2]
    if(current<previous and current<next_element):
        output.append(current)
print(output)"""

"""Write a Python program to find the largest absolute difference between two consecutive elements.

Input:


nums = [25, 10, 30, 18, 40]


Output:


22"""

"""nums=[25,10,30,18,40]
largest_absolute_difference=0
for i in range(0,len(nums)-1):
    first=nums[i]
    second=nums[i+1]
    if(second>first):
        difference=second-first
        if(difference>largest_absolute_difference):
            largest_absolute_difference=difference
print(largest_absolute_difference)"""

"""Question 1: Find the missing numbers

Input:


nums = [1, 2, 4, 6, 7, 10]


Output:


[3, 5, 8, 9]"""

"""nums=[1,2,4,6,7,10]
output=[]
res=max(nums)
for i in range(1,res+1):
    if(i not in nums):
        output.append(i)
print(output)"""


"""Question 1: Find all increasing pairs
Input:


t = (3, 5, 2, 4, 6)


Output:


(3, 5)
(2, 4)
(4, 6)"""

"""t=(3,5,2,4,6)
for i in  range(0,len(t)-1):
    first=t[i]
    second=t[i+1]
    if(second>first):
        print("(",first,second,")")"""

"""Count the length of each increasing sequence.

Input:

t = (3, 5, 7, 2, 4, 6, 1, 9)

Output:

3
3
2"""

