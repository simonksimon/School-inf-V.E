def spracuj_riadok(riadok):
    vystup=''
    cisla=map(int, riadok.split())
    for pocet in cisla:
        if vystup.endswith('1') or vystup == '':
            farba='0'
        else:
            farba='1'
        vystup+=(farba*pocet)
    return vystup

with open('dekompresia_obrazka_1.txt', 'r') as vstup:
    with open('dekompresia_obrazka_vystup.txt', 'w') as vystup:
        rozmery=vstup.readline().strip()
        vystup.write(rozmery+'\n')
        sirka, vyska=map(int, rozmery.split())
        pocet_bodov=sirka*vyska
        print(f'Šírka obrázka: {sirka}, Výška obrázka: {vyska}, Počet bodov: {pocet_bodov}')
        for riadok in vstup:
            riadok=riadok.strip()
            spracovany_riadok=spracuj_riadok(riadok)
            vystup.write(spracovany_riadok+'\n')