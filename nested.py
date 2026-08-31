"""employees = {
    "IT": [
        ("teja", 45000),
        ("ravi", 55000),
        ("kiran", 48000)
    ],
    "HR": [
        ("anil", 52000),
        ("suresh", 47000)
    ],
    "Sales": [
        ("mahesh", 60000),
        ("raju", 58000)
    ]
}
large=0
for i in employees:
    for j in range(len(employees[i])):
        if(employees[i][j][1]>large):
            large=employees[i][j][1]
            a=employees[i][j]
print(large)
print(a)"""

company = {
    "Python": {
        "teja": [80, 85, 90],
        "ravi": [70, 75, 80]
    },
    "Java": {
        "kiran": [90, 95, 92],
        "anil": [60, 70, 65]
    }
}

"""high_avg=0
for i in company:
    for j in company[i]:
        res=0
        for k in range(len(company[i][j])):
            res=res+company[i][j][k]
        avg=res//len(company[i][j])
        if(avg>high_avg):
            high_avg=avg
print(high_avg)
"""


