#zad39 - Pascalov trokut
#Unijeti broj redova pascalovog trokuta (do max 10)
#formatirano ispisati koristeći tabulator
#                  1
#              1       1
#          1       2       1
#      1       3       3       1

# formula https://hr.wikipedia.org/wiki/Binomni_koeficijent
# + pomogao je google

def binomniKoeficijent(broj,koef):
    rezultat = 1

    for x in range(koef):
        rezultat = rezultat * (broj-x)
        rezultat = rezultat // (x+1)
    return rezultat

test1 = binomniKoeficijent(4,2)


brojRedova = 0
while brojRedova < 1 or brojRedova > 10:
    brojRedova = int(input("Unesite broj redova za Pascalov trokut (do 10): "))
    if brojRedova < 1 or brojRedova > 10:
        print("Broj nije u navedenom rasponu, pokušajte ponovno!")

# brojač za formatiranje redova
counterTab = brojRedova

for red in range(brojRedova):
    print("\t"*counterTab, end = "")
    for brojevi in range(red+1):
        print(binomniKoeficijent(red,brojevi), end ="\t\t")
    counterTab -= 1
    print()