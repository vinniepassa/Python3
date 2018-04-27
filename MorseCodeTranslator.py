import time
import os

def translator(alpha, text, save): 
    latinToMorse = {"":""," ":"  ", "A":"·- ", "B":"-··· ", "C":"-·-· ", "D":"-·· ", "E":"· ", "F":"··-· ", "G":"--·", "H":"····", "I":"··", "J":"·---", "K":"-·-", "L":"·-··", "M":"--", "N":"-·", "O":"---", "P":"·--·", "Q":"--·-", "R":"·-·", "S":"···", "T":"-", "U":"··-", "V":"···-", "W":"·--", "X":"-··-", "Y":"-·--", "Z":"--··", "0":"-----", "1":"·----", "2":"··---", "3":"···--", "4":"····-", "5":"·····", "6":"-····", "7":"--···", "8":"---··", "9":"----·", ".":"·-·-·-", ",":"--··--", "?":"··--··", "'":"·----·", "!":"-·-·--", "/":"-··-·"}
    morseToLatin = {"":""," ":" ","·-":"A","-···":"B","-·-·":"C","-··":"D", "·":"E","··-·":"F","--·":"G","····":"H","··":"I","·---":"J","-·-":"K","·-··":"L","--":"M","-·":"N","---":"O","·--·":"P","--·-":"Q","·-·":"R","···":"S","-":"T","··-":"U","···-":"V","·--":"W","-··-":"X","-·--":"Y","--··":"Z","-----":"0","·----":"1","··---":"2","···--":"3","····-":"4","·····":"5","-····":"6","--···":"7","---··":"8","----·":"9","·-·-·-":".","--··--":",","··--··":"?","·----·":"'","-·-·--":"!","-··-·":"/"}
    text = text.upper()
    translation = []
    if(save == "N"):
        if(alpha == "Latin"):
            print("Output: ", end="", sep="")
            for i in text:
                print(latinToMorse[i], end="", sep="")
            print()
            print()
        elif(alpha == "Morse"): #modify
            print("Output: ", end="", sep="")
            for i in text:
                print(morseToLatin[i], end="", sep="")
            print()
            print()            
    else:
        if(alpha == "Latin"):
            for i in text:
                translation.append(latinToMorse[i])
            translation = translation[:-1]
            translation = "".join(translation)
            return(translation)
        elif(alpha == "Morse"): #problem is in this branch
            if("   " in text):
                text = text.split("   ")
                print(text)
                for i in text:
                    if(" " in i):
                        i = i.split(" ")
                        print(i)
                    for j in i:
                            translation.append(morseToLatin[j])
                translation = " ".join(translation)
            else:
                text = text.split(" ")
                for i in text:
                    translation.append(morseToLatin[i])
                translation = "".join(translation)
            print(translation)
            #translation = translation[:-1]
            #translation = "".join(translation)
            return(translation)

def detectAlpha(text):
    alpha = ""
    if("·" in text):
        alpha = "Morse"
    else:
        alpha = "Latin"
    return(alpha, text)

def main():
    print("MorseCodeTranslator\n")
    time.sleep(2)

    ans = 1

    while(ans != 0):
        print("*MENU*")
        print("Translate string [1]")
        print("Translate .txt file [2]")
        print("Exit [0]\n")
        ans = int(input(""))
        print()

        if(ans == 1):
            strng = input("Enter the string: ")
            a, b = detectAlpha(strng)
            
            print("Save translation to file? [Y][N]\n")
            save = input()
            save = save.upper()
            if(save == "Y"):
                filename = input("File name?\n")
                file = open(filename, 'w')
                file.write(translator(a, b, save))
                file.close()
                print()
            else:
                translator(a, b, save)
        elif(ans == 2):
            filename = input("Enter the file's name: ")
            if(not os.path.exists(filename)):
                print("File", filename, "does not exist in working directory!\n")
                time.sleep(2)
            else:
                __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
                with open(os.path.join(__location__, filename)) as file:
                    text = file.read()
                    a, b = detectAlpha(text)

                    print("Save translation to file? [Y][N]\n")
                    save = input()
                    save = save.upper()
                    if(save == "Y"):
                        filename = input("File name?\n")
                        file = open(filename, 'w')
                        file.write(translator(a, b, save))
                        file.close()
                        print()
                    else:
                        translator(a, b, save)

main()
