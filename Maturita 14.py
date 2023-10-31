krajiny = {}
vysledky = {}
f = open('skok_do_dialky.txt', 'r')
for line in f:
    mena_vykonov = line.split()
    kraj = mena_vykonov[1]
    if kraj not in krajiny:
        krajiny[kraj] = 0
    krajiny[kraj] += 1

    mena_vyk = line.split()
    meno = mena_vyk[0]
    najlepsi = max([int(x) for x in mena_vyk[2:]])
    vysledky[meno] = najlepsi

print("Krajiny, z ktorých boli športovci v súťaži:")
for kraj in sorted(krajiny.keys()):
    print(kraj)

print("\nPočty súťažiacich z jednotlivých krajín:")
for kraj in sorted(krajiny.keys()):
    poc_sut = krajiny[kraj]
    print(f"{kraj}: {poc_sut}")

maxvys = max(vysledky.values())
vitazi = [meno for meno, vysledok in vysledky.items() if vysledok == maxvys]
print("\nMeno/ná celkového/vých víťaza/zov ktorý/rí skočil(i) najďalej:")
if len(vitazi) == 1:
    print(f"- {vitazi[0]}")
else:
    for vitaz in vitazi:
        print(f"- {vitaz}")