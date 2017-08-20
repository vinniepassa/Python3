print("Questo programma classifica un anno in bisestile o non-bisestile")
anno = int(input("Inserisci l'anno: "))
if ((anno%4 == 0) and (anno%100 != 0)) or (anno%400 == 0):
    print("L'anno", anno, "è bisestile")
else:
    print("L'anno", anno, "non è bisestile")
