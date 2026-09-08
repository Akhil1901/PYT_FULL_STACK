"""def welcome(fun):
    def innerfun():
        print("welcome")
        fun()
    return innerfun

@welcome
def hello():
    print("hello")

hello()"""
"""
def message(fun):
    def innerfun():
        print("Start")
        fun()
        print("End")
    return innerfun

@message
def test():
    print("Testing")

test()"""

"""def add_five(fun):
    def innerfun():
        res=fun()
        return res+5
    return innerfun
@add_five
def number():
    return 10

print(number())
"""
"""def double_result(fun):
    def innerfun():
        res=fun()
        return res*2
    return innerfun

@double_result
def number():
    return 8

print(number())"""

"""def add_ten(fun):
    def innerfun(a,b):
        res=fun(a,b)
        return res+10
    return innerfun

@add_ten
def add(a, b):
    return a + b

print(add(10, 20))"""

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

print(subtract(5, 15))"""

"""def check_result(fun):
    def innerfun(a,b):
        res=fun(a,b)
        if(res>0):
            print("positive")
        else:
            print("negavtive")
        return res
    return innerfun

@check_result
def subtract(a, b):
    return a - b

print(subtract(2,10))"""



"""def show_arguments(fun):
    def innerfun(a,b):
        res=fun(a,b)
        print(f"a={a}")
        print(f"b={b}")
        return res
    return innerfun

@show_arguments
def add(a, b):
    return a + b

print(add(10,20))
"""

"""def show_args(fun):

    def innerfun(*args):
        print(args)

        res = fun(*args)

        return res

    return innerfun

@show_args
def add(a, b, c):
    return a + b + c

print(add(10, 20, 30))"""

"""def show_args(fun):
    def innerfun(*args):
        print(args)
        res=fun(*args)
        return res
    return innerfun

@show_args
def multiply(*args):
    result = 1

    for i in args:
        result = result * i

    return result

print(multiply(2, 3, 4))"""

"""def discount(fun):
    def innerfun():
        original_price=fun()
        discount=(20/100)*original_price
        final=original_price-discount
        return final
    return innerfun

@discount
def price():
    return 1000

print(price())"""

"""def add_five(fun):
    def innerfun(*args):
        res=fun(*args)
        ans=res+5
        return ans
    return innerfun
def double(fun):
    def inner_fun(*args):
        res=fun(*args)
        return res*2
    return inner_fun

def subtract_three(fun):
    def innerfun(*args):
        res=fun(*args)
        return res-3
    return innerfun

@subtract_three
@double
@add_five
def calculate(a, b):
    return a + b

print(calculate(10, 20))"""


"""def number(n):
    i=1
    while(i<=n):
        yield i
        i=i+1

n=10
for i in number(n):
    print(i)"""
"""data = {
    "A": [
        {"name": "Ravi", "marks": (80, 90)},
        {"name": "Anu", "marks": (70, 85)}
    ],
    "B": [
        {"name": "Kiran", "marks": (95, 88)}
    ]
}
for key in data.keys():
    for j in range(len(data[key])):
        for l in data[key][j]["marks"]:
            print(key, data[key][j]["name"], l)"""

"""data = [
    {
        "A": (
            [10, 20],
            [30, 40]
        )
    },
    {
        "B": (
            [50, 60, 70],
            [80, 90]
        )
    }
]
for i in data:
    for key,values in i.items():
        for j in values:
            for k in range(len(j)):
                print(key,j[k])
"""

"""def generator_even(n):
    i=1
    while(i<=n):
        if(i%2==0):
            yield i
        i=i+1

n=10
for i in generator_even(n):
    print(i)
"""
"""def genartor_numbers(n):
    i=1
    while(i<=n):
        if(i%3==0):
            yield i
        i=i+1
n=15
for i in genartor_numbers(n):
    print(i)"""
"""def generator_list(data):
    for i in data:
        yield i

data = [10, 20, 30, 40, 50]

for i in generator_list(data):
    print(i)"""
"""data = "PYTHON"
def generate_python(data):
    for i in data:
        yield i

for i in generate_python(data):
    print(i)"""

data = [10, 15, 20, 25, 30, 35, 40]
def generate_even(data):
    for i in data:
        if(i%2==0):
            yield i

for i in generate_even(data):
    print(i)