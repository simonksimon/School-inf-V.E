import random

# Otvorte a prečítajte súbor
with open('poprehadzovany_text1_vstup.txt', 'r') as f:
    text = f.read()

# Vypíše text z textového súboru na obrazovku
print(text)

# Funkcia na poprehadzovanie písmen vo slove
def shuffle_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    else:
        return word

# Rozdelí text na slová a poprehadzuje písmená vo slovách
words = text.split()
shuffled_words = [shuffle_word(word) for word in words]

# Vytvorí transformovaný text
transformed_text = ' '.join(shuffled_words)

# Vypíše transformovaný text na obrazovku
print(transformed_text)

# Uloží transformovaný text do súboru
with open('poprehadzovany_text1.txt', 'w') as f:
    f.write(transformed_text)
