"""Write a Python program using a decorator to display a message before and after executing the function. 
Input: hello batch 89 
Output: Function Started 
hello batch 89 
Function Ended"""

"""def before_after(fun):
    def innerfun():
        print("Function started")
        fun()
        print("Function Ended")
    return innerfun

@before_after
def middle():
    print("hello batch89")

middle()"""

"""Write a Python program using a decorator to count the number of times a function is called. 
Input: hello() hello() hello() 
Output: Call 1: hello Call 2: hello Call 3: hello"""

"""def count(fun):
    count=0
    def innerfun():
        nonlocal count
        count=count+1
        print(f"Call {count}: ",end="")
        fun()
    return innerfun

@count
def greet():
    print("hello")

greet()
greet()
greet()"""

"""Write a Python program using a decorator to display a message before adding two numbers. 
Input: n1 = 10 n2 = 20 
Output: Adding 10 and 20 Sum = 30
"""
"""def outer(fun):
    def innerfun(a,b):
        res=fun(a,b)
        ans=f"Adding {a} and {b} sum = {res}"
        return ans
    return innerfun
@outer
def numbers(a,b):
    return a+b
print(numbers(10,20))"""

"""Write a Python program using a decorator to multiply the return value of a function by 2.
Input: calculate(5) 
Output: Original Result: 5 
Final Result: 10"""

"""def outer(fun):
    def innerfun(n):
        x=fun(n)
        ans=x*2
        print(f"Original result :{n} Final result:{ans}")
    return innerfun

@outer
def calculate(n):
    return n

calculate(5)"""



