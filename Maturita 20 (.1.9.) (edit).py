from collections import Counter
import string
with open('tabulka_pocetnosti.txt', 'r') as f:
    text = f.read()
print(text)
text = ''.join(ch for ch in text if ch.isalpha()).lower()
counter = Counter(text)
for letter in string.ascii_lowercase:
    print(f'{letter} - {counter[letter]}')
missing_letters = [letter for letter in string.ascii_lowercase if letter not in counter]
print('Znaky, ktoré sa v texte vôbec nevyskytli:', ', '.join(missing_letters))
