"""amount=int(input("enter the amount:"))
if(amount<500):
    print("shipping charge:100")
elif(amount>=500 and amount<=1999  ):
    print("shipping charge:50")
else:
    print("free shipping")"""
'''reward=int(input("enter your reward points: "))
if(reward>=1000):
    print("platinum")
elif(reward>=500 and reward<=999):
    print("Gold")
elif(reward>=200 and reward<=499):
    print("silver")
else:
    print("bronze")
'''
'''num = int(input("enter a number : "))
i=1
sum=0
while(i<=num):
    sum=sum+i
    i=i+1
print(sum)'''
'''num=int(input("enter a number : "))
i=1
product=1
while(i<=num):
    if(i%2!=0):
        product=product*i
    i=i+1
print(product)'''
'''num=int(input("enter a number: "))
i=1
while(i<=num):
    if(i%2==0 and i%3==0 ):
        print(i)
    i=i+1
'''
num=int(input("enter a number: "))
i=1
count=0
while(i<=num):
    if(num%i==0):
        count=count+1
    i=i+1
if(count==2):
    print('prime')
else:
    print("not prime")

