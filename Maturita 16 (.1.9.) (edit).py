f = open('mena_zamestnancov.txt', 'r')
lines = f.readlines()

pocet = len(lines) // 2
print(f"Počet mien v súbore: {pocet}")

naj_km = max([len(line.strip()) for line in lines[:pocet]])
naj_p = max([len(line.strip()) for line in lines[pocet:]])
print(f"Dĺžka najdlhšieho krstného mena: {naj_km}")
print(f"Dĺžka najdlhšieho priezviska: {naj_p}")

with open('vystup.txt', 'w') as nf:
    for i in range(pocet):
        km = lines[i].strip()
        p = lines[i + pocet].strip()
        nf.write(f"{km}{' ' * (naj_km - len(km))} {p}{' ' * (naj_p - len(p))}\n")