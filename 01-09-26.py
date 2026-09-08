"""x=[10,20,30,40,50]
print(x)"""
"""x=[10,20,30,40]
x.append(50)
print(x)"""
"""x=[10,20,30,40,50]
sum=0
for i in x:
    sum=sum+i
print(sum)"""
"""x=[12,45,7,89,23]
n=0
for i in x:
    if(i>n):
        n=i
print(n)"""

"""def outerfun():
    print("chiranjeevi")
    def innerfun():
        print("balayya")
        return
    return innerfun
fun=outerfun()
print(fun)
fun()"""

"""Write a Python program using a closure where the outer function takes a number n
and the inner function takes another number x and returns n + x. 
Input: n = 10 x = 5 
Output: 15"""
"""def outer_func(n):
    def inner_func(x):
        return n+x
    return inner_func
fun=outer_func(10)
res=fun(5)
print(res)"""

"""Create a closure counter() that maintains a count. 
Every time the inner function is called, it should increase the count by 1 
and return the updated count.
Input: c = counter() print(c()) print(c()) print(c()) Output: 1 2 3"""

"""def counter():
    count=0
    def innerfun():
        nonlocal count
        count=count+1
        return count
    return innerfun
c=counter()
res=c()
print(res)
res1=c()
print(res1)
res3=c()
print(res3)"""

"""Write a closure that stores a number and provides an inner function to increase the stored number by a given value. 
Input: c = create_counter(10) print(c(5)) print(c(3)) print(c(7)) 
Output: 15 18 25"""

"""def create_counter(n):
    count=n
    def inner_fun(x):
        nonlocal count
        count=count+x
        return count
    return inner_fun
c=create_counter(10)
print(c(5))
print(c(3))
print(c(7))"""

"""data = [[10, 20], [30, 40], [50, 60]]

for i in data:
    for j in i:
        print(j)"""
"""data = [[10, 20], [30, 40], [50, 60]]
sum=0
for i in data:
    for j in i:
        sum=sum+j
print(sum)"""
data = {
    "student1": {
        "name": "Akhil",
        "age": 25
    },
    "student2": {
        "name": "Rahul",
        "age": 24
    }
}
"""for i in data:
        print(data[i]['name'],":",data[i]['age'])"""

"""data = {
    "student1": {
        "name": "Akhil",
        "marks": {
            "python": 90,
            "sql": 80
        }
    },
    "student2": {
        "name": "Rahul",
        "marks": {
            "python": 85,
            "sql": 75
        }
    }
}
for i in data:
    for j in data["marks"]:
        for k in j:
            print()"""
"""def outerfun(fun):
    def innerfun():
        print("*"*40)
        print(fun())
        print("*"*40) 
    return innerfun

@outerfun
def display():
    s="welcome to vcube"
    return s

display()
"""
"""def log(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print(add(5, 3))"""

"""def welcome(func):
    def innerfun():
        print("welcome to python")
        func()
        print("thank you")
    return innerfun
@welcome
def hello():
    print("Hello")

hello()
"""
"""data = {
    "A": [
        {"name": "Ravi", "marks": (80, 90)},
        {"name": "Anu", "marks": (70, 85)}
    ],
    "B": [
        {"name": "Kiran", "marks": (95, 88)}
    ]
}
for i in data:
"""

"""def add_five(fun):
    def innerfun(a,b):
        fun(a,b)
        return fun(a,b)+5
    return innerfun

@add_five
def calculate(a,b):
    return a+b

print(calculate(10,20))"""

"""def double_result(fun):
    def innerfun(a,b):
        result = fun(a,b)
        return result*2
    return innerfun

@double_result
def multiply(a,b):
    return a*b
print(multiply(10,20))"""

"""def check_positive(fun):
    def innerfun():
        result=fun()
        if(result>0):
            print(result)
            print("positive")
    return innerfun

@check_positive
def number():
    return 10
number()"""

"""def check_result(fun):
    def innerfun(a,b):
       res = fun(a,b)
       if(res>0):
           print("positive")
       else:
            print("negavtive")
       return res
    return innerfun

@check_result
def subtract(a, b):
    return a - b

print(subtract(5,10))"""

"""def make_positive(fun):
    def innerfun(a,b):
        res=fun(a,b)
        if(res<0):
            ans=-1*res
            res=ans
        return res
    return innerfun


@make_positive
def subtract(a, b):
    return a - b

print(subtract(5, 10))
"""
"""def square_result(fun):
    def innerfun(a,b):
        res=fun(a,b)
        return res**2
    return innerfun

@square_result
def add(a, b):
    return a + b

print(add(3, 2))

"""



@modify_result
def multiply(a, b):
    return a * b




