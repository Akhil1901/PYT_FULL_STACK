"""Write a Python program using a closure where the outer function takes a number n 
and the inner function takes another number x and returns n + x. 
Input: n = 10 x = 5 
Output: 15"""

"""def outer(n):
    def inner(x):
        return n+x
    return inner
res=outer(5)
res1=res(10)
print(res1)"""
"""Create a closure counter() that maintains a count. 
Every time the inner function is called, it should increase the count by 1 and return 
the updated count. 
Input: c = counter() print(c()) print(c()) print(c()) 
Output: 1 2 3"""
"""def counter():
    count=0
    def inner():
        nonlocal count
        count=count+1
        return count
    return inner
c=counter()
print(c())
print(c())
print(c())
"""
"""Write a closure that stores a number and provides an inner function to increase the stored number
by a given value. 
Input: c = create_counter(10) print(c(5)) print(c(3)) print(c(7)) 
Output: 15 18 25"""
"""def outter():
    count=10
    def inner(x):
        nonlocal count
        count+=x
        return count
    return inner
res=outter()
print(res(5))
print(res(3))
print(res(7))"""

"""Write a function calculator(n) that returns three inner functions:
add(x) → adds x to n sub(x) → subtracts x from n mul(x) → multiplies
n by x All three functions must access the same variable n from the outer function. 
Input: add, sub, mul = calculator(1"""  