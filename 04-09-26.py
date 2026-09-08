"""s="(}"
req_count=len(s)//2
count=0
for i in range(len(s)-1):
    curr=s[i]
    nxt=s[i+1]
    if(curr=="(" and nxt==")"):
        count=count+1
    elif(curr=="[" and nxt=="]"):
        count=count+1
    elif(curr=="{" and nxt=="}"):
        count=count+1
if(count==req_count):
    print(True)
else:
    print(False)"""

"""data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res=[j**2 for i in data for j in i if j%2==0]
print(res)"""

"""data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res=[j*2 if j%2==0 else j*3 for i in data for j in i]
print(res)"""

"""data = [[10, 15, 20], [25, 30, 35], [40, 45, 50]]
res=[j for i in data for j in i if j>20 and j%2==0]
print(res)"""
"""Write a recursive function to print numbers from 1 to 10"""
"""def num(n):
    if(n==11):
        return
    print(n)
    num(n+1)

num(1)"""

"""
def vowel_convert(fun):
    def innerfun(n):
        output=""
        vowels="aieou"
        space=" "
        res=fun(n)
        for i in range(len(res)):
            if(res[i] in vowels):
                ans=res[i].upper()
                output=output+ans
            else:
                output=output+res[i]
        return output
    return innerfun

def decorator(fun):
    start="***"
    total=""
    def inner_fun(n):
        res_str=fun(n)
        total=start+res_str+start
        return total
    return inner_fun
@decorator
@vowel_convert
def string(n):
    return n

n="hello world"
print(string("hello world"))"""



"""def generator_word(s):
    words=s.split()
    for i in range(len(words)-1,-1,-1):
        yield words[i]

s="python is very powerful"
for i in generator_word(s):
    print(i)"""

"""
def num(n):
    if(n==0):
        return
    print(n)
    num(n-1)

num(10)  """

"""def s_n(n):
    if(n==0):
        return 0
    return n+s_n(n-1)
print(s_n(5))"""

"""
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
print(fact(5))"""

"""def count_digits(n):
    count=0
    if(n==0):
        return count
    return 1+count_digits(n//10)

print(count_digits(12345))"""

"""Input: 12345
Output: 15"""
