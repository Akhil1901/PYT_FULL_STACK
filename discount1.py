num = int(input("Enter the price: "))
mship = input("Enter membership (yes/no): ")
c_code = input("Enter coupon code (yes/no): ")

discount = 0

if num > 1000:
    discount += 10

if mship == "yes":
    discount += 5

if c_code == "yes":
    discount += 5

calculated_discount = (discount / 100) * num
final_price = num - calculated_discount

print("Discount:", discount, "%")
print("Discount Amount:", calculated_discount)
print("Final Price:", final_price)
