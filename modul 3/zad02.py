"""
mate={
    "OIB":12345678910,
    "ime": "Mate",
    "spol": "M"
}

lista_ljudi = [mate,mate,mate]

print(lista_ljudi)
"""

class TelevizijskiAparat():
    """ Tevelizor """
    dijagonala = 55
    sirina = 124
    visina = 79
    proizvodac = "Grundig"
    model = "Extra55"
    
    je_ukljucen = False

    def ukljuci(self):
        self.je_ukljucen = True
        


tv_dnevni_boravak = TelevizijskiAparat()
print()
print(f"Proizvođač: {tv_dnevni_boravak.proizvodac}")
print(f"Dijagonala: {tv_dnevni_boravak.dijagonala}")
print("\n\n")

if tv_dnevni_boravak.je_ukljucen:
    print(f"Status: TV u dnevnom je uključen")
else:
    print(f"Status: TV u dnevnom je isključen")

tv_dnevni_boravak.ukljuci()

if tv_dnevni_boravak.je_ukljucen:
    print(f"Status: TV u dnevnom je uključen")
else:
    print(f"Status: TV u dnevnom je isključen")
    
"""
tv_soba = TelevizijskiAparat()
print()
print(f"Proizvođač: {tv_soba.proizvodac}")
print(f"Dijagonala: {tv_soba.dijagonala}")
print("\n\n")

"""