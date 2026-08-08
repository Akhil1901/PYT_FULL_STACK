"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
"""rows=int(input("enter no of rows: "))
for row_no in range(1,2*rows):
    if(row_no>=1 and row_no<(2*rows)/2):
        print(" "*(rows-row_no),"*"*((2*row_no)-1)," "*(rows-row_no),sep="")
    elif(row_no==2*rows/2):
        print("*"*(2*rows-1))
    else:
        print(" "*(row_no-rows),"*"*(2 * (2 * rows - row_no) - 1)," "*(row_no-rows),sep="")"""

"""
1
22
333
4444
55555
"""
"""rows=int(input("enter no of rows: "))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(row_no,end="")
    print()"""
"""1
12
123
1234
12345"""

"""rows=int(input("enter no of rows: "))
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(i,end="")
    print()
"""

"""12345
1234
123
12
1"""

"""rows=int(input("enter no of rows : "))
for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+2):
        print(i,end="")
    print()"""


"""ABCDE
ABCD
ABC
AB
A"""
"""rows=5
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(chr(64+i),end="")
    print()"""
"""ABCDE
ABCD
ABC
AB
A"""

"""rows=5
for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+2):
        print(chr(64+i),end="")
    print()"""
"""rows=5
for row_no in range(1,rows+1):
    for i in range(1,row_no+1):
        print(chr(64+row_no),end="")
    print()"""

"""rows=int(input("enter  no of rows: "))
for row_no in range(1,rows+1):
    for i in range(1,rows-row_no+1):
        print(" ",end="")
    for i in range(1,row_no+1):
        print(chr(64+i),end="")
    print()"""
