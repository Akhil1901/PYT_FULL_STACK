""" 1. Write a Python program to insert the square of every odd number immediately after it in the same list.
Input:
Enter the list: [3, 4, 5, 8, 7]
Output:
[3, 9, 4, 5, 25, 8, 7, 49] """

list=[3,4,5,8,7]
i=0
while(i<len(list)):
    if(list[i]%2!=0):
    
    i=i+1