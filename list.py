"""aabbcc"""
st="aabbcca"
output=" "
pre_output=0
for i in st:
    temp=i
    count=0
    for j in st:
        if (temp==j):
            count=count+1
    pre_output=temp+str(count)
    if(pre_output not in output):
        output=output+pre_output
print(output)