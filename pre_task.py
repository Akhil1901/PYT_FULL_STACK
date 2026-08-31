""" Write a Python function to return the *longest word* in a given sentence. 
If multiple words have the same maximum length, return the *first* one.
Input: Python is an amazing programming language
Output: programming 
Explanation: Find the word with the m"""
"""def longest_word(st):
    word=st.split()
    dic={}
    for i in word:
        dic[i]=len(i)
    maximum=0
    for k,v in dic.items():
        if(v>maximum):
            maximum=v
            t_word=k
    return t_word

st="Python is an amazing programming language"
ans=longest_word(st)
print(ans)"""

"""Write a Python function to return a new string by moving all 
*uppercase letters* to the beginning, followed by all *lowercase letters*,
while preserving their original order. 
Input: PyThOnProGram 
Output: PTOPGyhnroram 
Explanation: Collect all uppercase l"""
"""s="PyThOnProGram"
uppercase=" "
lowercase=""
for i in range(len(s)):
    if(s[i]>="A" and s[i]<="Z"):
        uppercase=uppercase+s[i]
    else:
        lowercase=lowercase+s[i]
output=uppercase+lowercase
print(output)"""
"""Write a Python function to return all characters that appear *exactly twice* in a string. 
Input: programming 
Output: r g m 
Explanation: Return all characters whose frequency is exactly 2."""
"""s="programming"
output="""""
"""for i in s:
    count=0
    for j in s:
        if(i==j):
            count=count+1
    if(count==2):
        if i not in output: 
            output=output+i+" "
print(output)"""

"""Write a Python function to return the *first non-repeating character* in a string. 
Input: aabbccddefg 
Output: e 
Explanation: Return the first character whose frequency is 1."""
"""st="aabbccddefg"
for i in st:
    count=0
    for j in st:
        if(i==j):
            count=count+1
    if(count==1):
        print(i)
        break
"""
"""Write a Python function to check whether two strings are *rotations* of each other. 
Input: s1 = "rotation" 
s2 = "tionrota" 
Output: True*"""
"""s1="rotation"
s2 = "tionrota" 
if(s1 in s2+s2):
    print(True)
else:
    print(False)"""

"""Write a Python function to return the *longest word* in a given sentence.
If multiple words have the same maximum length, return the *first* one. 
Input: Python is an amazing programming language 
Output: programmingc"""
"""st="Python is an amazing programming programminr language"
words=st.split()
dic={}
maximum=0
max_words=[]
for i in words:
    dic[i]=len(i)
for k,v in dic.items():
    if(v>maximum):
        maximum=v
        word=k
max_words.append(word)
print(max_words[0])
"""
"""n=30
for i in range(1,31):
    temp=i
    num=i
    s=0
    while(num>0):
        digit=num%10
        s=s+digit
        num=num//10
    if(temp%s==0):
        print(i)"""
"""Write a Python program to create a new string by placing all digits at the beginning, 
followed by all alphabets, while preserving their original order. 
Input: ab12cd34ef5 
Output: 12345abcdef"""
"""st="ab12cd34ef5"
numbers=""
lowercase=""
for i in st:
    if(i>='a'and i<='z'):
        lowercase=lowercase+i
    else:
        numbers=numbers+i
output=numbers+lowercase
print(output)"""

"""Write a Python program to print all characters whose ASCII value is a prime number. 
Input: ABCDEF 
Output: C"""
"""def is_prime(n):

    i = 1
    count = 0

    while(i <= n):
        if(n % i == 0):
            count = count + 1
        i = i + 1

    if(count == 2):
        return True
    else:
        return False

def asci_prime(str):
    for i in range(len(str)):
        value=ord(str[i])
        ans=is_prime(value)
        if(ans==True):
            return str[i]
str="ABCDEF"
res=asci_prime(str)
print(res)"""
"""Write a Python program to find the longest substring without repeating characters. 
Input: abcabcbb 
Output: abc"""
st="abcabcbb"
