def vytvor_subory_hlasovania(vstupny_subor):
    # Inicializácia počítadiel pre každé telefónne číslo
    pocitadla = {str(i): [] for i in range(5220, 5230)}
    celkovy_pocet_sms = 0

    with open(vstupny_subor, 'r') as vstup:
        for poradie, cislo in enumerate(vstup, start=1):
            cislo = cislo.strip()
            if cislo in pocitadla:
                pocitadla[cislo].append(str(poradie))
                celkovy_pocet_sms += 1

    # Vypíše celkový počet zaslaných SMS
    print(f'Celkový počet zaslaných SMS: {celkovy_pocet_sms}')

    # Vytvorenie súborov pre každé telefónne číslo
    for cislo, poradia in pocitadla.items():
        with open(f'{cislo}.txt', 'w') as subor:
            subor.write('\n'.join(poradia))

# Príklad použitia:
vytvor_subory_hlasovania('hlasovanie_1.txt')