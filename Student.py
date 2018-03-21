class Student():
    def __init__(self, name, surname, institute, mark):
        self.n = name
        self.s = surname
        self.i = institute
        self.m = mark
		
def printData(a):
    x = print("Name is", a.n)
    y = print("Surname is", a.s)
    z = print("Institute is", a.i)
    return(x, y, z)


def multipleMarks(list1):
    flag = True
    while flag:
        try:
            n = float(input("Mark (press any non-numeric key to exit the loop): "))
            list1.append(n)
        except(SyntaxError, TypeError, ValueError) as e:
            flag = False
    return(list1)

def avg(a):
    obj = a.m
    mean = sum(obj)
    print("The average of marks is", (mean/10))

list1 = []
print("This program outputs one student's data and the average of his/her marks.\n")
a = Student(input("Name: "), input("Surname: "), input("Institute: "), multipleMarks(list1))
printData(a)
avg(a)
