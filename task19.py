"""1.Write a Python program to create a new tuple by inserting the index of every element immediately after it.
Input:
(10, 20, 30, 40)
Output:
(10, 0, 20, 1, 30, 2, 40, 3)
Explanation:
Create a new tuple by inserting the index of each element immediately after that element."""

tu=(10,20,30,40)
output=[i    for i in tu ]
for i in tu:
    idx=tu.index(i)
    output.append(i)
    output.append(idx)
print(tuple(output))

""".Write a Python program to create a new tuple by repeating every element according to its position.
Input:
(10, 20, 30, 40)
Output:
(10, 20, 20, 30, 30, 30, 40, 40, 40, 40)
Explanation:
Repeat the element at index 0 once, index 1 twice, index 2 three times, and so on.
"""
"""tple=(10,20,30,40)
output=[]
for i in tple:
    idx=tple.index(i)
    j=0
    while(j<=idx):
        output.append(i)
        j=j+1
print(tuple(output))"""

"""3.Write a Python program to create a new tuple by inserting the sum of digits of every element immediately after that element.
Input:
(12, 35, 101)
Output:
(12, 3, 35, 8, 101, 2)
Explanation:
Insert the sum of digits of each element immediately after that element."""

""" tple=(12,35,101)
output=[]
for i in tple:
    number=i
    sum=0
    while(number>0):
        digit=number%10
        sum=sum+digit
        number=number//10
    output.append(i)
    output.append(sum)
print(tuple(output)) """

"""Write a Python program to create a new tuple containing only those elements that are greater than the average of the tuple.
Input:
(10, 25, 15, 30, 20)
Output:
(25, 30)
Explanation:
Average = 20. Create a new tuple containing only the elements greater than the average."""

""" tple=(10,25,15,30,20)
output=[i for i in tple if i>sum(tple)//len(tple)]
print(tuple(output)) """

"""5.Write a Python program to create a new tuple by replacing every even-index element with its square and every odd-index element with its cube.
Input:
(2, 3, 4, 5, 6)
Output:
(4, 27, 16, 125, 36)
Explanation:
* Even index → Square the element.
* Odd index → Cube the element."""

""" tple=(2,3,4,5,6)
output=[i**2 if tple.index(i)%2==0 else i**3 for i in tple ]
print(tuple(output)) """


