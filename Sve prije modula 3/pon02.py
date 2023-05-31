"""
brojevi = []

for broj in range(100,151):
    brojevi.append(broj)

trazeniBroj = int(input("Unesite broj za provjeru"))

for broj in brojevi:
    if broj == trazeniBroj:
        print(f"Našli stmo broj {trazeniBroj}")

if trazeniBroj in brojevi:
    print(f"Našli stmo broj {trazeniBroj}")
"""

dani = ["pon", "uto", "sri", "cet", "pet", "sub", "ned"]

radniDani = []
for dan in dani:
    if dan != "sub":
        radniDani.append(dan)
    else:
        break
print(radniDani)

radniDaniSlice = dani[:5:2]
print(radniDaniSlice)