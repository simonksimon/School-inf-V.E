def spracuj_riadok(riadok):
    vystup = ''
    cisla = map(int, riadok.split())
    for pocet in cisla:
        farba = '0' if vystup.endswith('1') or vystup == '' else '1'
        vystup += (farba * pocet)
    return vystup


def dekompresuj_obrazok(vstupny_subor, vystupny_subor):
    with open(vstupny_subor, 'r') as vstup, open(vystupny_subor, 'w') as vystup:
        rozmery = vstup.readline().strip()
        vystup.write(rozmery + '\n')
        sirka, vyska = map(int, rozmery.split())
        pocet_bodov = sirka * vyska
        print(f'Šírka obrázka: {sirka}, Výška obrázka: {vyska}, Počet bodov: {pocet_bodov}')

        for riadok in vstup:
            riadok = riadok.strip()
            spracovany_riadok = spracuj_riadok(riadok)
            vystup.write(spracovany_riadok + '\n')


# Príklad použitia:
dekompresuj_obrazok('dekompresia_obrazka_1.txt', 'dekompresia_obrazka_vystup.txt')