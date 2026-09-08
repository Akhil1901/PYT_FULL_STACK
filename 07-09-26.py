"""class Student:
    def __init__(self, name, marks1, marks2):
        self.name=name
        self.m1=marks1
        self.m2=marks2

    def total_marks(self):
        total=self.m1+self.m2

        return total,self.name

student1=Student("Akhil",34,56)
a,b=student1.total_marks()
print(a)
print(b)"""

class Student:
    def __init__(self,name,marks1,marks2):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2

    def total(self):
        total=self.marks1+self.marks2
        return total

    def average(self):
        average=(self.marks1+self.marks2)/2
        return average

    def result(self):
        average=self.average()
        if(average>=40):
            return"pass"
        else:
            return "fail"

student1 = Student("Akhil", 80, 90)

total=student1.total()
print(f"total:{total}")

average=student1.average()
print(f"average: {average}")

result=student1.result()
print(f"result:{result}")