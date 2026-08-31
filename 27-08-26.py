"""st="aaabbcc"
output=" "
for i in st:
    temp=i
    count=0
    for j in st:
        if(temp==j):
            count=count+1
    if(temp not in output):
        output=output+temp+str(count)
print(output)"""

st="babadbaab"
"""def is_plaindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False"""
i=0
j=0
while(i<len(st)):
    first=i
    last=j
    word=st[first:last+1]
    print(word)
    if()
    
