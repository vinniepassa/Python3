import pyphen
import string
import time

def basic_vocab(newt):
  fundamental = 0
  high_use = 0
  high_avail = 0

  with open('fondamentali.txt', 'r') as f1, open('alto_uso.txt', 'r') as f2, open('alta_disponibilità.txt', 'r') as f3:
    strings1 = f1.read()
    strings2 = f2.read()
    strings3 = f3.read()
    for i in newt:
      if i in strings1 and i not in strings2 and i not in strings3:
        fundamental += 1
      elif i not in strings1 and i in strings2 and i not in strings3:
        high_use += 1
      elif i not in strings1 and i not in strings2 and i in strings3:
        high_avail += 1
  
  return(fundamental, high_use, high_avail)
  
def syllables(text, language):
  syllable_counter = 0
  poly_counter = 0
  hyphenated = []
  pyphen.language_fallback(language)
  dic = pyphen.Pyphen(lang=language)
  for i in text:
    elem = dic.inserted(i)
    if '-' not in elem:
      syllable_counter += 1
    else:
      if elem.count('-')>=3:
        poly_counter += 1
      else:
        syllable_counter += elem.count('-')
  syllable_counter += 2
  if language == "it_IT":
    return(syllable_counter)

def preprocess(text):
  sentence_counter = 0
  letter_counter = 0
  word_counter = 0
  
  if "." not in text:
      sentence_counter = 1
  else:
      for i in text:
          if i == ".":
              sentence_counter += 1
              text.remove(i)

  for j in text:
      if j in string.ascii_letters:
          letter_counter += 1

  for k in text:
      if k in string.punctuation or k in string.digits:
          text.remove(k)

  text = "".join(text)
  text = text.split()
  word_counter = len(text)

  return(text, sentence_counter, letter_counter, word_counter)

def main():
  flag = True
  while flag:
    filename = input("Nome file: ")
    language = input("Lingua: ")
    print()
    tic = time.process_time()
    with open(filename, 'r') as file: #includere encoding='utf8' dopo 'r' se non dovesse funzionare alla prima
      text = file.read()
    text = list(text)

    newt, s, l, w = preprocess(text)

    f, u, a = basic_vocab(newt)

    if language == "it_IT":
      sy = syllables(newt, language)
      
      gulpease_index = 89+(((300*s)-(10*l))/w)

      if gulpease_index < 80 and gulpease_index >= 60:
        print("Indice GULPEASE:",gulpease_index,'difficile per licenza elementare')
      elif gulpease_index < 60 and gulpease_index >= 40:
        print("Indice GULPEASE:",gulpease_index,'difficile per licenza media')
      elif gulpease_index < 40:
        print("Indice GULPEASE:",gulpease_index,'difficile per licenza superiore')
      else:
        print("Indice GULPEASE:",gulpease_index)

      flesch_formula = 206 - (0.65*sy) - (w/s)

      if flesch_formula >= 90:
        print("Formula di Flesch:",flesch_formula,'(molto facile - fino a licenza elementare)')
      elif flesch_formula >= 80 and flesch_formula < 90:
        print("Formula di Flesch:",flesch_formula,'(facile - da licenza elementare a prima media)')
      elif flesch_formula >= 70 and flesch_formula < 80:
        print("Formula di Flesch:",flesch_formula,'(abbastanza facile - seconda media)')
      elif flesch_formula >= 60 and flesch_formula < 70:
        print("Formula di Flesch:",flesch_formula,'(medio - licenza media)')
      elif flesch_formula >= 50 and flesch_formula < 60:
        print("Formula di Flesch:",flesch_formula,'(abbastanza difficile - da licenza media a licenza superiore)')
      elif flesch_formula >= 30 and flesch_formula < 50:
        print("Formula di Flesch:",flesch_formula,'(difficile - università ma non laurea)')
      elif flesch_formula < 30:
        print("Formula di Flesch:",flesch_formula,'(molto difficile - laurea)')

    print()
    print("Frasi:",s)
    print("Parole:",w)
    print("Sillabe:",sy)
    print("Lettere:",l)
    print()
    print("Fondamentali (%):",((f*100)/w))
    print("Alto uso (%):",((u*100)/w))
    print("Alta disponibilità (%):",((a*100)/w))
    print()

    toc = time.process_time()
    print("Durata processo:",toc-tic)
    print()
    flag2 = True
    while flag2:
      print("Nuova analisi? [Y][N]")
      ans = input()
      ans = ans.upper()
      print()
      if ans == 'Y':
        flag2 = False
        continue
      elif ans == 'N':
        flag = False
        break

main()
