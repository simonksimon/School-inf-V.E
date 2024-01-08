# Otvorte a prečítajte súbor
with open('poprehadzovany_text1.txt', 'r') as f:
    text = f.read()

# Vytvorí nový text, kde sa pridá bodka jeden znak pred každé veľké písmeno
new_text = ''
i = 0
while i < len(text):
    if text[i].isupper() and i > 0:
        if new_text[-1] != '.' and (i == 0 or new_text[-2] != '.') and (i+1 == len(text) or text[i+1] != '.'):
            new_text = new_text[:-1] + '.' + text[i-1:i+1]
        else:
            new_text += text[i]
    else:
        new_text += text[i]
    i += 1

# Pridá bodku na koniec textu, ak tam už nie je
if new_text[-1] != '.':
    new_text += '.'

# Prejdite cez nový text a odstráňte druhú bodku od konca texu trikrát
for _ in range(3):
    dot_indices = [i for i, c in enumerate(new_text) if c == '.']
    if len(dot_indices) > 1:
        index = dot_indices[-2]
        new_text = new_text[:index] + new_text[index+1:]

# Vypíše transformovaný text na obrazovku
print(new_text)

# Uloží transformovaný text do súboru
with open('vystup.txt', 'w') as f:
    f.write(new_text)
