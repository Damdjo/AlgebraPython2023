import os, racuni, moduli    






def main():
    izbori = ["Informacije o računu", "Prikaz stanja računa", "Prikaz prometa po računu", "Uplata na račun", "Isplata sa računa"]
    
    while True:
        os.system("cls")
        
        moduli.meni(None,"glavni izbornik")


        if racuni.baza_racuni == []:
            moduli.init()
            racuni.kreiraj_racun()
            for racun in racuni.baza_racuni:
                trenutni_racun = racun["Broj Računa"]
            print() 
            datum, izmjena = racuni.mijenjaj_saldo(trenutni_racun, True)
            racuni.zapis_transakcija(datum, izmjena)
            os.system("cls")
            moduli.meni(izbori,"glavni izbornik", True)

        else:
            os.system("cls")
            moduli.meni(izbori,"glavni izbornik", True)

        for racun in racuni.baza_racuni:
            trenutni_racun = racun["Broj Računa"]
        
        
        
        try:
            izbor = int(input("Vaš izbor: \t"))
        except:
            print("error")

        else:
            match izbor:
                case 1:
                    os.system("cls")
                    moduli.meni(None,"INFORMACIJE O RAČUNU")
                    racuni.info_o_racunu(trenutni_racun)
                    print()
                    moduli.enter_to_continue()
                    
                case 2:
                    os.system("cls")
                    moduli.meni(None,"PRIKAZ STANJA")
                    racuni.prikaz_stanja(trenutni_racun)
                    print()
                    moduli.enter_to_continue()
                case 3:
                    os.system("cls")
                    moduli.meni(None,"PRIKAZ PROMETA")
                    promet = racuni.transakcije
                    
                    for key, value in promet.items():
                        print(f"{key} \t{value}")
                        print()
                    moduli.enter_to_continue()
                case 4:
                    os.system("cls")
                    moduli.meni(None,"UPLATA")
                    datum, izmjena = racuni.mijenjaj_saldo(trenutni_racun,False,"uplata")
                    racuni.zapis_transakcija(datum, izmjena)
                    print()
                    moduli.enter_to_continue()
                case 5:
                    os.system("cls")
                    moduli.meni(None,"ISPLATA")
                    datum, izmjena = racuni.mijenjaj_saldo(trenutni_racun,False,"isplata")
                    racuni.zapis_transakcija(datum, izmjena)
                    print()
                    moduli.enter_to_continue()
                case 0:
                    break

    print("Hvala na korištenju")

    












main()