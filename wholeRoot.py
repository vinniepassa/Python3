print("Questo programma calcola la radice quadrata intera approssimata per difetto di un numero")
sqrt = 0
num = int(input("Inserisci numero: "))
while ((sqrt*sqrt) <= num):
    sqrt += 1
sqrt -= 1
print("Risultato:", sqrt)
