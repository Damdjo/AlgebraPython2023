# a. Kreiranje računa Tvrtke+++
# Tvrtka ima podatke: Naziv, Ulica i broj, Poštanski broj sjedišta, Grad sjedišta, +++
# OIB (mora imati točno 11 znakova), Ime i prezime odgovorne osobe.+++
# i. Kod otvaranja računa treba položiti iznos po volji+++
# ii. Treba odabrati valutu računa EUR ili HRK//////
# iii. Račun generirati broj računa u formatu:
    # 1. BA-GODINA-MJESEC-Redni_broj +++
    # Primjer: BA-2021-02-00001+++
    # 2. BA - Business Account++ 
    # 3. Redni_broj - 00001 – 5 znamenki i mora imati nule ispred ako ++
    # je manji od 10 tisuća.++
    # b. Prikaz stanja računa+++
    # c. Prikaz prometa po računu++++
    # d. Polog novca na račun ++
    # e. Podizanje novca s računa++
    # f. Izlaz iz programa – program se izvršava cijelo vrijeme sve dok korisnik ne 
    # odabere opciju Izlaz iz glavnog izbornika.
import datetime, moduli

test_tvrtka = {"Broj Računa": "BA-2021-02-00001","naziv" : "Tvrtka d.o.o.", "Ulica" : "abc 123" , "Poštanski broj" : "47000", "Grad" : "Karlovac", "OIB" : "12345678910", "odgovorna osoba" : ["ime", "prezime"] , "saldo":0}

baza_racuni = [  ]

kreiranje_kljucevi = ["Broj Računa", "Naziv", "Ulica", "Poštanski broj", "Grad", "OIB" , "Odgovorna Osoba"]

counter = 0
counter_transakcija = 1

transakcije = {}

def datum() -> datetime:
    """
    dan = (f"{datetime.datetime.now().day:02d}")

    mjesec = (f"{datetime.datetime.now().month:02d}")
    
    godina = datetime.datetime.now().year
    """

    datum = datetime.datetime.now()

    return datum
    
def kreiraj_racun() -> dict:


    
    global counter
    #broj racuna

    #MJESEC
    mjesec = (f"{datetime.datetime.now().month:02d}")
    #GODINA
    godina = datetime.datetime.now().year
    #RASTUĆI BROJ
    counter += 1     
    counter = (f"{counter:05d}")
    
    # Primjer: BA-2021-02-00001
    kreiran = {}
    print("\n\n\tKREIRANJE NOVOG RAČUNA\n")
    for kljuc in kreiranje_kljucevi:
        
        match kljuc:
                case "Broj Računa":
                    broj_racuna = (f"BA-{godina}-{mjesec}-{counter}")
                    kreiran[kljuc] = broj_racuna
                case "Naziv":
                  naziv = input(f"Unesite {kljuc} Tvrtke: \t\t\t")
                  kreiran[kljuc] = naziv.capitalize()
                case"Ulica":
                  ulica = input(f"Unesite {kljuc} Tvrtke: \t\t\t")
                  kreiran[kljuc] = ulica.capitalize()
                case "Poštanski broj":
                  Po_broj = input(f"Unesite {kljuc} Tvrtke: \t\t")
                  kreiran[kljuc] = Po_broj
                case "Grad":
                  grad = input(f"Unesite {kljuc} u kojem se Tvrtka nalazi: \t")
                  kreiran[kljuc] = grad.capitalize()
                case "OIB":
                  oib = input(f"Unesite {kljuc} Tvrtke: \t\t\t")
                  kreiran[kljuc] = oib
                case "Odgovorna Osoba":
                  ime = input(f"Unesite ime odgovorne osobe Tvrtke: \t")
                  prezime = input(f"Unesite prezime odgovorne osobe Tvrtke: ")
                  ime_i_prezime = []
                  ime_i_prezime.append(ime.capitalize())
                  ime_i_prezime.append(prezime.capitalize())
                  kreiran[kljuc] = ime_i_prezime
    kreiran["saldo"]=0
    moduli.enter_to_continue()
    baza_racuni.append(kreiran)
    
    
def mijenjaj_saldo(broj_racuna:str, nov:bool=False, radnja:str=None) -> list:
   
   for rjecnik in baza_racuni:
      
      for key,value in rjecnik.items():
        if value == broj_racuna:
            if nov:
                print("Račun je tek kreiran, molimo vas unesite iznos pologa! ")
                while True:
                    try:
                        polog = int(input("Iznos: "))
                    except ValueError:
                        print("Polog mora biti brojčano iskazan")
                    else:
                        rjecnik["saldo"] = polog
                        return datum(), polog
                     
                        
            else:
                match radnja:
                    case "uplata":
                        print("Unesite iznos koji želite uplatiti!")
                        while True:
                            try:
                                uplata = int(input("Iznos: "))
                            except ValueError:
                                print("Iznos mora biti brojčano iskazan")
                            else:
                                rjecnik["saldo"] += uplata
                                return datum(), uplata
                                
                    case "isplata":
                        print("Unesite iznos koji želite isplatiti!")
                        while True:
                            try:
                                isplata = int(input("Iznos: "))*-1
                            except ValueError:
                                print("Iznos mora biti brojčano iskazan")
                            else:
                                while True:
                                    if int(isplata*-1) > int(rjecnik["saldo"]):
                                        print("Ne možete isplatiti veći iznos od stanja na računu")
                                        break
                                    
                                    else:
                                        rjecnik["saldo"] += isplata
                                        return datum(), isplata
                                        

            #print("ima")
            #print(rjecnik["saldo"])
            
            
            
            
            
            break
        

def prikaz_stanja(broj_racuna:str) -> None:
    for rjecnik in baza_racuni:      
      for key,value in rjecnik.items():
        if value == broj_racuna:
            stanje = rjecnik["saldo"]
            print(f"Stanje računa {broj_racuna} iznosi {stanje} €")

def zapis_transakcija(datum:datetime, izmjena:int) -> list:
    global transakcije, counter_transakcija
    if izmjena > 0:
        tekst = (f"{datum} uplaćen iznos: {izmjena} €")
    else:
        tekst = (f"{datum} isplaćen iznos: {izmjena*-1} €")
    transakcije[counter_transakcija]= tekst
    counter_transakcija += 1

def main():
    #baza_racuni.append(test_tvrtka) ############ TEST DELETE
    #kreiraj_racun()
    datum, izmjena = mijenjaj_saldo("BA-2021-02-00001", True)
    zapis_transakcija(datum, izmjena)
    
    datum, izmjena = mijenjaj_saldo("BA-2021-02-00001", False, "uplata")
    zapis_transakcija(datum, izmjena)
    
    datum, izmjena = mijenjaj_saldo("BA-2021-02-00001", False, "isplata")
    zapis_transakcija(datum, izmjena)

    print(transakcije)

def info_o_racunu(broj_racuna:str) -> None:
    for rjecnik in baza_racuni:      
      for key,value in rjecnik.items():
        match key:
            
            case "Broj Računa":
                print(f"{key}:\t\t{value}")
            case "Naziv":
                print(f"{key}:\t\t\t{value}")
            case"Ulica":
                print(f"{key}:\t\t\t{value}")
            case "Poštanski broj":
                print(f"{key}:\t\t{value}")
            case "Grad":
                print(f"{key}:\t\t\t{value}")
            case "OIB":
                print(f"{key}:\t\t\t{value}")
            case "Odgovorna Osoba":
                print(f"{key}:\t{value[0]} {value[1]}")

     


   
    
    
    
   
    
    
          
    



if __name__ == "__main__":
    main()