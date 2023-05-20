import accounts,asortiman,moduli,proizvodi,skladiste



def main():

    user = accounts.login()

    if user == "skladiste":
        while True:
            izbori = ["Ispis tablice sa proizvodima", "Provjera stanja proizvoda po id-u", "Izmjena stanja proizvoda po id-u", "Dodavanje novog proizvoda", ]
            moduli.sucelje(izbori)
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
                    break

            
    
    






















main()