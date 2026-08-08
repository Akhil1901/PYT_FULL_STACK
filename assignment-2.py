"""num=int(input("enter an number: "))
for i in range(1,num+1):
    number=i
    temp=i
    count=0
    while(i>0):
        i=i//10
        count=count+1
    d=10**(count-1)
    power_count=0
    sum=0

    while(temp>0):
        digit=temp//d
        power_count=power_count+1
        power=digit**power_count
        sum=sum+power
        temp=temp%d
        d=d//10
    if(sum==number):
        print(number)"""

"""num=int(input("enter the number:  "))
for i in range(1,num+1):
    number=i
    sum=0
    while(number>0):
        digit=number%10
        sum=sum+digit
        number=number//10
    if(i%sum==0):
        print(i)
"""
