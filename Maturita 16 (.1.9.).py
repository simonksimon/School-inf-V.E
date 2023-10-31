# Otvorte súbor a načítajte všetky riadky
with open('mena_zamestnancov.txt', 'r') as f:
    lines = f.readlines()

# Vypíšte počet mien v súbore
pocet_mien = len(lines) // 2
print(f"Počet mien v súbore: {pocet_mien}")

# Nájdite najdlhšie krstné meno a najdlhšie priezvisko
najdlhsie_krstne_meno = max([len(line.strip()) for line in lines[:pocet_mien]])
najdlhsie_priezvisko = max([len(line.strip()) for line in lines[pocet_mien:]])

# Vytvorte výsledný súbor vystup.txt
with open('vystup.txt', 'w') as f:
    for i in range(pocet_mien):
        # Získajte krstné meno a priezvisko z prvej a druhej polovice riadkov
        krstne_meno = lines[i].strip()
        priezvisko = lines[i + pocet_mien].strip()
        # Zapíšte meno a priezvisko do súboru vystup.txt
        f.write(f"{krstne_meno}{' ' * (najdlhsie_krstne_meno - len(krstne_meno))} {priezvisko}{' ' * (najdlhsie_priezvisko - len(priezvisko))}\n")

# Vypíšte dĺžku najdlhšieho krstného mena a najdlhšieho priezviska
print(f"Dĺžka najdlhšieho krstného mena: {najdlhsie_krstne_meno}")
print(f"Dĺžka najdlhšieho priezviska: {najdlhsie_priezvisko}")