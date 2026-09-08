"""Write a generator function that takes a number and generates its digits from right to left. 
Input: n = 58321 
Output: 1 2 3 8 5"""
"""def generator_digits(n):
    while(n>0):
        d=n%10
        yield d
        n=n//10

n=58321
for i in generator_digits(n):
    print(i)"""

"""Write a generator function that generates the first n Fibonacci numbers. 
Input: n = 7 
Output: 0 1 1 2 3 5 8"""
count=0
"""def generate_fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    i=3
    while(i<=n):
        c=a+b
        yield c
        a=b
        b=c
        i=i+1
n=7
for i in generate_fibonacci(n):
    print(i)
"""
"""Write a generator function that takes a list and yields an element only when it is different from the previously yielded element. 
Input: nums = [1, 1, 2, 2, 2, 3, 1, 1, 4] 
Output: 1 2 3 1 4"""
"""def generator(x):
    for i in range(len(x)):
        if(x[i]!=x[i-1]):
            yield x[i]

x=[1,1, 2, 2, 2, 3, 1, 1, 4]
for i in generator(x):
    print(i)"""

"""Write a generator function that generates the first n prime numbers. 
Input: n = 8 
Output: 2 3 5 7 11 13 17 19"""
"""def generator_prime(n):
    i=1
    prime_count=0
    while(True):
        num=i
        j=1
        count=0
        while(j<=num):
            if(num%j==0):
                count=count+1
            j=j+1
        if(count==2):
            yield num
            prime_count+=1
        if(prime_count==n):
            break
        i=i+1

n=8
for i in generator_prime(n):
    print(i)"""

"""Write a Python generator function that takes a compressed string and yields each character/group according to its count. 
Input: a[2]bc[3] 
Output: a a bc bc bc"""
def compress_generator(st):
    n_st = ""
    for i in range(len(st)):
        count = 0
        content = ""
        if st[i]=="[":
            for j in range(i+1,len(st)):
                if st[j]=="]":
                    break
                content+=st[j]
        if st[i]=="[":
            count=int(st[i-1])
        n_st+=count*content
    yield n_st
  
st="a[2]bc[3]"
for i in compress_generator(st):
    print(i)