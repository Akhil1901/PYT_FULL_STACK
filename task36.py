"""Write a recursive function to find the sum of all even digits in a given number. 
Input: n = 583624 
Output: 20"""

"""def fun(n):
    result= n%10
    s=0
    if result%2==0:
        s+=result
    if n<10:
        return s
    else:
        return s+ fun(n//10)

n=583624
print(fun(n))"""

"""Write a recursive function to reverse a given number without using loops or converting the number into a string. 
Input: n = 48291 
Output: 19284"""
def inverse(n):
    rev=0
    if(n==0):
        return ''
    d=n%10
    rev=rev*10+d
    return str(d)+inverse(n//10)
b=inverse(1234)
print(b)

"""Write a recursive function to find the factorial of a given number. 
Input: n = 6 
Output: 720"""




"""Write a recursive function to find the sum of the first n natural numbers. 
Input: n = 8 
Output: 36"""




"""Write a recursive function to find the nth Fibonacci number. 
Input: n = 7 Output: 13"""