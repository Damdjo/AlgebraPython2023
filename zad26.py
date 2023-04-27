#pogodi dan u tjednu, u skraćenom obliku:
#pon, uto, sri, cet, pet, sub, ned
#neka racunalo odabere jedan dan u tjednu iz liste dana
#neka korisnik unosis skraćeni dan, vodite score board za pobjede(broj pokušaja i pogodaka)
#izlaz iz programa će biti kada korisnik unese bilo koji krivi unos

#koristimo random.choice(IMELISTE)
import random

listaDana = ["pon", "uto", "sri", "cet", "pet", "sub", "ned"]

status = True
pokusaj = 0
pogodak = 0

izbornik = """
    Pokušajte pogoditi dan u tjednu
    Moguće opcije su:   

        pon, uto, sri, cet, pet, sub, ned
    
    U slučaju da je unos bilo što drugo, igra završava

"""


while status:

    
    while True:
        unosRacunalo = random.choice(listaDana)
        print(izbornik)
        unosKorisnik = str(input("Unesite jedan od dana u tjednu u skraćenom obliku: "))
        print(f"Računalo je odabralo {unosRacunalo}")
        #print(unosRacunalo)

    #google pomogao if "not in" list
        if unosKorisnik not in listaDana:
            status = False
            print("\nIzlaz iz igre\n")
            break
        
        if unosKorisnik == unosRacunalo:
            print("Pogodak")
            pokusaj += 1
            pogodak += 1
        else:
            print("Promašaj")
            pokusaj += 1
        
print(f"Od ukupno {pokusaj} pokušaja, uspješno ste pogodili {pogodak} puta!\n")