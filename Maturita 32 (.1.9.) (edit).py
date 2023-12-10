def spracuj_riadok(riadok):
    vystup=''
    for i in range(0, len(riadok), 2):
        pixel=riadok[i:i+2]
        if int(pixel, 16)<128:
            vystup+='0 '
        else:
            vystup+='1 '
    return vystup.strip()

with open('ciernobiely_obrazok_1.txt','r') as vstup:
    with open('konverzia_suboru_1_vystup.txt','w') as vystup:
        rozmery=vstup.readline().strip()
        vystup.write(rozmery+'\n')
        sirka, vyska=map(int,rozmery.split())
        pocet_bodov=sirka*vyska
        print(f'Šírka obrázka: {sirka}, Výška obrázka: {vyska}, Počet bodov: {pocet_bodov}')
        for riadok in vstup:
            riadok=riadok.strip()
            spracovany_riadok=spracuj_riadok(riadok)
            vystup.write(spracovany_riadok+'\n')