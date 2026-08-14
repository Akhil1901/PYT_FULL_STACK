"""numbers = [10, 25, 30, 45, 50, 65, 70]
sum=0
for i in numbers:
    if(i%2==0):
        sum=sum+i
print(sum)"""

"""numbers = [10, 25, 30, 45, 50, 65, 70]
sum=0
for i in numbers:
    if(i%2!=0):
        sum=sum+i
print(sum)"""

"""numbers = [25, 10, 45, 5, 30]
largest=0
for i in numbers:
    if(i>largest):
        largest=i
print(largest)
"""
"""output=[i**2 for i in list]"""
"""output=[i for i in list if i%2==0]"""

"""numbers = [10, 20, 10, 30, 20, 40, 10]
output=[]
for i in numbers:
    if i in output:
        continue
    else:
        output.append(i)
print(output)"""

"""numbers = [10, 20, 30, 40, 50]
output=[]
for i in range(len(numbers)-1,-1,-1):
    output.append(numbers[i])
print(output)"""

"""Find the elements that occur more than once."""
"""numbers = [5, 2, 8, 2, 9, 5, 1, 8, 3]
output=[]

for i in numbers:
    count=0
    for j in numbers:
        if(i==j):
            count=count+1
    if(count>1):
        if i not in output:
            output.append(i)
print(output)"""














