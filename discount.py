num = int(input("enter the price: "))
mship=input("enter yes or no : ")
c_code=input(" enter yes or no : ")
if num>1000 and mship=='yes' and c_code=='yes':
    discount = 10+5+5
    calculated_discount=(discount/100)*num
    final_price=num-calculated_discount
    print(final_price)
if num > 1000 and mship == 'yes' and c_code=='no' :
   discount = 10+5
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num > 1000 and mship == 'no' and c_code=='yes' :
   discount = 10+5
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num <1000 and mship == 'yes' and c_code=='yes' :
   discount = 5+5
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num <1000 and mship == 'no' and c_code=='no' :
   discount = 0
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num <1000 and mship == 'yes' and c_code=='yes' :
   discount = 5+5
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num <1000 and mship == 'no' and c_code=='yes' :
   discount = 5
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num >1000 and mship == 'no' and c_code=='no' :
   discount = 10
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)
if num <1000 and mship == 'yes' and c_code=='no' :
   discount = 5
   calculated_discount=(discount/100)*num
   final_price=num-calculated_discount
   print(final_price)

