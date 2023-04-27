import random

"""broj=random.randint(1,3)
print(broj)"""

# imamo 2 igrača, jedan live (covjek) i jedan račinalni (random)
# računalo će odabrati jednu opciju (od 1 do 3), baš kao i mi
#ako smo "jači", dobili smo, ako smo slabiji, izgubili, a ako imamo jednako, onda ponavljamo

izbornik = """
    Izbornik opcija (upišite broj ispred opcije)
    1. Kamen
    2. Škare
    3. Papir
    0. Izlaz

    """

listaOpcija = ["", "Kamen", "Škare", "Papir"]
bodoviKorisnik = 0
bodoviRacunalo = 0

while True:
    izborRacunalo=random.randint(1,3)
    while True:
        print(izbornik)
        izborKorisnik = int(input("Izaberite broj ispred opcije: "))
        if izborKorisnik == 0:
            print("Izlaz")
            print(f"Bodovi računala su {bodoviRacunalo}, a korisnika {bodoviKorisnik}")
            status = False
            break        
        elif izborKorisnik >= 1 and izborKorisnik <= 3:
            break
        print("Pogrešan unos! ")

    #print("Nastavak")
    if izborKorisnik == 0:            
            status = False
            break  
    elif izborKorisnik == izborRacunalo:
        print(f"\nNeriješeno, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        
    elif izborKorisnik == 2 and izborRacunalo == 1:
        print(f"\nIzgubili ste, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        bodoviRacunalo += 1
    elif izborKorisnik == 3 and izborRacunalo == 2:
        print(f"\nIzgubili ste, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        bodoviRacunalo += 1
    elif izborKorisnik == 1 and izborRacunalo == 3:
        print(f"\nIzgubili ste, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        bodoviRacunalo += 1
    elif izborKorisnik == 1 and izborRacunalo == 2:
        print(f"\nPobijedili ste, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        bodoviKorisnik += 1
    elif izborKorisnik == 2 and izborRacunalo == 3:
        print(f"\nPobijedili ste, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        bodoviKorisnik += 1
    elif izborKorisnik == 3 and izborRacunalo == 1:
        print(f"\nPobijedili ste, izbor računala je {listaOpcija[izborRacunalo]}, a vaš {listaOpcija[izborKorisnik]}")
        bodoviKorisnik += 1
