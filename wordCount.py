import sys

print("Questo programma riporta il numero di parole in una stringa")
flag = True
while flag:
        ans = input("Digita la stringa o digita & per uscire: ")
        if ans != "&":
                if len(ans.split()) == 0 or len(ans.split()) != 1:
                        print("Questa stringa contiene", len(ans.split()), "parole")
                elif len(ans.split()) == 1:
                        print("Questa stringa contiene", len(ans.split()), "parola")
        elif ans == "&":
                flag = False
                sys.exit()
