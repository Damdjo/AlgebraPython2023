# RACUN
# Racun je dio liste svih racuna (mozemo vise racuna jedan za drugim napraviti)
# Dodavanje proizvoda id ili opis, kolicina
# Ispis u obliku tablice: Stavka (1,2,3), Opis proizvoda, 
# Kolicina, Jed.cijena, Ukupno za stavku, Ukupno racun
# Izostaviti detalje poput PDV-a
# Ispis računa SMANJUJE stanje proizvoda u listi proizvoda za odgovarajuću količinu!

import moduli, skladiste

svi_racuni = {}

stavke_na_racunu = []
counter = 1
counter_racuna = 1

def dodaj_stavku_na_racun(lista:list, lista_proizvoda:list) -> dict:
    """
    Funkcija koja će od unsenog id-a proizvoda povući opis i cijenu artikla te će od kupca tražiti unos količine na kraju se stavka sa podacima pretvara u dictionary te se dodaje listu\n
    lista -> lista u koju se dodaje artikl\n
    lista_proizvoda -> lista sa matičnim podatcima o proizvodima ( iz nje se izvlače opis, cijena, stanje prema unesenom id-u) 
        
    """

    #unos id, te provjera da već nije u artiklima
    global counter
    print(f"Unesite id {counter}. stavke: ")    
    while True:
        id = input("Unos: ")
        id_taken_check = moduli.check_if_id_taken(id,lista_proizvoda)
        match id_taken_check:
            case False:
                print(f"Id \"{id}\" ne postoji u tablici, pokušajte ponovno!")
            case True:
                # nakon što se unese artikl čiji id postoji u tablici ispisuje se njegov opis radi preglednosti
                proizvod_index = moduli.vrati_rijecnik(id,lista_proizvoda)
                proizvod_opis = lista_proizvoda[proizvod_index]["opis"]
                proizvod_dosputno = lista_proizvoda[proizvod_index]["stanje"]
                print(f"Odabrali ste {proizvod_opis}, na stanju ga ima {proizvod_dosputno}")
                #provjera ima li proizvnoda na stanju 
                check_stanje = lista_proizvoda[proizvod_index]["stanje"]
                if check_stanje <= 0:
                    print("Proizvoda nema na stanju!")
                    break
                else:
                    pass
       
                
                
                
                check_id = moduli.confirm()
                match check_id:
                    case True:
                        break
                    case False:
                        continue
                
       
           
       
    #
    
    #unos opisa
    
    for proizvod in lista_proizvoda:
            if id == proizvod["id"]:
                opis = proizvod["opis"]        
    

    #unos cijene
    for proizvod in lista_proizvoda:
            if id == proizvod["id"]:
                cijena = proizvod["cijena"]
    
    #unos stanje
    for proizvod in lista_proizvoda:
            if id == proizvod["id"]:
                stanje = proizvod["stanje"]
    if stanje == 0:
         moduli.enter_to_continue()
         return None
    

    #unos kolicine stavke na racunu
    for proizvod in lista_proizvoda:
        if id == proizvod["id"]:
            stanje = proizvod["stanje"]
    while True:
        try: 
            kolicina = int(input("Unesite traženu količinu stavke na računu: "))
        except ValueError:
            print ("Početno stanje mora biti iskazana kao cijeli broj!")
        else:           

            if kolicina > stanje:
                print(f"Unesena količina je veća od trenutnog stanja ({stanje})")
            elif kolicina <= stanje:
                skladiste.izmjeni_stanje(id,lista_proizvoda,False,kolicina*-1)
                break
            else:
                print("Error")
    
    proizvod = {"redni broj":counter, 'id':id, 'opis':opis, 'cijena':cijena, "kolicina":kolicina, "ukupno":round(kolicina*cijena,2), "stanje":stanje}
    stavke_na_racunu.append(proizvod)
    counter += 1

def vrati_stanje(lista_proizvoda:list):
    #[{'redni broj': 1, 'id': 'abc123', 'opis': 'Mlijeko Megle 250g', 'cijena': 18.9, 'kolicina': 132, 'ukupno': 2494.7999999999997, 'stanje': 132}]
    
    for stavka in stavke_na_racunu:
        stavka["stanje"] = skladiste.izmjeni_stanje(stavka["id"],lista_proizvoda,False,stavka["kolicina"])
    
    pass

def ispis_stavki() -> None:
    lista_stupci = ["Rb.", "Id","Opis", "Jed.cijena", "Kolicina", "Ukupno"]
    moduli.tablicaIspis(lista_stupci,stavke_na_racunu,lista_stupci,"racun")

def novi_racun(lista_proizvoda:list) -> list:
    """
    funkcija racun u listu "stavke_na_racunu" dodaje stavke pomoću funkcije "dodaj_stavku_na_racun"\n
    lista_proizvoda -> lista sa matičnim podatcima o proizvodima
    
    """
    global stavke_na_racunu, counter
    counter = 1
    stavke_na_racunu = []
    while True:
        print("\n"*20)
        ispis_stavki()
        print("\n"*15)
        nova_stavka = input("Želite li dodati novu stavku u račun? (da/ne): ")        
        match nova_stavka.capitalize():
            case "Da":
                dodaj_stavku_na_racun(stavke_na_racunu, lista_proizvoda)
            case "Ne":
                spremanje = input("Želite li spremiti trenutni račun? (da/ne)")
                match spremanje.capitalize():
                    case "Da":
                        spremanje_racuna(svi_racuni,stavke_na_racunu)
                        break
                    case "Ne":
                        vrati_stanje(lista_proizvoda)
                        break
                    case _:
                        pass




            case _:
                print("Error")

def spremanje_racuna(popis_racuna:dict, racun:list) -> None:
    """
    Funkcija će u tuple "popis_racuna" spremiti listu "racun"\n

    popis_racuna -> dictionary u koji će biti spremljena lista iz 2. argumenta, koristi se dict kojem će ključ biti redni broj računa, a vrijednost lista sa svim stavkama racuna\n
    racun -> lista dobivena korištenjem funkcije "novi_racun"
    

    """
    global counter_racuna

    lista = racun

    popis_racuna[counter_racuna] = lista
    counter_racuna += 1




def main():
    pass












if __name__ == "__main__":
    main()