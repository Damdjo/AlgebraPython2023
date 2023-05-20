# SKLADISTE - ULAZ
# Logiranje s korisnickim imenom-lozinkom (ulaz-ulaz)
# Meni: Stanje, Stanje po proizvodu (upit), Dodaj proizvod, Izmjeni stanje (dodaj-oduzmi), Logout

#import moduli,proizvodi
import moduli

# proizvod={'id':'abc123', 'opis':'Maslo Megle 250g', 'cijena':18.90, 'stanje':132}

def stanje_id(id:str,lista_proizvoda:list) -> int:
    "funkcija vraća stanje artikla sa unesenim id-em"
    
    for proizvod in lista_proizvoda:
        if id == proizvod["id"]:
            opis = proizvod["opis"]
            stanje = proizvod["stanje"]
            print(f"Stanje proizvoda {opis} je: {stanje}")

def izmjeni_stanje(id:str,lista_proizvoda:list, manual:bool=True, auto_broj:int=None) -> int:
    """
    funkcija izmjenjuje stanje proizvoda iz unesene liste proizvoda čiji je id unesen, manual je True/False te se odnosi na ručno(True) ili automatso izvršavanje funkcije(False)\n
    id -> id proizvoda kojeg mijenjamo\n
    lista_proizvoda -> lista u kojoj tražimo id proizvoda\n
    manual -> može biti - True  -> funkcija traži ručan unos podataka
                                -> funkcije ne traži nikakav input od korisnika ( koristi se za smanjivanje stanja u računu)


    
    
    """

    if manual == True:
        for proizvod in lista_proizvoda:
            if id == proizvod["id"]:
                stanje = proizvod["stanje"]
                stanje_bu = stanje
                proizvod = proizvod["opis"]
                print(f"Trenutno stanje proizvoda \" {proizvod} \" je: {stanje}")
                izmjena = input("Želite li izmjeniti stanje navedenog proizvoda? (Da / Ne): ")
                match izmjena.capitalize():
                    case "Da":
                        #proizvod["stanje"] = int(input("Unesite željeno stanje proizvoda: "))
                        artikl_za_izmjenu = moduli.vrati_rijecnik(id, lista_proizvoda)                    
                        stanje = int(input("Unesite stanje: "))
                        lista_proizvoda[artikl_za_izmjenu]["stanje"] = stanje
                        print(f"Želite li stanje proizvoda \" {proizvod} \" izmjenniti sa: {stanje_bu}  na: {stanje}")
                        check = moduli.confirm()

                        #funkcija check iz modula koja shodno vraćenoj vrijednosti potvrđuje ili poništava izmjenu stanja
                        match check:
                            case True:
                                print(f"Stanje proizvoda \" {proizvod} \" je izmjenjeno sa: {stanje_bu}  na: {stanje}")
                            case False:
                                lista_proizvoda[artikl_za_izmjenu]["stanje"] = stanje_bu
                                print(f"Stanje proizvoda je vraćeno na prvobitno ({stanje_bu}))")


                                        
                    case "Ne":
                        print("Stanje proizvoda nije izmjenjeno")
                    case _:
                        print("Krivi unos!")
    else:
        for proizvod in lista_proizvoda:
            if id == proizvod["id"]:
                
                stanje = proizvod["stanje"]
                artikl_za_izmjenu = moduli.vrati_rijecnik(id, lista_proizvoda)
                stanje = stanje + auto_broj
                lista_proizvoda[artikl_za_izmjenu]["stanje"] = stanje




                

            
def dodaj_proizvod(lista:list) -> None:
    """
    lista -> lista u koju se dodaje artikl ( u ovom programu se radi o listi asortiman u datoteci asortiman.py)
        
    """

    #unos id, te provjera da već nije u artiklima
    print("Unesite id za novi artikl: ")    
    while True:
        id = input("Unos: ")
        id_taken_check = moduli.check_if_id_taken(id,lista)
        match id_taken_check:
            case True:
                print(f"Id \"{id}\" već postoji, pokušajte ponovno!")
            case False:
                check_id = moduli.confirm()
                match check_id:
                    case True:
                        break
                    case False:
                        continue
                
            
            case _:
                print("Greška")
    #
    
    #unos opisa
    
    while True:
        opis = input("Unesite naziv artikla: ")
        check_opis = moduli.confirm()
        match check_opis:
            case True:
                break
            case False:
                pass
            case _:
                print("Greška")
    

    #unos cijene, provjera da je unesena kao float i potvrda
    while True:
        try: 
            cijena = float(input("Unesite cijenu za artikl: "))
        except ValueError:
            print ("Cijena mora biti brojčano iskazana, decimale se odvajaju točkom ( . )")
        else:
            check_cijena = moduli.confirm()
            match check_cijena:
                case True:
                    break
                case False:
                    pass
                case _:
                    print("Greška")
    

    #unos početnog stanja, provjera da je unesena kao broj i potvrda
    while True:
        try: 
            poc_stanje = int(input("Unesite početno stanje artikla: "))
        except ValueError:
            print ("Početno stanje mora biti brojčano iskazana")
        else:
            if poc_stanje > 0:
                check_poc_stanje = moduli.confirm()
                match check_poc_stanje:
                    case True:
                        break
                    case False:
                        pass
                    case _:
                        print("Greška")
            else:
                print("Početno stanje mora biti veće od 0")
    
    proizvod = {'id':id, 'opis':opis, 'cijena':cijena, 'stanje':poc_stanje}
    
    



def main():
    pass
    
    
    
          
    

















if __name__ == "__main__":
    main()