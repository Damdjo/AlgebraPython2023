#nadodati spremanje podataka u txt file ako smo imali prethodnu zadaći

#ako nismo, na zadatke sa zadnjeg predavanja nadovezati se
#možda jedan od dijelova "contact manager" zadatka



import os
import datetime as dt
from dateutil.relativedelta import relativedelta, TU, FR
from dateutil import tz

adresar_putanja = "m3/Zadace/zadaca04/eventi.txt"

input_list = ["Naziv", "Opis", "Datum", "Vrijeme"]
meni_opcije = ["Novi događaj","Ispis kalendara", "Promjeni korisnika", "Ispis opisa eventa"]

class User:
    """User"""
    def __init__(self, korisnik):
        self.korisnik = korisnik
        
    def check_user(self):
        return self.korisnik

class Kalendar(User):
    def __init__(self, korisnik, event_id = "1"):
        super().__init__(korisnik)
        self.event_id = event_id
    
    def set_ev_id(self):
        max = self.event_id
        with open("m3/Zadace/zadaca04/eventi.txt", "r") as file_writer:
                for red in file_writer:
                    red = red.split(";")                    
                    if int(max) <= int(red[0]):
                        max = int(red[0]) + 1
        self.event_id = str(max).zfill(4)

    def check_evid(self):        
        return self.event_id.zfill(4)
    
    def print_kalendar(self, rijecnik):
        temp_dict = rijecnik
        print_order = []
        while temp_dict != {}:
            min = " 31.12.9999 23:59"
            min_key = "0000"
            for key, value in temp_dict.items():
                try:
                    value = dt.datetime.strptime(value, " %d.%m.%Y %H:%M")
                except TypeError as type:
                    pass
                except Exception as e:
                    print(f"Greška: {type}")
                try:
                    min = dt.datetime.strptime(min, " %d.%m.%Y %H:%M")
                except TypeError as type:
                    pass
                except Exception as e:
                    print(f"Greška: {type}")
                if value < min:
                    min = value
                    min_key = key

            print_order.append(min_key)
            temp_dict.pop(min_key)
        
        clear_screen()
            

        for key in print_order:
            with open("m3/Zadace/zadaca04/eventi.txt", "r") as file_writer:
                for red in file_writer:
                    red = red.split(";")
                    if red[0] == key:
                                    #EVENT ID         #DATUM                  #SATI                                   #NAZIV        
                        print(f"Event ID: {red[0]} | {red[3]}. u {red[4]} \tsati događaj: {red[1]}".center(40))  


class Event(Kalendar):
    """Klasa ima korisnika, naziv, opis, datum i vrijeme"""
    def __init__(self, korisnik = "", naziv = "", opis = "", datum = "", vrijeme = "", event_id = "1"):
        super().__init__(korisnik, event_id)
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
        
        
        with open("m3/Zadace/zadaca04/eventi.txt", "a") as file_writer:
            file_writer.write(f"{self.event_id.zfill(4)}; {self.naziv}; {self.opis}; {self.datum}; {self.vrijeme}; \n") 
        self.event_id = str(int(self.event_id)+1)           


    def ispisi_opis(self, key):
        
        
        with open("m3/Zadace/zadaca04/eventi.txt", "r") as file_writer:
            for red in file_writer:
                red = red.split(";")
                if key == red[0]:
                    print(f"ID: {red[0]} | Opis: {red[2]}")
                    return None
                
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

def line_parse(string:str) -> list:
    parsed = string.split(";")
    return parsed

def id_date_time_dict(file_path):
    returned_dict = {}
    with open(file_path, "r") as file_writer:
                    for line in file_writer:                        
                        line = line_parse(line)
                        id = line[0]
                        date = line[3]
                        time = line[4]
                        datetime = date + time
                        datetime = dt.datetime.strptime(datetime, " %d.%m.%Y %H:%M")
                        datetime = datetime.strftime(" %d.%m.%Y %H:%M")                                                
                        returned_dict[id] = datetime                        
    
    return returned_dict
    
    

#MAIN

clear_screen()
print()
#current_user = input("Unesite naziv korisnika: ")
current_user = "Korisnik"
current_user = Event(current_user)
status = -1
while status != 0:
    
    clear_screen()
    meni()

    try: odabir = int(input("Unesite odabir: "))
    except ValueError:
        print("Unos nije ispravan!")
        enter_to_continue()

    else:
        match odabir:
            case 1:
                current_user.set_ev_id()
                current_user.novi_dogadaj(current_user)
            case 2:
                trunc_dict = id_date_time_dict(adresar_putanja)
                current_user.print_kalendar(trunc_dict)
                enter_to_continue()
            case 3:
                current_user = Event(input("Unesite naziv novog korisnika: "))
                
                print(f"{current_user}")
            case 4:
                unos = input("Unesite ID eventa: ")
                current_user.ispisi_opis(unos)
                enter_to_continue()
            case 5:
                current_user.set_ev_id()
            case 6:
                pass
            case 7:
                
                pass
            case 0:
                break