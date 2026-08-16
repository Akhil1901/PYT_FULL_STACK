"""numbers=[10,20,30,40,50,60]
middle=len(numbers)//2
print(numbers[middle])"""

"""numbers=[10,20,30,40,50]
numbers[4]=500
print(numbers)"""
"""Swap the first and last elements of this list:

numbers = [10, 20, 30, 40, 50]"""

"""numbers=[10,20,30,40,50]
pointer=0
temp=0
for i in range(0,len(numbers)):
    pointer=numbers[0]
    if(i==len(numbers)-1):
        temp=numbers[i]
        numbers[i]=pointer
        numbers[0]=temp
print(numbers)
"""
"""Swap the second and fourth elements.

numbers = [10, 20, 30, 40, 50]

Write only the code"""

"""numbers=[10,20,30,40,50]

second=numbers[1]
fourth=numbers[3]
numbers[1]=fourth
numbers[3]=second
print(numbers)"""
"""
nums=[10,20,30,40,50]
for i in range(len(nums)-1,-1,-1):
    print(nums[i])"""

"""n=int(input("enter how many rotations  do you want to do : "))
nums=[10,20,30,40,50]
i=0
while(i<n):
    temp=0
    
    for j in range(len(nums)-1,-1,-1):
        temp=nums[len(nums)-1]

        if(j==0):
            nums.remove(temp)
            nums.insert(0,temp)
    
    i=i+1
print(nums)"""
"""Print the element before the last element of this list.

numbers = [10, 20, 30, 40, 50]

⚠️ Don't count the elements manually.

Use a pointer (index)."""
"""nums=[10,20,30,40,50]
for i in range(0,len(nums)):
    temp=nums[i]
    if(i==len(nums)-1):
        print(nums[i-1])
"""

"""Print the second-to-last element using a negative index.

nums = [15, 25, 35, 45, 55, 65]

Write only the code."""
"""nums = [15, 25, 35, 45, 55, 65]
print(nums[-5:-1:1])"""

x=frozenset([10,'vcube',True,10])
y=frozenset([20,'python',1])
print(x|y)
print(x&y)