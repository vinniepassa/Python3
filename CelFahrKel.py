print("Programma per convertire temperature da gradi Celsius a gradi Fahrenheit e Kelvin")
abs_zero = -273.15
celsius = int(input("Per favore, inserisci la temperatura in gradi Celsius: "))
if celsius >= abs_zero:
    fahrenheit = (9/5)*celsius+32
    kelvin = celsius+273.15
    print("La temperatura in gradi Fahrenheit è", fahrenheit)
    print("In gradi Kelvin è", kelvin)
elif celsius < abs_zero:
    print("Errore!")
