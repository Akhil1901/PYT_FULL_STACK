"""Write a recursive function flatten(lst) that converts a nested list into a single flat list. 
Input: lst = [1, [2, 3], [4, [5, 6]], 7] 
Output: [1, 2, 3, 4, 5, 6, 7]"""
"""def flatten(lst,output=[]):
    for i in lst:
        if(type(i)==list):
            flatten(i)
        else:
            output.append(i)
    return(output)

lst=[1, [2, 3], [4, [5, 6]], 7]
print(flatten(lst)) """

"""Write a recursive function nested_sum(lst) that calculates the sum of all numbers present inside a nested list, regardless of the nesting level. 
Input: lst = [1, [2, [3, 4]], [5, [6, [7]]]] Output: 28"""
"""def nested_sum(lst,output=[],sum=0):
    for i in lst:
        if(type(i)==list):
            nested_sum(i)
        else:
            output.append(i)
    for j in output:
        sum=sum+j
    return sum

print(nested_sum([1, [2, [3, 4]], [5, [6, [7]]]]))
"""
"""Write a Python generator function that takes a number n and divides it into 4 equal parts. 
If n is not exactly divisible by 4, add the remaining value only to the last part. 
Input: n = 103 Output: 25 25 25 28"""

"""def generator_n(n):
    i=1
    d=4
    while(i<=d):
        if(n%d==0):
            res=n/d
            yield res
        else:
            if(n%d!=0 and i<=3):
                q=n//d
                yield q
            elif(i==4):
                q=n//d
                r=n-4*q
                res=q+r
                yield res
        i=i+1
n=105
for i in generator_n(n):
    print(i)"""