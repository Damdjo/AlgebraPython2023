#Autor: Saša Knapek
#pogodi dan u tjednu u skraćenom obliku
#pon, uto. sri, cet, pet, sub, ned
#neka računalo odabere jedan dan u tjednu iz liste dana
#neka korisnik unosi skraćeni dan, voditi score board za pobjede
#izlaz iz programa će biti kad korisnik unese bilo koji krivi unos
#broji se ukupni broj pokusaja i broj uspjesnih pogadjanja, oblik je 5/11 npr.

import random

dani = ["pon", "uto", "sri", "cet", "pet", "sub", "ned"]
ukupno_pokusaja=0
pogodjeno=0

while True:
    
    odabir_racunala=random.choice(dani)
    ukupno_pokusaja+=1
    odabir_korisnika = input('Unesi željeni skraćeni dan: ')
    print(f'Odabrali ste: {odabir_korisnika}')
    print(f'Racunalo je odabralo: {odabir_racunala}')

    if odabir_korisnika in dani:
        if odabir_racunala==odabir_korisnika:
            pogodjeno+=1
            print('Pogodili ste dan')
        else:
            print('Niste pogodili dan')
    else:
        print('Unesen nepostojeci dan')
        break
    print(f'Trenutni rezultat je {pogodjeno}/{ukupno_pokusaja}')
