""".Write a Python program to group all keys having the same value into a list.
Input:
d = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
Output:
{10: ['a', 'c', 'f'],20: ['b', 'e'],30: ['d']}"""
"""d={"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
output={}
for i in d:
    if d[i] not in output:
        output[d[i]]=[i]
    else:
        output[d[i]].append(i)
print(output)
"""
"""Write a Python program to arrange the dictionary in ascending order of values without using the built-in sorted() function.
Input:
d = {"A": 45,"B": 12,"C": 78,"D": 30,"E": 56}
Output:
{"B": 12,"D": 30,"A": 45,"E": 56,"C": 78}"""
"""d={"A":45,"B":12,"C":78,"D":30,"E":56}
li = list(d.items())
for i in range(0,len(d)-1):
    for j in range(0,len(d)-i-1):
        if(li[j][1]>li[j+1][1]):
            li[j+1],li[j]=li[j],li[j+1]
output={k:v for k,v in li}
print(output)"""
""".Write a Python program to find all keys whose values are prime numbers.
Input:
d = {"a": 12,"b": 17,"c": 23,"d": 25,"e": 31}
Output:
['b', 'c', 'e']"""

"""d = {"a": 12,"b": 17,"c": 23,"d": 25,"e": 31}
output=[]
for k,v in d.items():
    prime=v
    i=1
    count=0
    while(i<=prime):
        if(prime%i==0):
            count=count+1
        i=i+1   
    if(count==2):
        output.append(k)
    
print(output)"""

""".Write a Python program to find the row whose sum is maximum in a nested list. If two rows have the same sum, consider the first one.
Input:
x = [ [10, 20, 5],[15, 8, 12],[25, 5, 10],[7, 18, 20] ]
Output:
[7, 18, 20]
Sum: 45"""
""" x = [ [10, 20, 5],[15, 8, 12],[25, 5, 10],[7, 18, 20] ]
s=0
for i in x:
    temp=i
    s1=sum(temp)
    if(s1>s):
        s=s1
        a=temp
print(a) """

"""5.Write a Python program to remove duplicate tuples from a nested tuple while maintaining the original order.
Input:
x = ((1, 2),(3, 4),(1, 2),(5, 6),(3, 4),(7, 8))
Output:
((1, 2), (3, 4), (5, 6), (7, 8))"""
x = ((1, 2),(3, 4),(1, 2),(5, 6),(3, 4),(7, 8))
output=[]
for i in x:
    for j in x:
        if(i==j):
            if(i not in output):
                output.append(i)
print(tuple(output))