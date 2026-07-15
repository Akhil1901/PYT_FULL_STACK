age=int(input("enter your age:"))

if(age<18):
    print("register in pediatrics department")
else:
    insurance=input("do you have insurance? (yes/no): ")
    if(insurance=="yes"):
        print("You are eligible for a discount.")
    else:
        print("Please purchase insurance to avail discount.")