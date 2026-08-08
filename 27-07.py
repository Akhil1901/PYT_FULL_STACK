""""***    P  A T T E R N S    *****"""

""" *
   ***
  *****
 *******
*********
 ******* 
  *****
   ***
    *"""

"""rows=int(input("enter no of rows: "))
row_no=1
middle=(rows//2)+1
while(row_no<=rows):
    if(row_no>=1 and row_no < middle):
        print(" "*(middle-row_no),"*"*(2*row_no-1) ," "*(middle-row_no),sep="")
    elif(row_no==middle):
        print("*"*rows)
    elif(row_no>middle):
        print(" "*(row_no-middle),"*"*(rows-2*(row_no-middle))," "*(row_no-middle),sep="")
    row_no=row_no+1
"""
"""
*      *
**    **
***  ***
********
***  ***
**    **
*      *
"""
"""rows = int(input("enter an number of rows: "))
row_no=1
middle=(rows//2)+1
while(row_no<=rows):
    if(row_no>=1 and row_no<middle):
        print("*"*row_no," "*(rows + 1 - 2 * row_no),"*"*row_no,sep="")
    elif(row_no==middle):
        print("*"*(rows+1))
    else:
        print("*"*(rows-row_no+1)," "*(2*(row_no-middle)),"*"*(rows-row_no+1),sep="")
    row_no=row_no+1"""


