print("Questo programma legge da tastiera una sequenza di numeri e ne determina la media a partire dal primo numero")
print("Inserendo un numero negativo, il programma termina")
tot = 0
ind = 0
num = int(input("Inserisci un numero: "))
while num >= 0:
    tot += num
    ind += 1
    avg = tot/ind
    print("La media attuale è:", avg)
    num = eval(input("Inserisci un numero: "))
print("La media finale è:", avg)
