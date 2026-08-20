"""student = {
    "name": "Akhil",
    "age": 20,
    "city": "Hyderabad"
}
print(student['city'])
"""
"""car = {
    "brand": "Toyota",
    "year": 2025,
    "price": 1500000
}
print(car['brand'])
print(car['price'])"""
"""
employee = {
    "name": "Ravi",
    "salary": 50000,
    "department": "IT"
}
print(employee['name'],"works in", employee['department'])"""
"""marks = {
    "Math": 85,
    "Science": 92,
    "English": 78
}
total=0
for  i in marks:
    total= total+marks[i]
print(total)"""

"""products = {
    "Pen": 10,
    "Book": 25,
    "Pencil": 15,
    "Eraser": 5
}
for i in products:
    if(products[i]>10):
        print(i)"""
"""scores = {
    "Akhil": 85,
    "Ravi": 72,
    "Ram": 91,
    "John": 68
}
highest=0
for i in scores:
    if(scores[i]>highest):
        highest=scores[i]
        name=i
print(name)"""

"""inventory = {
    "Pen": 10,
    "Book": 25,
    "Pencil": 15,
    "Eraser": 5,
    "Marker": 30
}
s=0
c=0
for i in inventory:
    s=s+inventory[i]
    c=c+1
avg=s//c
print(avg)"""

"""Write a Python program to group all keys having the same value into a list.
Input:
d = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
Output:
{10: ['a', 'c', 'f'],20: ['b', 'e'],30: ['d']}"""
"""d = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
output={}
for i in d:
    key=d[i]
    temp=[]
    for j in d:
        if(key==d[j]):
            temp.append(j)
    if key not in output:
        output[key]=temp
print(output)"""

"""Count how many digits are equal to 0.

Example:

Input: 1020304
Output: 3"""
"""num=1020304
temp=num
org=num
count=0
while(num>0):
    digit=num%10
    if(digit==0):
        count=count+1
    num=num//10
print(count)"""

"""Find the largest digit in a number.

Example:

Input: 5832741

Output:

8"""
"""num=5832741
largest=0
while(num>0):
    digit=num%10
    if(digit>largest):
        largest=digit
    num=num//10
print(largest)"""
"""Count how many digits are greater than their previous digit (from right to left).

Example:

Input: 527486

Compare the digits from right to left:

6 → no previous digit
8 > 6  ✓
4 > 8  ✗
7 > 4  ✓
2 > 7  ✗
5 > 2  ✓

Output:

3"""
"""num=527486
previous=0
count=0
while(num>0):
    digit=num%10
    if(previous>0):
        if(digit>previous):
            count+=1
    previous=digit
    num=num//10
print(count)"""

"""Find the first digit that is repeated consecutively (from right to left).

Example:

Input: 1233445

Digits from right to left:

5, 4, 4, 3, 3, 2, 1

The first consecutive repetition is:

4, 4

Output:

4"""
"""num=1233445
previous_digit=0
while(num>0):
    next_digit=num%10
    if(previous_digit==next_digit):
        print(next_digit)
        break
    previous_digit=next_digit
    num=num//10
"""
"""Find the longest sequence of consecutive even digits.

Example:

Input: 124688913

Sequences of even digits:

2, 4, 6, 8, 8 → length = 5

Output:

5
"""
"""num=124688913
previous_digit=0
current_length=0
max_length=0
while(num>0):
    digit=num%10
    if(previous_digit>0):
        if(digit%2==0 and previous_digit%2==0):
            current_length+=1
        else:
            current_length=0
    if(current_length>max_length):
        max_length=current_length
    previous_digit=digit
    num=num//10
print(max_length)"""




