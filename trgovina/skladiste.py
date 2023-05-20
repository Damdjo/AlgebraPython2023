# SKLADISTE - ULAZ
# Logiranje s korisnickim imenom-lozinkom (ulaz-ulaz)
# Meni: Stanje, Stanje po proizvodu (upit), Dodaj proizvod, Izmjeni stanje (dodaj-oduzmi), Logout

#import moduli,proizvodi
from asortiman import asortiman
import moduli

# proizvod={'id':'abc123', 'opis':'Maslo Megle 250g', 'cijena':18.90, 'stanje':132}

def stanje_id(id:str) -> int:
    
    for proizvod in asortiman:
        if id == proizvod["id"]:
            print(proizvod["stanje"])

def izmjeni_stanje(id:str) -> int:
    global asortiman
    
    for proizvod in asortiman:
        if id == proizvod["id"]:
            stanje = proizvod["stanje"]
            proizvod = proizvod["opis"]
            print(f"Trenutno stanje proizvoda \" {proizvod} \" je: {stanje}")
            izmjena = input("Želite li izmjeniti stanje navedenog proizvoda? (Da / Ne): ")
            match izmjena.capitalize():
                case "Da":
                    #proizvod["stanje"] = int(input("Unesite željeno stanje proizvoda: "))
                     artikl_za_izmjenu = moduli.vrati_rijecnik(id, asortiman)
                     stanje = int(input("Unesite stanje: "))
                     asortiman[artikl_za_izmjenu]["stanje"] = stanje
                case "Ne":
                    print("Izlaz")
                case _:
                    print("Krivi unos!")
            print(f"Trenutno stanje proizvoda \" {proizvod} \" je: {stanje}")



def main():
    #stanje_id("abc123")
    #izmjeni_stanje("83418247")

















if __name__ == "__main__":
    main()