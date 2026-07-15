amount=int(input("enter the purchase amount:"))
p_ship=input("enter yes or no:")
discount=0
if(amount>1000):
    discount+=10
if(p_ship=='yes'):
    discount+=5
total_discount=discount
print("total discount percentage",discount)
discount_amount=(total_discount/100)*amount
print("discounted amount",discount_amount)
amount_to_pay=amount-discount_amount
print("amount to pay",amount_to_pay)
    
