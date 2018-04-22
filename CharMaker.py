import time
import string

class Character():
    def __init__(self, name, gender, cls, strength, magic, dexterity):
        self.name = name
        self.gender = gender
        self.cls = cls
        self.strength = strength
        self.magic = magic
        self.dexterity = dexterity

    def printStats(self):
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Class:", self.cls)
        print("Strength:", self.strength)
        print("Magic:", self.magic)
        print("Dexterity:", self.dexterity)

print("Welcome to CharMaker! \n")
print("CharMaker lets you create the perfect RPG character based on your personality \n")
print("Soon you will be asked several questions \n")

time.sleep(5)

q0 = input("What's your name? ")
q1 = input("Question #1: Are you a male or a female? [M][F] ")
q2 = input("Question #2: 'I would rather read a book at home than going out with friends' [Y][N] ")
q3 = input("Question #3: 'I play at least two sports' [Y][N] ")
q4 = input("Question #4: 'I am a good cook [Y][N]' ")
q5 = input("Question #5: 'I get angry easily [Y][N]' ")
q6 = input("Question #6: 'I easily get bored when I am doing homework' [Y][N] ")
q7 = input("Question #7: 'I often act impulsively' [Y][N] ")

print("\nHooray! That was the last question. Wait a few seconds...")

char = Character(q0, q1, "", 5, 5, 5)

q1.upper()
q2.upper()
q3.upper()
q4.upper()
q5.upper()
q6.upper()

if(q1 == "M"):
    char.strength += 2
    char.dexterity += 1
else:
    char.strength -= 1
if(q2 == "N"):
    char.magic -= 2
else:
    char.magic += 2
if(q3 == "Y"):
    char.dexterity += 2
    char.strength += 1
else:
    char.magic += 1
if(q4 == "Y"):
    char.magic += 2
    char.dexterity += 1
else:
    char.magic -= 2
if(q5 == "Y"):
    char.strength += 2
else:
    char.magic += 1
if(q6 == "Y"):
    char.magic += 2
else:
    char.magic += 1
if(q7 == "Y"):
    char.dexterity -= 2
    char.strength += 1
else:
    char.magic += 1

if(char.strength >= 10) and (char.dexterity <= 7):
    char.cls = "Warrior"
if(char.strength < 10) and (char.dexterity > 7):
    char.cls = "Bandit"
if(char.strength < 10) and (char.dexterity >= 6) and (char.magic >= 10):
    if(char.gender == "M"):
        char.cls = "Wizard"
    else:
        char.cls = "Witch"

time.sleep(5)

print("Done! These are your character's stats:\n")
char.printStats()
