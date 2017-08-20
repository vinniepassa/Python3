print("Questo programma conta le vocali in una stringa")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
ans = list((input("Parola: ")))
tot = 0
for i in vowels:
        if i in ans:
                tot += ans.count(i)
print("La parola ha", tot, "vocali")





                
