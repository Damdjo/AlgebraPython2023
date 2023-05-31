#napraviti praznu listu brojeva
#popunjavati je korisnickim unosima
#funkcija za popunjavanje vraca True ako je broj dodan
#vraca False ako broj vec postoji i nije dodan
#iskoristiti While sve dok korisnik ne odabere x|X za izlaz iz popisa
 
#generiraj 6 loto brojeva od 45
 
from random import randint
import zad43modul
 
 
loto_brojevi=[]
'''
 
#slucajni_broj=randint(1,45)
#print(slucajni_broj)
#zad43modul.add_number_to_list(loto_brojevi,slucajni_broj)
print(loto_brojevi)
 
print()
print()
 
while len(loto_brojevi)<6:
    slucajni_broj=randint(1,45)
    zad43modul.add_number_to_list(loto_brojevi,slucajni_broj)
 
print(loto_brojevi)
 
 
print()
print()
'''
 
izbornik=['Loto 7/39', 'Loto 6/45']
zad43modul.meni(izbornik)
 
izbor=int(input('Unesite opciju: '))
match izbor:
    case 1:
        lotomax=39
        lotood=7
    case 2:
        lotomax=45
        lotood=6
    case _:
        print('Krivi unos')
 
while len(loto_brojevi)<lotood:
    slucajni_broj=randint(1,lotomax)
    zad43modul.add_number_to_list(loto_brojevi,slucajni_broj)
 
print(loto_brojevi)