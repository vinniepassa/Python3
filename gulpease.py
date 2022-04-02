import string

def gulpeaseIndex(s, l, w):
    formula = 89+(((300*s)-(10*l))/w)
    print("Indice GULPEASE:", formula)

def preprocess(text):
    sentenceCounter = 0
    letterCounter = 0
    wordCounter = 0
    
    if "." not in text:
        sentenceCounter = 1
    else:
        for i in text:
            if i == ".":
                sentenceCounter += 1
                text.remove(i)

    for j in text:
        if j in string.ascii_letters:
            letterCounter += 1

    for k in text:
        if k in string.punctuation or k in string.digits:
            text.remove(k)

    text = "".join(text)
    text = text.split()
    word_counter = len(text)

    return(sentenceCounter, letterCounter, wordCounter)

flag = True

while flag:
    text = input('Testo: ')
    text = list(text)
    s, l, w = preprocess(text)
    gulpeaseIndex(s, l, w)
    ans = input("Nuova analisi? [Y][N] ")
    if ans == "N" or ans == "n":
        flag = False
    elif ans == "Y" or ans == "y":
        next
    else:
        print("Input non valido!")
        break
