import random
import re

def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)

# Otvorte a prečítajte súbor
with open('poprehadzovany_text_vstup2.txt', 'r') as f:
    text = f.read()

# Vypíše text z textového súboru na obrazovku
print(text)

# Vypíše prázdny riadok na obrazovku
print()

# Rozdelí text na slová a oddelí prvé a posledné písmeno každého slova
words = re.findall(r'\b\w+\b', text)
non_words = re.findall(r'\W+', text)
shuffled_words = []
for word in words:
    if len(word) > 3:
        middle = pomiesaj(word[1:-1])
        shuffled_word = word[0] + middle + word[-1]
    else:
        shuffled_word = word
    shuffled_words.append(shuffled_word)

# Vytvorí transformovaný text
transformed_text = ''
for i in range(len(shuffled_words)):
    transformed_text += shuffled_words[i]
    if i < len(non_words):
        transformed_text += non_words[i]

# Vypíše transformovaný text na obrazovku
print(transformed_text)

# Uloží transformovaný text do súboru
with open('poprehadzovany_text.txt', 'w') as f:
    f.write(transformed_text)
