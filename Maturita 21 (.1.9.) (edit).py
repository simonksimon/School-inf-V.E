import random
with open('poprehadzovany_text1_vstup.txt', 'r') as f:
    text = f.read()
print(text)

def shuffle_word(word):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    else:
        return word

words = text.split()
shuffled_words = [shuffle_word(word) for word in words]
transformed_text = ' '.join(shuffled_words)
print("\n"+transformed_text)
with open('poprehadzovany_text1.txt', 'w') as f:
    f.write(transformed_text)
