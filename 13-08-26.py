"""num=[10,20,30,20,40,10,50]
print(set(num))
"""
"""num=(10,20,30,40,50)
print(list(num))"""

"""num=(10,15,20,25,30)
out=[]
target=5
new_tuple=()
for i in num: 
    difference=0
    for j in num:
        difference=j-i
        if(difference==target):
            new_tuple=(i,j)
    if new_tuple not in out:
        out.append(new_tuple)
print(out)"""

"""num=(2, 7, 11, 15, 3, 8)
out=[]
target=10
new_tuple=()
for i in num:
    sum=0
    for j in num:
        sum=i+j
        if(sum==target):
            new_tuple=(i,j)
    if new_tuple not in out:
        out.append(new_tuple)
print(out)"""

"""num=[[1,2],[3,4],[5,6]]
temp_list=[]
out=[]
for i in num:
    temp_list=i
    j=0
    while(j<=len(temp_list)-1):
        element=temp_list[j]
        out.append(element)
        print(out)
        j=j+1"""

"""matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
out=[]
for i in range(0,1):
    temp=matrix[i]
    for j in range(1,2):
        temp2=matrix[j]
        k=0
        while(k<len(temp)):
            new_list=[temp[k],temp2[k]]
            out.append(new_list)
            k=k+1
print(out)"""

"""numbers = (10, 20, 30, 40, 50)

for i in numbers:
    print(i)
"""

  
























