# Vytvorte slovník pre každú krajinu
krajiny = {}

# Otvorte súbor a pre každý riadok v súbore:
with open('skok_do_dialky.txt', 'r') as f:
    for line in f:
        # Rozdeľte riadok na mená a výkony
        mena_vykonov = line.split()
        # Získajte kód krajiny
        kod_krajiny = mena_vykonov[1]
        # Ak kód krajiny ešte nie je v slovníku, pridajte ho
        if kod_krajiny not in krajiny:
            krajiny[kod_krajiny] = 0
        # Pridajte jedného súťažiaceho pre danú krajinu
        krajiny[kod_krajiny] += 1

# Vypíšte zoznam krajín
print("Zoznam krajín, z ktorých boli športovci účastníkmi súťaže:")
for kod_krajiny in sorted(krajiny.keys()):
    print(kod_krajiny)

# Vypíšte počty súťažiacich z jednotlivých krajín
print("\nPočty súťažiacich z jednotlivých krajín:")
for kod_krajiny in sorted(krajiny.keys()):
    pocet_sutaziacich = krajiny[kod_krajiny]
    print(f"{kod_krajiny}: {pocet_sutaziacich}")

# Nájdite víťaza
vysledky = {}
with open('skok_do_dialky.txt', 'r') as f:
    for line in f:
        mena_vykonov = line.split()
        meno = mena_vykonov[0]
        najlepsi_vysledok = max([int(x) for x in mena_vykonov[2:]])
        vysledky[meno] = najlepsi_vysledok

# Vypíšte víťaza alebo víťazov
max_vysledok = max(vysledky.values())
vitazi = [meno for meno, vysledok in vysledky.items() if vysledok == max_vysledok]
if len(vitazi) == 1:
    print(f"\nMeno celkového víťaza – kto skočil najďalej:\n- {vitazi[0]}")
else:
    print("\nMeno celkového víťaza – kto skočil najďalej:")
    for vitaz in vitazi:
        print(f"- {vitaz}")