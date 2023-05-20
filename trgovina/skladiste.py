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
            stanje_bu = stanje
            proizvod = proizvod["opis"]
            print(f"Trenutno stanje proizvoda \" {proizvod} \" je: {stanje}")
            izmjena = input("Želite li izmjeniti stanje navedenog proizvoda? (Da / Ne): ")
            match izmjena.capitalize():
                case "Da":
                    #proizvod["stanje"] = int(input("Unesite željeno stanje proizvoda: "))
                    artikl_za_izmjenu = moduli.vrati_rijecnik(id, asortiman)
                    stanje = int(input("Unesite stanje: "))
                    asortiman[artikl_za_izmjenu]["stanje"] = stanje
                    print(f"Želite li stanje proizvoda \" {proizvod} \" izmjenniti sa: {stanje_bu}  na: {stanje}")
                    check = moduli.confirm()

                    #funkcija check iz modula koja shodno vraćenoj vrijednosti potvrđuje ili poništava izmjenu stanja
                    match check:
                        case True:
                            print(f"Stanje proizvoda \" {proizvod} \" je izmjenjeno sa: {stanje_bu}  na: {stanje}")
                        case False:
                            asortiman[artikl_za_izmjenu]["stanje"] = stanje_bu
                            print(f"Stanje proizvoda je vraćeno na prvobitno ({stanje_bu}))")


                                       
                case "Ne":
                    print("Stanje proizvoda nije izmjenjeno")
                case _:
                    print("Krivi unos!")
            



def main():
    #stanje_id("abc123")
    izmjeni_stanje("83418247")

















if __name__ == "__main__":
    main()