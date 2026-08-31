"""x=[[10,20,30],[20,40,10],[50,20,30],[60,10,20]]
new_li=[]
for i in x:
    new_li.extend(i)
print(new_li)
frequent=0
for j in new_li:
    count=0
    for k in new_li:
        if(j==k):
            count=count+1
    if(count>frequent):
        frequent=count
        element=j
print("frequency: ", frequent)
print("element: ", element)"""
d= {"A":45,"B":80,"C":25,"D":60,"E":90}
li=list(d.items())
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        if(li[i][1]<li[j][1]):
            li[i],li[j]=li[j],li[i]
ans={k:v for k,v in li}
print(ans)
