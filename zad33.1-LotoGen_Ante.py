# 2. Loto generator (meni s opcijama 6/45, 7/39, Eurojackpot, broj kombinacija, Custom x/y)
# -napraviti MENI s navedenim opcijama (1., 2., 3..., 0. za izlaz)
# -ovisno o odabranoj igri ponuditi ispis N kombinacija (random modul) bez ponavljanja (lista)
# -ovisno o igri, napraviti formatirani ispis i vratiti se na meni

import random

def meni():
    print('*'*40)
    print(' '*17,'MENI',' '*17)
    print('*'*40)
    print('\t1. LOTO 6/45')
    print('\t2. LOTO 7/39')
    print('\t3. Eurojackpot')
    print('\t4. Prilagodjeno')
    print('\t0. Izlaz')
    print('*'*40)

def izvuci_brojeve(broj_izvucenih, ukupni_broj):
    lista_izvucenih_brojeva=[]
    while(len(lista_izvucenih_brojeva)<broj_izvucenih):
        slucajni=random.randint(1,ukupni_broj)
        if slucajni not in lista_izvucenih_brojeva:
            lista_izvucenih_brojeva.append(slucajni)
    #print(lista_izvucenih_brojeva)
    return lista_izvucenih_brojeva


meni()

"""
#postoji mogucnost ponavljanja brojeva
broj=random.randint(1,45)
for i in range(6):
    print(broj)
"""

"""
#nacini izvlacenja slucajnih brojeva bez ponavljanja

lista_od_45_brojeva=[]
for broj in range(1,46):
    lista_od_45_brojeva.append(broj)

print(lista_od_45_brojeva)
izvucenih_6_brojeva=random.sample(lista_od_45_brojeva, k=6)
print(izvucenih_6_brojeva)

#alternativni nacin (nismo osigurali da se doista 7 brojeva spremi u listu)
izvucenih_7_brojeva=[]
for broj in range(7):
    slucajni=random.randint(1,39)
    if slucajni not in izvucenih_7_brojeva:
        izvucenih_7_brojeva.append(slucajni)

print(izvucenih_7_brojeva)


#bolja alternativa (osigurali smo 7 razlicitih brojeva u listi)
izvucenih_7_brojeva_alt=[]
while(len(izvucenih_7_brojeva_alt)<7):
    slucajni=random.randint(1,39)
    if slucajni not in izvucenih_7_brojeva_alt:
        izvucenih_7_brojeva_alt.append(slucajni)

print(izvucenih_7_brojeva_alt)

"""

meni()
opcija=int(input('Unesite opciju 0-4'))

if opcija==2:
    print('\n'*3)
    lista7od39=izvuci_brojeve(7,39)
    lista7od39.sort()
    print(lista7od39)
else:
    print('nesto')
