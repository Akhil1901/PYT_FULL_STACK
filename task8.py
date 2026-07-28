"""num1=int(input("enter an number : "))
num2=int(input("enter an number : "))
i=1
while(True):
    if(i%num1 ==0 and i%num2==0):
        print(i)
        break
    i=i+1
"""

"""num=int(input("enter an number "))
temp=num
sum=0
while(True):
    sum=0
    while(num>0):
        digit=num%10
        sqr=digit**2
        sum=sum+digit
        num=num//10
    num=sum
    if(sum==1):
        print("happy number")
        break
"""
"""rows=int(input("enter an number "))
row_no=1
while(row_no<=rows):
    if(row_no==1 or row_no==rows):
        print("*"*row_no)
    else:
        print("*"," "*(row_no-rows//2),"*",sep="")

    row_no=row_no+1"""

"""rows=int(input("enter an number : "))
row_no=1

while(row_no<=rows):
    if(row_no%2 !=0):
        print("*"*rows)
    else:
        print("*"," "*(rows-2),"*",sep="")
    row_no=row_no+1"""

"""rows=int(input("enter an number : "))
row_no=1
while(row_no<=(rows*2)):
    if(row_no>=1 and row_no<((rows*2)//2)):
        print("*"*row_no)
    elif(row_no==((rows*2)//2)):
        print("*"*rows)
    elif(row_no>((rows*2)//2)):
        print("*"*((rows*2)-row_no))
    row_no=row_no+1
       """