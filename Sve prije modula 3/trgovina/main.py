import accounts,asortiman,moduli,skladiste,racun,admin



def main():


    while True:
        init_izbor_lista = ["Ulaz u korisnički račun"]
        moduli.sucelje(init_izbor_lista,True,False,"trgovina")

        init_izbor = moduli.input_validation()
            
        
        match init_izbor:
            
            case 1:
                user, logged_in = accounts.login()
                print("\n"*25)
                while logged_in:    
                    if user == "skladiste":
                        while True:
                            izbori = ["Ispis tablice sa proizvodima", "Provjera stanja proizvoda po id-u", "Izmjena stanja proizvoda po id-u", "Dodavanje novog proizvoda"]
                            moduli.sucelje(izbori,False,True,user)
                            print("")
                            izbor = moduli.input_validation()

                            match izbor:
                                case 1:
                                    print("\n"*25)
                                    moduli.tablicaIspis(None,asortiman.asortiman,None,"full")
                                    print()                                    
                                    moduli.enter_to_continue()
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
                                    print("\n"*25)
                                    break

                    if user == "prodaja":
                        while True:
                            izbori = ["Novi račun", "Ispis trenutnog računa", "Ispis spremljenog računa"]
                            moduli.sucelje(izbori,False,True,user)
                            print("")
                            izbor = moduli.input_validation()

                            match izbor:
                                case 1:
                                    racun.novi_racun(asortiman.asortiman)
                                case 2:
                                    racun.ispis_stavki()
                                    
                                case 3:
                                    print("Unesite id računa koji želite ispisati: ")
                                    id_racuna = moduli.input_validation()
                                    racun.ispis_racuna(id_racuna,True)
                                    print("\n")
                                    moduli.enter_to_continue()
                                    
                                case 4:
                                    print(racun.svi_racuni)

                                case 0:
                                    logged_in = accounts.logout()
                                    print("\n"*25)
                                    break
                    if user == "admin":
                        while True:
                            izbori = ["Ispis stanja svih proizvoda","Broj izdanih racuna","Ukupan promet", ]
                            moduli.sucelje(izbori,False,True,user)
                            print("")
                            izbor = moduli.input_validation()

                            match izbor:
                                case 1:
                                    print("\n"*25)                                                                       
                                    moduli.tablicaIspis(None,asortiman.asortiman,asortiman.asortiman,"stanje")
                                    print()                                    
                                    moduli.enter_to_continue()
                                
                                case 2:
                                    print("\n"*25) 
                                    admin.koliko_racuna(racun.counter_racuna)
                                    print()
                                    moduli.enter_to_continue()
                                
                                case 3:
                                    sav_promet = admin.promet(racun.svi_racuni)
                                    match sav_promet:
                                        case 0:
                                            print("Još nije bilo prometa!")
                                        case _:
                                            print(f"Ukupno je bilo {sav_promet} € prometa.")
                                    
                                case 4:
                                    pass

                                case 0:
                                    logged_in = accounts.logout()
                                    print("\n"*25)
                                    break

            case 0:
                print("Hvala na korištenju")
                break       

    
    






















main()