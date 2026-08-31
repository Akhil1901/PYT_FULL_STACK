"""Write a Python function to find the longest palindrome substring in a given string.
If multiple palindromes have the same length,
return the one that appears first. 
Input: "forgeeksskeegfor" 
Output: "geeksskeeg"""

"""Write a Python program to find the second-largest unique element from each tuple and 
store the results in a list. 
Input: [(10, 5, 8, 10), (7, 12, 3, 9), (20, 15, 20, 18)] 
Output: [8, 9, 18]"""
"""li=[(10, 5, 8, 10), (7, 12, 3, 9), (20, 15, 20, 18)] 
output=[]
for i in li:
    tu=i
    largest=max(tu)
    for j in tu:
        count=0
        for k in tu:
            if(j==k):
                count=count+1
        if(count<2):
            for z in tu:
                if(j<largest):
                    if(j>z and j!=largest):
                        if(j not in output):
                           output.append(k)
print(output)"""

"""Set + List Write a Python program to find all elements that occur in the list more than once, 
but return them as a set without using count(). 
Input: [4, 7, 2, 4, 9, 7, 3, 2, 8, 7] 
Output: {2, 4, 7}"""
"""li=[4, 7, 2, 4, 9, 7, 3, 2, 8, 7]
n_li=[]
for i in li:
    count=0
    for j in li:
        if(i==j):
            count=count+1
    if(count>1):
        n_li.append(i)
print(set(n_li))"""

"""Write a Python program using a nested function where 
the inner function modifies a variable from the outer function using nonlocal. 
Each call should increase the value by the given input. 
Input: start = 10 
values = [5, 8, 12] 
Output: 15 23 35"""
       