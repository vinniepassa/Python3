class Student():
    def __init__(self, name, surname, institution, grade):
        self.n = name
        self.s = surname
        self.i = institution
        self.m = grade
		
def printData(a):
    x = print("Name is", a.n)
    y = print("Surname is", a.s)
    z = print("Institution is", a.i)
    return(x, y, z)


def multipleGrades(list1):
    flag = True
    while flag:
        try:
            n = float(input("Grade (press any non-numeric key to exit the loop): "))
            list1.append(n)
        except(SyntaxError, TypeError, ValueError) as e:
            flag = False
    return(list1)

def avg(a):
    obj = a.m
    mean = sum(obj)
    print("Average grade is", (mean/10))

list1 = []
print("This program outputs student data for one student and the average of their grades.\n")
a = Student(input("Name: "), input("Surname: "), input("Institution: "), multipleGrades(list1))
printData(a)
avg(a)
