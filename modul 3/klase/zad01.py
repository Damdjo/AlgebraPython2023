
def dodaj_racun():
    global racuni_broj_counter,racun_stavke,svi_racuni,racun_iznos_pdv
    
    
    novi_broj_racun = racun_broj[:2] + str(racuni_broj_counter) + racun_broj[4:] 
    datum = int(racun_datum_izdavanja[4])
    novi_datum = racun_datum_izdavanja[:4] + str(datum+1) + racun_datum_izdavanja[6:] 
    for stavka in racun_stavke.values():
        stavka += 50
    racun_ukupan_iznos = 0
    for stavka in racun_stavke.values():
        racun_ukupan_iznos += stavka
    racun_iznos_pdv = racun_ukupan_iznos * 0.25
    svi_racuni[racuni_broj_counter] = {"Račun broj":novi_broj_racun,"Datum izdavanja računa":novi_datum,"Stavke":racun_stavke,"Iznos PDV":racun_iznos_pdv,"Ukupna cijena":racun_ukupan_iznos}
    racuni_broj_counter += 1



svi_racuni = {}
racuni_broj_counter = 1



racun_broj = "R-1-2021-01"
racun_datum_izdavanja = "31.02.2021"

racun_stavke = {
    "Laptop": 368.80,
    "Torba za laptop": 39.99,
    "Monitor": 160.40,
    "Office licenca": 20.99
}

racun_ukupan_iznos = 0

for stavka in racun_stavke.values():
    racun_ukupan_iznos += stavka

racun_iznos_pdv = racun_ukupan_iznos * 0.25













#ispis racuna
"""
for racun in svi_racuni.items:
    print("\n\n")
    print("*"*50)
    print(f"\n\tRAČUN: \t\t {racun_broj}")
    print(f"\tDATUM: \t\t{racun_datum_izdavanja}\n")

    print("-"*50)
    print(f"\n\tProizvod\t\tCijena\n")
    for proizvod, cijena in racun_stavke.items():
        if len(proizvod) < 10:
            print(f"\t{proizvod}\t\t\t{cijena} €")
        elif len(proizvod) < 18:
            print(f"\t{proizvod}\t\t{cijena} €")
        else:
            print(f"\t{proizvod}\t{cijena} €")
    print("\n")
    print("-"*50)
    print(f"\n\IZNOS PDV: \t {racun_iznos_pdv:2f}")
    print(f"\nUKUPAN IZNOS: \t\t {racun_ukupan_iznos+racun_iznos_pdv:2f}")
    """


for broj in range(3):
    dodaj_racun()
print(svi_racuni)

