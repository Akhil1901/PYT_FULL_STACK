"""1. Write a Python program to count the frequency of a given digit in a number using a while loop.
Input:
Number: 122313221
Digit: 2
Output: 4"""

"""num=int(input("enter an number: "))
d=int(input("enter to digit to count"))
count=0
while(num>0):
    digit=num%10
    if(digit==d):
        count=count+1
    num=num//10
if(count==0):
    print("enter the presented in the digit")
else:
    print(d,":",count)"""



"""2. Write a Python program to count how many even digits and odd digits are present in a given number using a while loop.
Input: 4827316
Output:
Even digits: 4
Odd digits: 3"""


"""num=int(input("enter an number : "))
evn_count=0
odd_count=0

while(num>0):
    digit=num%10
    if(num%2==0):
        evn_count=evn_count+1
    else:
        odd_count=odd_count+1
    num=num//10
print("even digts", evn_count)
print("odd digits", odd_count)"""

"""3. Write a Python program to reverse a number and check whether the reversed number is divisible by 11 using a while loop.
Input: 121
Output: Divisible by 11"""


"""num=int(input("enter an number "))
reverse=0
while(num>0):
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if(reverse%11 == 0):
    print("divisible by 11")
else:
    print("not divisible by 11")"""


"""4. Write a Python program to find the sum of all even digits and the sum of all odd digits in a given number using a while loop.
Input: 4827316
Output:
Sum of even digits: 20
Sum of odd digits: 10"""

""""num=int(input("enter a number : "))
evn_sum=0
odd_sum=0
while(num>0):
    digit=num%10
    if(num%2==0):
        evn_sum=evn_sum+digit
    else:
        odd_sum=odd_sum+digit
    num=num//10
print("sum of even digits", evn_sum)
print("sum of odd digits", odd_sum)
"""


"""5. Write a Python program to count the number of digits that are greater than 5 in a given number using a while loop.
Input: 58392716
Output: 4"""

"""num=int(input("enter an number : "))
count=0
while(num>0):
    digit=num%10
    if(digit>5):
        count=count+1
    num=num//10
print("no of digits greater than five",count)"""




