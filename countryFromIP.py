import webbrowser
import sys
import socket

website = "https://www.iplocation.net/search?cx=partner-pub-1026064395378929%3A2796854705&cof=FORID%3A10&ie=UTF-8&q=79.55.243.41&sa=Search&siteurl=www.iplocation.net%2F&ref=www.iplocation.net%2F&ss=40j1600j2"
flag1, flag2 = True, True

on_or_off = int(input("Online [1] or offline [2]? "))
while flag2:
    if on_or_off == 1:
        while flag1:
            ans = input("Insert IP address, or press 0 to exit: ")
            if ans != "0":
                website1 = website.replace("79.55.243.41", ans)
                webbrowser.open(website1)
            elif ans == "0":
                flag1, flag2 = False, False
                sys.exit()
    elif on_or_off == 2:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        s.close()
        flag2 = False
