#napraviti praznu listu brojeva
#popunjavati je korisničkim unosima
#funkcija za popunjavanje vraća True ako je broj dodan
#vraća False ako broj već postoji i  nije dodan
#iskoristiti while sve dok korisnik ne odabere x | X za izlaz iz popisa

#generiraj 6 loto brojeva od 45

from random import randint
import zad43_modul

izbornik = ["Loto 7/39", "Loto 6/45"]
zad43_modul.meni(izbornik)

izbor = int(input("Unesite opciju"))
match izbor:
    case 1:
        lotoMax = 39
        brojOd = 7
    case 2:
        lotoMax = 45
        brojOd = 6
    case _:
        print("Krivi unos")


lotoBrojevi = []
slucajniBroj = randint(1,45)

print(slucajniBroj)
#addNumberToList(lotoBrojevi,slucajniBroj)
print(lotoBrojevi)

print()
print()
print()

while len(lotoBrojevi) < brojOd:
    slucajniBroj = randint(1,lotoMax)
    zad43_modul.addNumberToList(lotoBrojevi,slucajniBroj)

print(lotoBrojevi)