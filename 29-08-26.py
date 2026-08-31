"""data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
for i in data:
    for j in range(len(i)):
        print(i[j])
"""
"""data = [
    [10, 20, 30],
    [40, 50],
    [60, 70, 80, 90]
]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j])"""

"""data = [
    [10, 25, 30],
    [45, 50],
    [60, 15, 80]
]
count=0
for i in range(len(data)):
    for j in range(len(data[i])):
        if(data[i][j]>40):
            count=count+1
print(count)"""

"""data = [
    [10, 20],
    [30, 40, 50],
    [60, 70]
]
sum=0
for i in data:
    for j in range(len(i)):
        sum=sum+i[j]
print(sum)"""

"""data = [
    {"name": "Ravi", "age": 22},
    {"name": "Anu", "age": 25},
    {"name": "Kiran", "age": 21}
]
for i in range(len(data)):
    print(data[i]['name'])"""

"""data = [
    {"name": "Ravi", "age": 22},
    {"name": "Anu", "age": 25},
    {"name": "Kiran", "age": 21},
    {"name": "Meena", "age": 27}
]
sum=0
for i in range(len(data)):
    sum=sum+data[i]['age']

avg=sum//len(data)
print(avg)
"""
"""data = [
    {"name": "Ravi", "marks": [80, 70, 90]},
    {"name": "Anu", "marks": [60, 85, 75]},
    {"name": "Kiran", "marks": [90, 95, 88]}
]
for i in range(len(data)):
    total =sum(data[i]['marks'])
    print(data[i]['name'],":",total)"""

"""data = [
    {"name": "Ravi", "marks": [80, 70, 90]},
    {"name": "Anu", "marks": [60, 85, 75]},
    {"name": "Kiran", "marks": [90, 95, 88]}
]
"""
"""for i in data:
    list=i['marks']
    highest=0
    for j in list:
        if(j>highest):
            highest=j
    print(i['name'],":",highest)"""

"""data = [
    {
        "name": "Ravi",
        "marks": {"math": 80, "science": 70, "english": 90}
    },
    {
        "name": "Anu",
        "marks": {"math": 60, "science": 85, "english": 75}
    },
    {
        "name": "Kiran",
        "marks": {"math": 90, "science": 95, "english": 88}
    }
]"""

"""for i in data:
    total=0
    for j in i["marks"]:
        total=total+i["marks"][j]
    print(i['name'],":",total)"""

"""data = [
    {
        "name": "Ravi",
        "subjects": {
            "math": [80, 85],
            "science": [70, 75]
        }
    },
    {
        "name": "Anu",
        "subjects": {
            "math": [60, 65],
            "science": [85, 90]
        }
    }
]"""
"""for i in data:
    total=0
    for j in  i["subjects"]:
        for k in i["subjects"][j]:
            total=total+k
    print(i["name"],":",total)"""

data = [
    {
        "name": "Ravi",
        "subjects": {
            "math": [80, 85],
            "science": [70, 75]
        }
    },
    {
        "name": "Anu",
        "subjects": {
            "math": [60, 65],
            "science": [85, 90]
        }
    }
]
"""for i in data:
    highest=0
    for j in i["subjects"]:
        for k in i["subjects"][j]:
            if(k>highest):
                highest=k
                name=i["name"]
                subjects=j
    print(name,":",subjects)"""

"""data = [
    {
        "name": "Ravi",
        "subjects": {
            "math": [
                {"exam": "mid", "mark": 80},
                {"exam": "final", "mark": 90}
            ],
            "science": [
                {"exam": "mid", "mark": 70},
                {"exam": "final", "mark": 85}
            ]
        }
    },
    {
        "name": "Anu",
        "subjects": {
            "math": [
                {"exam": "mid", "mark": 75},
                {"exam": "final", "mark": 88}
            ],
            "science": [
                {"exam": "mid", "mark": 82},
                {"exam": "final", "mark": 95}
            ]
        }
    }
]  
for i in data:
    highest=0
    for j in i["subjects"]:
        for k in i["subjects"][j]:
            if(k["mark"]>highest):
                highest=k["mark"]
                name=i["name"]
    print(name,":",highest)"""


"""data = [
    (10, 20, 30),
    (40, 50),
    (60, 70, 80)
]
for i in data:
    for j in i:
        print(j)"""

