"""nums=124688913
previous=0
count=0
while nums>0:
    current=nums%10
    if(previous>0):
        if(previous%2==0 and current%2==0):
            count=count+1
        else:
            count=count+0
    previous=current
    nums=nums//10
print(count)"""

"""nums = 5832741

largest = -1
second = -1

while nums > 0:

    current = nums % 10

    if current > largest:

        second = largest
        largest = current

    elif current > second and current != largest:

        second = current

    nums = nums // 10

print("Largest =", largest)
print("Second largest =", second)"""
"""num=1023045
product=1
while num>0:
    digit=num%10
    if(digit!=0):
        product=product*digit
    num=num//10
print(product)"""

"""num=8264359
while(num>0):
    digit=num%10
    number=digit
    i=1
    count=0
    while(i<=digit):
        if(digit%i==0):
            count=count+1
        i=i+1
    if(count==2):
        print(number)
        break
    num=num//10"""
