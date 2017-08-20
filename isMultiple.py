print("Questo programma legge due numeri e controlla se il primo è multiplo del secondo")
first = int(input("Primo numero: "))
second = int(input("Secondo numero: "))
if first%second == 0:
    print(first, " è multiplo di ", second)
elif first%second != 0:
    print(first, " non è multiplo di ", second)
