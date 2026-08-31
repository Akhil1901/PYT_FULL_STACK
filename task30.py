"""Write a Python function to rearrange a string so that each word is 
placed immediately after its reversed form. Preserve the original word
order. 
Input: hello world python
Output: hello olleh world dlrow python nohtyp"""

"""def mirror(s):
    li=s.split()
    output=" "
    for i in li:
        temp=i
        holder=" "
        for j in range(len(temp)-1,-1,-1):
            holder=holder+temp[j]
        if temp not in output:
            output=output+temp+" "+holder+" "
    return output

s=input("enter your string: ")
res=mirror(s)
print(res)
    """
"""Write a Python function to find the longest word in a sentence that contains all unique characters. 
Input: apple dream house coding 
Output: dream"""

"""def long_unique(s):
    result=s.split()
    for i in result:
        if len(i)==len(set(i)):
            return i
st="apple dream house coding "
res=long_unique(st)
print(res)"""
"""Write a Python function to find the word whose characters have the highest total ASCII value. 
If multiple words have the same value, return the first one.
Input: cat dog apple 
Output: apple"""
"""st="cat dog apple"
def ascis(st):
    li=st.split()
    highest=0
    for i in li:
        temp=i
        total=0
        for i in temp:
            asci=ord(i)
            total=total+asci
        if(total>highest):
            highest=total
            word=temp
    return word
s=ascis(st)
print(s)"""

"""Write a Python function to decode a string where each alphabetic character is followed by a number 
indicating how many times it should be repeated. 
Input: a3b2c4 Output: aaabbcccc"""
"""st="a3b2c4"
def string(st):
    word=" "
    for i in range(len(st)):
        if (st[i]>="a" and st[i]<="z"):
            first=st[i]
        elif(int(st[i])>=1 and int(st[i])<=9):
            second=int(st[i])
            word=word+(first*second)
    return word
ans=string(st)
print(ans)"""


       
