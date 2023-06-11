# unositi datum kada imamo sastanak/obveze te će se spremati u liste
# podatci u listi ce biti u datetime obliku
# program će kronološkim redosljedom ispisivati sve obveze
# dodatno "zakomplicirati" ako hocemo

import os
import datetime as dt
from dateutil.relativedelta import relativedelta, TU, FR
from dateutil import tz

input_list = ["Naziv", "Opis", "Datum", "Vrijeme"]
meni_opcije = ["Novi događaj","Ispis kalendara", "Promjeni korisnika", "Ispis opisa eventa"]

class User:
    """User"""
    def __init__(self, korisnik):
        self.korisnik = korisnik
        
    def check_user(self):
        return self.korisnik

class Kalendar(User):
    def __init__(self, korisnik, event_id = "1", kalendar = {}):
        super().__init__(korisnik)
        self.event_id = event_id
        self.kalendar = kalendar

    def check_evid(self):        
        return self.event_id.zfill(4)
    
    def print_kalendar(self):
        temp_dict = self.kalendar.copy()
        print_order = []
        while temp_dict != {}:
            min = "29.12.9999"
            min_key = "0000"
            for key, value in temp_dict.items():
                
                if value[2] < min:
                    min = value[2]
                    min_key = key

            print_order.append(min_key)
            temp_dict.pop(min_key)
                

        for key in print_order:
                        #DATUM
            clear_screen()
            print()
            print(f"ID: {key} | {self.kalendar[key][2]} u {self.kalendar[key][3]} sati događaj: {self.kalendar[key][0]}")  
        print()     
        
                
             

        

    """
    case 4:
            
        case 5:
            print(current_user.kalendar["0001"])
            enter_to_continue() 
    
    
    
    
    """
        


class Event(Kalendar):
    """Klasa ima korisnika, naziv, opis, datum i vrijeme"""
    def __init__(self, korisnik = "", naziv = "", opis = "", datum = "", vrijeme = "", event_id = "1", kalendar = {}):
        super().__init__(korisnik, event_id, kalendar)
        self.naziv = naziv
        self.opis = opis
        self.datum = datum
        self.vrijeme = vrijeme
    
    def novi_dogadaj(self, user):
        global input_list        
        self.korisnik = user
        for item in input_list:
            
            match item.lower():
                case "naziv":
                    self.naziv = input(f"Unesite {item.upper()}: ")
                case "opis":
                    self.opis = input(f"Unesite {item.upper()}: ")
                case "datum":

                    while True:
                        unos = input(f"Unesite {item.upper()} u obliku (DAN.MJESEC.GODINA): ")
                        try: self.datum = dt.datetime.strptime(unos, "%d.%m.%Y")
                        except ValueError:
                            print("Datum nije unesen u ispravnom formatu (DAN.MJESEC.GODINA) \nPokušajte ponovno!")
                        else:
                            self.datum = self.datum.strftime("%d.%m.%Y")
                            break
                        
                case "vrijeme":                    
                    
                    while True:
                        unos = input(f"Unesite {item.upper()} u obliku (SATI:MINUTE): ")
                        try: self.vrijeme = dt.datetime.strptime(unos, "%H:%M")
                        except ValueError:
                            print("Vrijeme nije uneseno u ispravnom formatu (SATI:MINUTE) \nPokušajte ponovno!")
                        else:
                            self.vrijeme = self.vrijeme.strftime("%H:%M")
                            break                    
                case _:
                    pass
        event_lista = [self.naziv, self.opis, self.datum, self.vrijeme]
        self.kalendar[self.event_id.zfill(4)] = event_lista
        self.event_id = str(int(self.event_id)+1)            


    def ispisi_opis(self, key):
        if key in self.kalendar.keys():
            print(f"ID: {key} | Opis: {self.kalendar[key][1]}")
        else:
            print("Ne postoji event sa navedenim ID-om")


#SUCELJE
def clear_screen():
    os.system("cls")

def meni():
    print("*"*50)
    print(" "*17,"KALENDAR DOGAĐAJA")
    print("*"*50)
    print("\n")
    for broj, opcija in enumerate(meni_opcije):
        print(f"\t{broj+1}. {opcija}")
    print()
    print("0. Izlaz")
    print("\n")

def enter_to_continue():
    input("Pritisnite tipku enter za nastavak...")



#MAIN

clear_screen()
print()
current_user = input("Unesite naziv korisnika: ")
current_user = Event(current_user)
status = -1
while status != 0:
    
    clear_screen()
    meni()

    try: odabir = int(input("Unesite odabir: "))
    except ValueError:
        print("Unos nije ispravan!")

    else:
        match odabir:
            case 1:
                current_user.novi_dogadaj(current_user)
            case 2:
                current_user.print_kalendar()
                enter_to_continue()
            case 3:
                current_user = Event(input("Unesite naziv novog korisnika: "))
                
                print(f"{current_user}")
            case 4:
                unos = input("Unesite ID eventa: ")
                current_user.ispisi_opis(unos)
                enter_to_continue()

            case 0:
                break