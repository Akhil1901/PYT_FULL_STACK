units=int(input("Enter the number of units consumed: "))
if(units<=100):
    bill=units*2
elif (units>100 and units<=300):
    bill=units*3
else:
    bill=units*5
print("The total bill is: ",bill)