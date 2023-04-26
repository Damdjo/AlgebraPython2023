#domZad3 provjera unesenih ocjena
#Moraju biti 1,2,3,4,5

#Napraviti program koji će sadržavati 5 osoba, te osobe će imati popis svojih ocjena
# ocjene se zapisuju u obliku liste
# Napraviti report sa: prosječna ocjena, najmanja ocjena, najviša ocjena, broj specifičnih ocjena

imenik = {

    "Pero":  [],
    "Mate" : [],
    "Ivan" : [],
    "Josip": [],
    "Ante" : []
}

for ime in imenik.keys():
    brojOcjena = int(input(f"Unesite broj ocjena koji {ime} ima: "))
    krivihUnosa = 0
    for broj in range(brojOcjena):
        ocjena = int(input(f"Unesite {broj+1}. ocjenu: "))
        if ocjena >= 1 and ocjena <= 5:
            imenik[ime].append(ocjena)
    
    #brojač krivih unosa za svjedodžbu
        else:
            krivihUnosa += 1
            print("Pogrešan unos! Unesena ocjena nije zabilježena!")
    
    if krivihUnosa > 0:
        imenik[ime].append(krivihUnosa*7)


for ime in imenik.keys():
    if len(imenik[ime]) > 0:
        print(f"\nSvjedodžba {ime}")
        #Prosjek, najveća i najniža ocjena
        sumaOcjena = 0
        brojOcjena = 0
        kriveOcjene = 0

        #micanje najviše ocjene ukoliko je bilo krivih unosa
        if max(imenik[ime]) % 7 == 0:
            kriveOcjene = imenik[ime].pop(-1)       

        for ocjena in imenik[ime]:
            sumaOcjena += ocjena
            brojOcjena += 1
        print(f"Prosjek ocjena iznosi {round(float(sumaOcjena/brojOcjena),2)}")
        print(f"Od svih dobivenih ocjena, najviša je {max(imenik[ime])}, a najniža {min(imenik[ime])}")
        print(f"Ovoliko puta se pojavila svaka ocjena: \n", end="")
        
        # Broj dobivenih ocjena
        for ocjena in imenik[ime]:
            if ocjena >= 1 and ocjena <= 5:
                brojOcjena = imenik[ime].count(ocjena)
                print(f"\t{brojOcjena} puta je dobivena ocjena {ocjena}.")

        #Krivo unesene ocjene
        if kriveOcjene > 0:
            print(f"Bilo je {int(kriveOcjene/7)} krivo unesenih ocjena")
    else:
        print(f"{ime} je preskočen", end="")
    print()












