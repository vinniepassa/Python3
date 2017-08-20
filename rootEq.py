import math
print("Calcolatore radici di equazioni secondo grado")
a = int(input("Primo coefficiente: "))
b = int(input("Secondo coefficiente: "))
c = int(input("Terzo coefficiente: "))
if a == 0:
         print("L'equazione non è di secondo grado")
else:
         delta = ((b*b)-4*a*c)
         if delta < 0:
             print("L'equazione non ammette soluzioni reali")
         else:
             x1 = (-b-(math.sqrt(delta)))/2*a
             print("La prima radice è:", x1)
             x2 = (-b+(math.sqrt(delta)))/2*a
             print("La seconda radice è:", x2)
    
