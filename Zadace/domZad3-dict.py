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
    for broj in range(brojOcjena):
        imenik[ime].append(int(input(f"Unesite {broj+1}. ocjenu: ")))

for ime in imenik.keys(): 
    print(f"\nSvjedodžba {ime}")
    #Prosjek, najveća i najniža ocjena
    sumaOcjena = 0
    brojOcjena = 0

    for ocjena in imenik[ime]:
        sumaOcjena += ocjena
        brojOcjena += 1
    print(f"Prosjek ocjena iznosi {round(float(sumaOcjena/brojOcjena),2)}")
    print(f"Od svih dobivenih ocjena, najviša je {max(imenik[ime])}, a najniža {min(imenik[ime])}")
    print(f"Ovoliko puta se pojavila svaka ocjena: \n", end="")
    
    # Broj dobivenih ocjena
    for ocjena in imenik[ime]:
        brojOcjena = imenik[ime].count(ocjena)
        print(f"\t{brojOcjena} puta je dobivena ocjena {ocjena}.")










