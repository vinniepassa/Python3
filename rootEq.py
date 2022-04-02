import math
print("Calculator of quadratic equation roots")
a = int(input("First coefficient: "))
b = int(input("Second coefficient: "))
c = int(input("Third coefficient: "))
if a == 0:
         print("The equation is not quadratic")
else:
         delta = ((b*b)-4*a*c)
         if delta < 0:
             print("The equation does not admit solutions in the set of real numbers")
         else:
             x1 = (-b-(math.sqrt(delta)))/2*a
             print("First root:", x1)
             x2 = (-b+(math.sqrt(delta)))/2*a
             print("Second root:", x2)
    
