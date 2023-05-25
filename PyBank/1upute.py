# UPUTE ZA UPLOAD KODA:
# LINK: tinyurl.com/algpythonosnove
# UPLOAD FILE: mapu Pybank zipat (nemojte koristiti naše dijakritičke znakove) i takvu uploadat 

# 1. Kreirajte projekt unutar foldera PyBank te u njemu kreirajte jednu datoteku u koju 
# ćete upisivati Vaš Python kôd.

# 2. Funkcionalnosti koje program treba imati su:
# a. Kreiranje računa Tvrtke
# Tvrtka ima podatke: Naziv, Ulica i broj, Poštanski broj sjedišta, Grad sjedišta, 
# OIB (mora imati točno 11 znakova), Ime i prezime odgovorne osobe.
# i. Kod otvaranja računa treba položiti iznos po volji
# ii. Treba odabrati valutu računa EUR ili HRK
# iii. Račun generirati broj računa u formatu:
    # 1. BA-GODINA-MJESEC-Redni_broj 
    # Primjer: BA-2021-02-00001
    # 2. BA - Business Account 
    # 3. Redni_broj - 00001 – 5 znamenki i mora imati nule ispred ako 
    # je manji od 10 tisuća.
    # b. Prikaz stanja računa
    # c. Prikaz prometa po računu
    # d. Polog novca na račun
    # e. Podizanje novca s računa
    # f. Izlaz iz programa – program se izvršava cijelo vrijeme sve dok korisnik ne 
    # odabere opciju Izlaz iz glavnog izbornika.

# 3. Kada se program pokrene cijeli ekran konzole se „očisti“ i prikaže se samo glavni 
# izbornik. To znači da se sve što je bilo prikazano prije u konzoli izbriše. To se postiže 
# pomoću modula os. Znači trebate koristiti „import os“ i svaki put kada dođete do 
# točke kada želite da se ekran „očisti“ od prethodnog sadržaja pokrenite funkciju:
# os.system('cls' if os.name == 'nt' else 'clear') – provjerava je li OS 
# Windows ili Linux.
# Dakle kod svake promjene ekrana pokrenite ovu naredbu. 