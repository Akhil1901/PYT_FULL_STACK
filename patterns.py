#patterns
"""rows = int(input("enter the number of rows:"))
for row_no in range(1,rows+1):
    print("*"*rows)
"""
"""
*
**
***
****
*****"""
"""rows=int(input("enter an number: "))
for row_no in range(1,rows+1):
    print("*"*row_no)"""

"""
*****
****
***
**
*"""
"""rows=int(input("enter an number: "))
row_no=1
for row_no in range(1,rows+1):
    print("*"*(rows-row_no+1))"""

"""
1
12
123
1234
12345"""

"""rows=int(input("enter no of rows: "))
row_no=1
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(i,end="")
    print()"""


"""
1
22
333
4444
55555"""

"""rows=int(input("enter an number of rows: "))
row_no=1
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(row_no,end="")
    print()"""

"""   
    *
   **
  ***
 ****
*****"""