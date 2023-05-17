potrosnjaPo100km = float(input("Unesite potrošnju automobila na 100km: "))
cijenaLGoriva = float(input("Unesite cijenu litre goriva: "))
udaljenostDoPosla = float(input("Unesite udaljenost do posla u Km: "))
brojDanaUMjesecu = int(input("Unesite broj dana u mjesecu: "))

cijenaPoKm = potrosnjaPo100km *  cijenaLGoriva * 2
mjesecniTrosak = cijenaPoKm * udaljenostDoPosla * brojDanaUMjesecu

print(f"Cijena goriva po Km udaljenosti je {cijenaPoKm} €")
print(f"Trošak prijevoza u mjesecu od {brojDanaUMjesecu} dana je {mjesecniTrosak}")

