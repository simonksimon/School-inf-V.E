secret_table = {'0': ' ', '1': 'ABC', '2': 'DEF', '3': 'GHI', '4': 'JKL', '5': 'MNO', '6': 'PQR', '7': 'STU', '8': 'VWX', '9': 'YZ'}
text = input('Zadajte text na zašifrovanie: ')
encryption = ''
for char in text:
    for key in secret_table:
        if char in secret_table[key]:
            index = secret_table[key].index(char)
            encryption += key * (index + 1) + ' '
            break
encryption = encryption.strip()
print(f'Zašifrovaný text: {encryption}')

count = {}
for num in encryption:
    if num != ' ':
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
maxc = max(count.values())
maxresult = [num for num, freq in count.items() if freq == maxc]
print(f'Najčastejšie zvolené políčka: {", ".join(maxresult)}')