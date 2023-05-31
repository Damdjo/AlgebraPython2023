#Od korisnika zatraži unos ukupne količine (broja) ocjena.
#Vodite evidenciju ukupnog broja upisanih ocjena, te ukupne sume svih ocjena
#Na osnovu navedenog napišite program koji će ispisati:
#a) prosječnu ocjenu
#b) maksimalnu ocjenu
#c) minimalnu ocjenu
#d) listu u kojoj će biti količina pojedine ocjene gdje index 0 predstavlja ocjenu 1
#   a index 4 predstavlja ocjenu 5 



granica = int(input("Unesi gornju granicu: "))
ocjene = []
prosjek = 0.0

#unos ocjena do broja koji je unesen pod "granica"
for broj in range(granica):
    ocjene.append(int(input(f"Unesite {broj+1}. ocjenu:")))

#računanje prosjeka
brojOcjena = 0
sumaOcjena = 0
for ocjena in ocjene:
    brojOcjena += 1
    sumaOcjena += ocjena
prosjek = sumaOcjena/brojOcjena

print(f"Prosjek unesenih ocjena iznosi {round(prosjek, 2)}.")

#printanje najveće i najniže ocjene
print(f"Najviša unesena ocjena u listi je {max(ocjene)}, a najniža {min(ocjene)}")
