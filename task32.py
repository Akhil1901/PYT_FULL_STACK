"""
Write a Python function to find the maximum sum of any two consecutive elements in 
a list and return the elements that produce the maximum sum. 
Input: [4, 7, 2, 9, 5, 12, 3] Output: [5, 12]"""
"""li=[4,7,2,9,5,12,3]
def max_cons(li):
    s=0
    output=[]
    for i in range(len(li)-1):
        first=li[i]
        second=li[i+1]
        if(first+second>s):
            s=first+second
            output.clear()
            output.append(li[i])
            output.append(li[i+1])
    print(output)
max_cons(li)"""

"""Write a Python function to remove consecutive duplicate characters from a string while keeping the
 first occurrence of each consecutive group. 
 Input: "aaabbccdaaee" 
 Output: "abcdae"""
"""def remove_consecutive(s):
    a=""
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            a+=s[i]
    else:
        a+=s[i]
    return a
st="aaabbccdaaee"
ans=remove_consecutive(st)
print(ans)
"""
"""Given a tuple of numbers, 
find the smallest positive number that is missing from the tuple. 
Input: (3, 4, -1, 1, 2, 6) 
Output: 5
"""
"""tu=(3,4,-1,1,2,6)
n_tu=sorted(tu)
ans=0
for i in range(len(n_tu)-1):
    if(n_tu[i]>0 and n_tu[i+1]!=n_tu[i]+1):
        ans=n_tu[i]+1
print(ans)"""

"4"
"""def outer():
    x=5
    def inner():
        nonlocal x
        li=[3,7,2,8]
        for i in range(len(li)):
            if(i==0):
                res=li[i]+x
                print(res)
            else:
                res=res+li[i]
                print(res)
    return inner()
outer()
"""