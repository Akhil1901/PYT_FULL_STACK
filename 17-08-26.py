"""student={
    "name":"akhil",
    "age" : 20,
    "city":"Hyd"
}
for k,v in student.items():
    print(k , v)"""
"""marks={
    "math":85,
    "science":90,
    "English":78
}
for v in marks.values():
    print(v)"""
"""employee={
    "name":"Ravi",
    "Salary":5000,
    "departement":"cse"
}
for i in employee:
    print(i)"""

"""products={
    "laptop":5000,
    "mouse":500,
    "keyboard":1500
}
for k,v in products.items():
    print(k)"""
"""books={
    "python":500,
    "Java":600,
    "c":400
}
for _,v in books.items():
    if(v>450):
        print(v)"""
"""students={
    "Akhil":85,
    "Ravi":72,
    "Ram":91,
    "John":68
}
for k,v in students.items():
    if(v>=80):
        print(k)"""

"""employees={
    "akhil":50000,
    "ravi":45000,
    "Ram":60000,
    "jhon":40000,
}
sum=0
for k,v in employees.items():
    sum=sum+v
print(sum)"""

fruits={
    "apple":120,
    "banana":60,
    "orange":90,
    "mango":150
}
"""count=0
for i,j in fruits.items():
    if(j>100):
        count=count+1
print(count)"""
"""movies={
    "A":8,
    "B":9,
    "C":7,
    "D":10
}
for i,j in movies.items():
    if(j>=9):
        print(i)"""

"""products={
    "laptops":50000,
    "Mouse":500,
    "keyboard":1500,
    "monitor":12000
}
sum=0
count=0
for i,j in products.items():
    sum=sum+j
    count=count+1
avg=sum/count
print(avg)"""

"""cities = {
    "Hyderabad": 12000000,
    "Mumbai": 20000000,
    "Delhi": 19000000,
    "Chennai": 11000000
}
largest=0
for k,v in cities.items():
    if(v>largest):
        largest=v
        a=k
print(a)"""

"""students = {
    "Akhil": 85,
    "Ravi": 72,
    "Ram": 91,
    "John": 68
}
lowest=100
for k,v in students.items():
    if(v<lowest):
        lowest=v
        a=k
print(a)"""

"""employees = {
    "Akhil": 50000,
    "Ravi": 45000,
    "Ram": 60000,
    "John": 40000
}
count=0
for v in employees.values():
    if(v>=45000 and v<=60000):
        count=count+1
print(count)"""

"""inventory = {
    "Pen": 25,
    "Book": 10,
    "Pencil": 40,
    "Eraser": 15
}

for k,v in inventory.items():
    if(v<20):
        a=k
        print(a)"""


"""marks={
    "math":85,
    "science":92,
    "English":78,
    "physics":88
}
count=0
for i,j in marks.items():
    if(j>=85):
        count=count+1
print(count)"""


"""scores = {
    "Akhil": 85,
    "Ravi": 72,
    "Ram": 91,
    "John": 68
}
for i,j in scores.items():
    if(j<80):
        print(i,":",j)"""

"""sales = {
    "January": 5000,
    "February": 7000,
    "March": 6000,
    "April": 8000
}
largest=0
second=0
for i,j in sales.items():
    if(j>largest):
        largest=j
    elif(j>second and j<largest):
        second=j
        print(i)"""
"""players = {
    "Akhil": 85,
    "Ravi": 72,
    "Ram": 91,
    "John": 68,
    "Sam": 95
}
sum=0
count=0
for k,v in players.items():
    sum=sum+v
    count=count+1
avg=sum//count
for k,v in players.items():
    if(v>avg):
        print(k)"""
