pocitadla={str(i): [] for i in range(5220, 5230)}
celkovy_pocet_sms=0

with open('hlasovanie_1.txt', 'r') as vstup:
    for poradie, cislo in enumerate(vstup, start=1):
        cislo=cislo.strip()
        if cislo in pocitadla:
            pocitadla[cislo].append(str(poradie))
            celkovy_pocet_sms+=1
print(f'Celkový počet zaslaných SMS: {celkovy_pocet_sms}')

for cislo, poradia in pocitadla.items():
    with open(f'{cislo}.txt', 'w') as subor:
        subor.write('\n'.join(poradia))