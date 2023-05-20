# RACUN
# Racun je dio liste svih racuna (mozemo vise racuna jedan za drugim napraviti)
# Dodavanje proizvoda id ili opis, kolicina
# Ispis u obliku tablice: Stavka (1,2,3), Opis proizvoda, 
# Kolicina, Jed.cijena, Ukupno za stavku, Ukupno racun
# Izostaviti detalje poput PDV-a
# Ispis računa SMANJUJE stanje proizvoda u listi proizvoda za odgovarajuću količinu!

import moduli

stavke_na_racunu = []
counter = 1

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
         print("Error")
    

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
            elif kolicina < stanje:
                break
            else:
                print("Error")
    
    proizvod = {"redni broj":counter, 'id':id, 'opis':opis, 'cijena':cijena, "kolicina":kolicina, "ukupno":kolicina*cijena, "stanje":stanje}
    stavke_na_racunu.append(proizvod)
    counter += 1


def ispis_stavki(racun_lista:list) -> None:
    pass







def main():
    pass












if __name__ == "__main__":
    main()