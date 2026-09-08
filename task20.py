"""1. Write a Python program to find all pairs of elements whose sum is equal to the given target.
Input:
(2, 7, 11, 15, 3, 8)
Target = 10
Output:
[(2, 8), (7, 3)]"""
num=(2,7,11,15,3,8)
a=[]
target=10
for i in range(len(num)):
    for j in range(i,len(num)):
        if num[i]+num[j]==target:
            a.append(( num[i],num[j]))
print(a)
"""2. Write a Python program to remove all duplicate elements from a tuple while maintaining the original order.
Input:
(10, 20, 10, 30, 20, 40, 30, 50)
Output:
(10, 20, 30, 40, 50)"""

"""tuple1=(10,20,10,30,20,40,30,50)
list1=[]
for i in tuple1:
    if i  not in list1:
        list1.append(i)
print(tuple(list1))

"""
"""3. Write a Python program to find the longest continuous sequence of the same element in a tuple.
Input:
(1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5)
Output:
4"""

"""tuple1=(1,1,2,2,2,3,3,4,4,4,4,6,6,6,6,6,6,6,6,6,5)

longest_sequence=0
for i in tuple1:
    count=0
    for j in tuple1:
        if(i==j):
            count=count+1
    if(count>longest_sequence):
        longest_sequence=count
print(longest_sequence)"""

"""4. Write a Python program to split a tuple into two tuples: one containing elements at even indices and another containing elements at odd indices.
Input:
(10, 20, 30, 40, 50, 60, 70, 80)
Output:
Even Index Tuple: (10, 30, 50, 70)
Odd Index Tuple: (20, 40, 60, 80)
"""
num=(10,20,30,40,50,60,70,80)
even=[]
odd=[]
for i in range(0,len(num)):
    if(i%2==0):
        even.append(num[i])
    else:
        odd.append(num[i])
print(tuple(even))
print(tuple(odd))

"""5. Write a Python program to check whether a tuple is a palindrome without converting it into a list.
Input:
(10, 20, 30, 20, 10)
Output:
Palindrome"""

"""num=(10,20,30,20,10)
res=num[::-1]
if(num==res):
    print("plaindrome")"""

"""6. Write a Python program to find the common elements between two sets.
Input:
Set1 = {10, 20, 30, 40, 50}
Set2 = {30, 40, 50, 60, 70}
Output:
{30, 40, 50}"""
"""set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1 | set2)"""

"""7. Write a Python program to find all elements that are present in the first set but not in the second set.
Input:
Set1 = {10, 20, 30, 40, 50}
Set2 = {30, 40, 60, 70}
Output:
{10, 20, 50}"""

"""set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}

print(set1 - set2)"""








