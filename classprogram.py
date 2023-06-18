class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.grade=""
    def displayInfo(self):
        print("My name is: ",self.name)
        print("My marks is: ",self.marks)
        print("My grade is: ",self.grade)
    def calculate(self):
        if(self.marks>=600):
            self.grade="A"
        elif(self.marks>=500):
            self.grade="B"
        elif(self.marks>=350):
            self.grade="c"
        else:
            print("FAIL")
'''s1=Student("Aditi",700)
s1.displayInfo()
s1.calculate()
s1.displayInfo()'''
n=int(input())
for i in range(n):
    name=input()
    marks=int(input())
    s1=Student(name,marks)
    s1.calculate()
    s1.displayInfo()
    print("-----------------------------------------------------------------------------------")