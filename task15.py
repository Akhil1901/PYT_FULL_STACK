""".Write a Python program to print all elements that are greater than both of their adjacent elements.
Input:
[5, 18, 10, 25, 15, 30, 20]
Output:
18 25 30"""

"""list=[5,18,10,25,15,30,20]
i=0
while(i<(len(list)-1)):
    element=list[i]
    next_element=list[i+1]
    if(next_element>element):
        print(next_element)
    i=i+1"""

"""2.Write a Python program to print all elements in a list that are equal to the sum of all previous elements.
Input:
[2, 3, 5, 10, 20, 21]
Output:
5 10 20
Explanation:
5 = 2 + 3
10 = 2 + 3 + 5
20 = 2 + 3 + 5 + 10"""

"""list=[2,3,5,10,20,21]
sum=0
for i in list:
    if sum==i:
        print(i)
    sum=sum+i"""

"""Write a Python program to split a list into groups of 3 elements using slicing and print only the groups whose sum is greater than 50.
Input:
[10, 20, 30, 5, 10, 15, 25, 20, 15]
Output:
[10, 20, 30]
[25, 20, 15]"""
"""
list=[10,20,30,5,10,15,25,20,15]
"""

""".Write a Python program using List Comprehension to create a new list containing the square of all even numbers.
Input:
[2, 3, 4, 5, 6, 7]
Output:
[4, 16, 36]"""


"""list=[2,3,4,5,6,7]
output=[]
for i in list:
    if(i%2==0):
        square=i**2
        output.append(square)

print(output)"""

"""Write a Python program using List Comprehension to create a new list containing the squares of the numbers that are divisible by 5.
Input:
[5, 8, 10, 12, 15, 18, 20]
Output:
[25, 100, 225, 400]"""

"""list=[5,8,10,15,18,20]
output=[]
for i in list:
    if(i%5==0):
        square=i**2
        output.append(square)

print(output)"""

"""Write a Python program using List Comprehension to create a new list containing only the perfect square numbers from the given list.
Input:
[4, 7, 9, 10, 16, 18, 25]
Output:
[4, 9, 16, 25]"""

"""list=[4,7,9,10,16,18,25]
output=[]
for i in list:
    root=i**0.5
    print(root)
    square=root**2
    print(square)
    if(square==i):
        output.append(i)
print(output)
""" 
"""Write a Python program using List Comprehension to create a new list containing the cubes of all odd numbers.
Input:
[2, 3, 4, 5, 6, 7]
Output:
[27, 125, 343]"""

list=[2,3,4,5,6,7]
for i in list:
    if(i%2!=0):
        

