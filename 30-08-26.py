"""data = [
    (10, 20, 30),
    (40, 50),
    (60, 70, 80)
]
for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j])"""

"""data = (
    [10, 20],
    [30, 40, 50],
    [60, 70]
)
for i in data:
    for j in i:
        print(j)"""

"""data = [
    {"name": "Ravi", "age": 22},
    {"name": "Anu", "age": 25},
    {"name": "Kiran", "age": 21}
]
for i in data:
    for j in i:
        print(j,":",i[j])"""

"""data = {
    "A": [10, 20, 30],
    "B": [40, 50],
    "C": [60, 70, 80]
}
for k,v in data.items():
    for j in v:
        print(k,":",j)

"""
"""data = [
    ("A", [10, 20]),
    ("B", [30, 40, 50]),
    ("C", [60, 70])
]
for i in range(len(data)):
    for j in data[i][1]:
        print(j)"""

"""data = [
    {"name": "Ravi", "marks": [80, 90]},
    {"name": "Anu", "marks": [70, 85]},
    {"name": "Kiran", "marks": [95, 88]}
]
for i in data:
    for k in i["marks"]:
        print(i["name"], ":", k)"""
"""
data = [
    ("A", {"x": 10, "y": 20}),
    ("B", {"x": 30, "y": 40}),
    ("C", {"x": 50, "y": 60})
]
for i in data:
    for j in i[1]:
        print(i[0],j,i[1][j])"""

"""data = (
    {"name": "Ravi", "marks": [80, 90]},
    {"name": "Anu", "marks": [70, 85]},
    {"name": "Kiran", "marks": [95, 88]}
)
for i in data:
    for j in i["marks"]:
        print(i["name"],":",j)"""


"""data = (
    [
        {"name": "Ravi", "age": 22},
        {"name": "Anu", "age": 25}
    ],
    [
        {"name": "Kiran", "age": 21},
        {"name": "Meena", "age": 27}
    ]
)
for i in data:
    for j in i:
        print(j['name'],":",j['age'])"""
print("abc" == "abc")
print("abc" != "xyz")
print("abc" < "xyz")