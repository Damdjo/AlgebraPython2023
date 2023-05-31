
import accounts






def sucelje(lista_izbora:list, izlaz:bool=False) -> None:
    
    if izlaz != True:

        for broj, opcija in enumerate(lista_izbora):
            print(f"\t{broj+1}. {opcija}")
    else:
        for broj, opcija in enumerate(lista_izbora):
            print(f"\t{broj+1}. {opcija}")
        print(f"\n \t0. Izlaz")








def main():
    
    while True:
        try: 
            prava, ime, prezime, logged_in, user, blocked = accounts.login()
        except TypeError:
            print("Unesen username/password nije ispravan")
            print()
            print("Pokušajte ponovno")
        else:
            if blocked == False:    
                match prava:
                    case "admin":
                        print("\n"*8)
                        print(f"Dobro došli, {ime} {prezime}\n")
                        
                        
                        while logged_in:
                            popis_opcija = ["Registracija", "Ispis korisnika", "Izmjena lozinke usera"]
                            

                            sucelje(popis_opcija, True)
                            izbor = int(input("Odaberite željenu opciju: "))
                            match izbor:
                                case 1:
                                    accounts.kreiraj_racun()
                                case 2:
                                    accounts.ispis_korisnika("admin")
                                case 3:
                                    accounts.promjeni_lozinku(user)
                                case 0:
                                    print("izlaz")
                                    logged_in = False
                                    break
                            print()
                        
                    case "korisnik":
                        print("\n"*8)
                        print(f"Dobro došli, {ime} {prezime}\n")
                        
                        
                        while logged_in:
                            popis_opcija = ["Izmjeni sifru"]
                            

                            sucelje(popis_opcija, True)
                            izbor = int(input("Odaberite željenu opciju: "))
                            match izbor:
                                case 1:
                                    accounts.promjeni_lozinku(user)
                                
                                case 0:
                                    print("izlaz")
                                    logged_in = False
                                    break
                            print()

                    case _:
                        print("Greška")
            else:
                continue

    

    









main()