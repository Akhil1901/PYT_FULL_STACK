"""nums = [[10, 20], [30, 40], [50, 60]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])
"""
"""nums = [[10, 20, 30], [40, 50], [60, 70, 80]]
s=0
for i in range(len(nums)):
    for j in range(len(nums[i])):
        s=s+nums[i][j]
print(s)"""
"""data = [
    [10, 20, 30],
    [5, 50, 15],
    [40, 10, 20],
    [25, 25, 25]
]
maxi_sum=0
row_count=0
for i in data:
    temp=i
    row_count=row_count+1
    max_sum=sum(temp)
    if(max_sum>maxi_sum):
        maxi_sum=max_sum
        a=row_count
print(a)
print(maxi_sum)
"""
"""data = [
    [1, 2, 3, 4],
    [10, 5, 6, 7],
    [2, 4, 6, 8, 10],
    [9, 8, 7, 6]
]"""
"""highest_length=0
for i in data:
    temp=i
    length=0
    for j in temp:
        length=length+1
    if(length>highest_length):
        highest_length=length
        row=temp
print(row)
print(highest_length)"""
"""highest_length=0
for i in data:
    temp=i
    length=0
    for j in range(len(temp)-1):
        if(temp[j+1]>temp[j]):
            length=length+1
        else:
            length=1
    if(length>highest_length):
        highest_length=length
        row=temp
print(highest_length)
print(row)"""

"""data = [
    [10, 20, 30, 40],
    [20, 40, 50, 60],
    [40, 60, 70, 80]
]
y=[]
for i in data:
    y.extend(i)

for i in y:
    count=0
    for j in y:
        if(j==i):
            count=count+1
    if(count==3):
        print(i)
        break
    """

"""data = [
    [10, 20],
    [30, [40, 50]],
    [[60, 70], 80],
    [90, [100, [110, 120]]]
]
y=[]
for i in data:
    temp=i
    for j in temp:
        if(type(j)==int):
            y.append(j)
        if(type(j)==list):
            for k in j:
                if(type(k)==int):
                    y.append(k)
                elif(type(k)==list):
                    y.extend(k)
for i in y:
    print(i)"""



""""how many lists you enter to reach an element."

For this data:

data = [
    [10, 20],
    [30, [40, [50, 60]]],
    [[70, 80], 90]
]"""
"""data = [
    [10, 20],
    [30, [40, [50, 60]]],
    [[70, 80], 90]
]
for i in data:
    first=i
    if()"""

"""Write a Python function to count the number of words that contain at least two vowels.
Input:
Python is easy to learn
Output:
2
Explanation:
Count the words that contain at least two vowels."""

"""para="Python is easy to learn"
li=para.split()
vowels="aeiou"
word_count=0
for i in li:
    temp=str(i.lower())
    count=0
    for i in temp:
        for j in vowels:
            if(i==j):
                count=count+1
    if(count>=2):
        word_count=word_count+1
print(word_count)"""
"""
Write a Python function to find the first character that appears more than once in a string.
Input:
abcaefbd
Output:
a
Explanation:
The character a is the first character that appears more than once"""

"""st = "abcaefbd"
count = 0
for i in st:
    if st[0] == i:
        count +=1
if count>1:
    print(st[0])"""

"""3.Write a Python function to check whether a string contains all unique characters.
Input:
python
Output:
True
Explanation:
Return True if no character appears more than once; otherwise, return False."""


"""def unq_ch(st):
    count=0
    for i in st:
        for j in st:
            if(i==j):
                count=count+1
    if(count==len(st)):
        return True
    else:
        return False

st=input("enter an string: ")
res=unq_ch(st)
print(res)"""

"""Write a Python function to create a new dictionary by assigning a rank to each key based on its value in descending order. The highest value should get rank 1.
Input:
{'A': 85, 'B': 92, 'C': 78, 'D': 88}
Output:
{'B': 1, 'D': 2, 'A': 3, 'C': 4}
Explanation:
Assign ranks based on the values in descending order. The key with the highest value gets rank 1, the next highest gets rank 2, and so on
"""
"""dic={'A': 85, 'B': 92, 'C': 78, 'D': 88}
output={}
output1={}
for i in dic:
    if dic[i]>90:
        output[i]=1
    elif dic[i]>85:
        output[i]=2
    elif dic[i]>80:
        output[i]=3
    else:
        output[i]=4
print(output)
for i in output:
    for j in output:
"""
""".Write a Python function to check whether two lists are rotations of each other.
Input:
[1, 2, 3, 4, 5]
[3, 4, 5, 1, 2]
Output:
True
Explanation:
Return True if one list can be obtained by rotating the other; otherwise, return False."""

"""list1=[1,2,3,4,5]
target=[5,3,4,2,1]
k=int(input("enter the no of rotations : "))
i=0
while(i<=k):
    for i in range(0,len(list1)):
        first=list1[0]
        list1[0]=list1[len(list1)-1]
        list1[len(list1)-1]=first
    i=i+1
if(list1==target):
    print(True)
else:
    print(True)
"""

"""dic = {'A': 85, 'B': 92, 'C': 78, 'D': 88}
output= {}
for i in dic:
    if dic[i] > 90:
        output[i]=1
    elif dic[i]>85:
        output[i] =2
    elif dic[i]>80:
        output[i]=3
    else:
        output[i]=4
li = list(output.items())
#[('A', 3), ('B', 1), ('C', 4), ('D', 2)]
[('B', 1),('A', 3), ('C', 4), ('D', 2)]

for i in range(0,len(li)-1):
    for j in range(0,len(li)-i-1):
        if li[j][1] > li[j+1][1]:#
            li[j],li[j+1] = li[j+1],li[j]
res ={k:v for k,v in li}
print(res) 
print(li)"""

data = [
    [10, 20, 30],
    [5, 15, 25, 35],
    [40, 50],
    [7, 8, 9, 10, 11]
]

for i in data:
    temp=data
    for j in range(len(temp)):
        if(temp[j+1]>temp[j]):
            
