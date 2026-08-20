""".Write a Python program to count the frequency of each element in a list using a dictionary.
Input:
[1, 2, 3, 2, 1, 2, 4]
Output:
{1: 2, 2: 3, 3: 1, 4: 1}"""
"""num=[1,2,3,2,1,2,4]
output={}

for i in num:
    if i in output:
        output[i]+=1
    else:
        output[i]=1
print(output)"""

"""Write a Python program to find the key having the highest value in a dictionary.
Input:
{"a": 10, "b": 25, "c": 15, "d": 30}
Output:
d"""

"""fict={"a": 10, "b": 25, "c": 15, "d": 30}
large=0
for key in fict:
    if fict[key]>large:
        large=fict[key]
        a=key
print(a)
"""
"""
Write a Python program to calculate the sum of all values in a dictionary without using sum().
Input:
{"a": 10, "b": 20, "c": 30}
Output:
60"""
"""a={"a":10,"b":20,"c":30}
sum=0
for key in a:
    sum=sum+a[key]
print(sum)"""
"""Write a Python program to count the occurrence of each character in a string using a dictionary.
Input:
programming
Output:
{"p": 1, "r": 2, "o": 1, "g": 2, "a": 1, "m": 2, "i": 1, "n": 1}"""

"""str1="programming"
output={}
for i in str1:
    if i in output:
        output[i]+=1
    else:
        output[i]=1
print(output)"""


"""Write a Python program to find the key and value whose value is the second highest in a dictionary.
Input:
{"A": 80, "B": 95, "C": 70, "D": 90}
Output:
D-90"""
"""m={"A":80,"B":95,"C":70,"D":91zxd}
large=0
second=0
for i in m:
    if(m[i]>large):
        large=m[i]
    elif(m[i]>second and m[i]<large):
        second=m[i]
        a=i
print(a,"-",second)""" 