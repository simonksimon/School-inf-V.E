secret_table = {
    '0': ' ',
    '1': 'ABC',
    '2': 'DEF',
    '3': 'GHI',
    '4': 'JKL',
    '5': 'MNO',
    '6': 'PQR',
    '7': 'STU',
    '8': 'VWX',
    '9': 'YZ'
}

def encrypt_text(text: str) -> str:
    encrypted_text = ''
    for char in text:
        for key in secret_table:
            if char in secret_table[key]:
                index = secret_table[key].index(char)
                encrypted_text += key * (index + 1) + ' '
                break
    return encrypted_text.strip()

input_text = input('Zadajte text na zašifrovanie: ')
encrypted_text = encrypt_text(input_text.upper())
print(f'Zašifrovaný text: {encrypted_text}')

freq_dict = {}
for num in encrypted_text:
    if num != ' ':
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

if freq_dict:
    max_freq = max(freq_dict.values())
    most_frequent_nums = [num for num, freq in freq_dict.items() if freq == max_freq]
    print(f'Najčastejšie zvolené políčka: {", ".join(most_frequent_nums)}')
else:
    print('Šifrovaný text neobsahuje žiadne čísla.')