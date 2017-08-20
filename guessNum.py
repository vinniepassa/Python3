import random
import sys
import winsound #libreria suoni
print("Questo gioco si basa sull'indovinare un numero casuale")
ran_num = random.randrange(2, 500) 
flag = True
while flag:
    ans = int(input("Digita il numero, oppure digita 0 per uscire: "))
    if ans != 0:
        if ans > ran_num:
            print("Troppo alto!")
        elif ans < ran_num:
            print("Troppo basso!")
        elif ans == ran_num:
            winsound.Beep(800, 400) #numero sinistra = frequenza in Hertz (37-32767), numero destra = durata millisecondi
            print("Hai indovinato!")
            flag = False
    elif ans == 0:
        flag = False
        sys.exit()
        
