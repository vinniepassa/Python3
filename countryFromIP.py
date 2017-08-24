import webbrowser
import sys

print("Questo programma cerca online l'indirizzo IP immesso")
website = "https://www.iplocation.net/search?cx=partner-pub-1026064395378929%3A2796854705&cof=FORID%3A10&ie=UTF-8&q=79.55.243.41&sa=Search&siteurl=www.iplocation.net%2F&ref=www.iplocation.net%2F&ss=40j1600j2"
flag = True
while flag:
    ans = input("Inserisci indirizzo IP, oppure 0 per uscire: ")
    if ans != "0":
        website1 = website.replace("79.55.243.41", ans)
        webbrowser.open(website1)
    elif ans == "0":
        flag = False
        sys.exit()
