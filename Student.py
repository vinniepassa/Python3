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
	for i in range(10):
		i = int(input("Mark: "))
		list1.append(i)
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
