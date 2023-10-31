# Načítanie vety zo vstupu
veta = input("Zadajte vetu: ")

# Vytvorenie tajnej tabuľky ako slovníka
tajna_tabulka = {
    0: " ",
    1: "ABC",
    2: "DEF",
    3: "GHI",
    4: "JKL",
    5: "MNO",
    6: "PQR",
    7: "STU",
    8: "VWX",
    9: "YZ"
}

# Zašifrovanie vety na čísla políčok
zasifrovana_veta = ""
for pismeno in veta:
    for cislo, znaky in tajna_tabulka.items():
        if pismeno in znaky:
            # Ak je písmeno druhé alebo tretie z políčka, zopakovať číslo políčka
            opakovanie = znaky.index(pismeno) + 1
            zasifrovana_veta += str(cislo) * opakovanie + " "
            break

# Výpis zašifrovanej vety na obrazovku
print("Zašifrovaná veta je:", zasifrovana_veta)

# Zistenie najčastejšieho čísla políčka v šifre
pocetnosti = {}
for cislo in zasifrovana_veta:
    if cislo != " ":
        pocetnosti[cislo] = pocetnosti.get(cislo, 0) + 1

max_pocetnost = max(pocetnosti.values())
najcastejsie_policka = [cislo for cislo, pocetnost in pocetnosti.items() if pocetnost == max_pocetnost]

# Výpis najčastejšieho čísla políčka na obrazovku
print("Najčastejšie zvolené políčka:", ", ".join(najcastejsie_policka))