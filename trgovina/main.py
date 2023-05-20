import accounts,asortiman,moduli,skladiste,racun



def main():

    user, logged_in = accounts.login()
    while logged_in:    
        if user == "skladiste":
            while True:
                izbori = ["Ispis tablice sa proizvodima", "Provjera stanja proizvoda po id-u", "Izmjena stanja proizvoda po id-u", "Dodavanje novog proizvoda"]
                moduli.sucelje(izbori,False,True,user)
                print("")
                izbor = int(input("Unesite željenu opciju: "))

                match izbor:
                    case 1:
                        
                        moduli.tablicaIspis(None,asortiman.asortiman,None,"full")
                    case 2:
                        id = input("Unesite id proizvoda kojem provjeravate stanje: ")
                        print()
                        skladiste.stanje_id(id,asortiman.asortiman)

                    case 3:
                        id = input("Unesite id proizvoda kojem mijenjate stanje: ")
                        print()
                        skladiste.izmjeni_stanje(id,asortiman.asortiman)
                    
                    case 4:
                        skladiste.dodaj_proizvod(asortiman.asortiman)
                    
                    
                    
                
                    case 0:
                        logged_in = accounts.logout()
                        break

        if user == "prodaja":
            while True:
                izbori = ["Unos stavke na račun", "Ispis trenutnog računa", "PLACEHOLDER"]
                moduli.sucelje(izbori,False,True,user)
                print("")
                izbor = int(input("Unesite željenu opciju: "))

                match izbor:
                    case 1:
                        racun.dodaj_stavku_na_racun(racun.stavke_na_racunu,asortiman.asortiman)

                    case 2:
                        lista_stupci = ["Rb.", "Id","Opis", "Jed.cijena", "Kolicina", "Ukupno"]
                        moduli.tablicaIspis(lista_stupci,racun.stavke_na_racunu,lista_stupci,"racun")

    
    






















main()