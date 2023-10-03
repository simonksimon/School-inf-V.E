from collections import Counter
import string

# Otvorte a prečítajte súbor
with open('tabulka_pocetnosti.txt', 'r') as f:
    text = f.read()

# Vypíše text z textového súboru na obrazovku
print(text)

# Prevedie text na malé písmená a ignoruje ostatné znaky
text = ''.join(ch for ch in text if ch.isalpha()).lower()

# Vytvorí počítadlo pre každý znak
counter = Counter(text)

# Vypíše jednotlivé počty znakov anglickej abecedy v tvare znak – počet_výskytov
for letter in string.ascii_lowercase:
    print(f'{letter.upper()} - {counter[letter]}')

# Vypíše zoznam znakov, ktoré sa v texte vôbec nevyskytli
missing_letters = [letter for letter in string.ascii_lowercase if letter not in counter]
print('Znaky, ktoré sa v texte vôbec nevyskytli:', ', '.join(missing_letters).upper())
