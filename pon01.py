#opisne ocjene
#od korisnika zatražimo da unese brojčanu ocjenu
#mi mu na osnovu te ocjene ispišemo opisnu (Odličan, Vrlo dobar, ... , Nedovoljan)


popisOcjena = ["Pogrešan unos" , "NEDOVOLJAN", "DOVOLJAN", "DOBAR", "VRLO DOBAR", "ODLIČAN"]
uneseneOcjene = []



# cilj je unjeti više ocjena, spremiti ih, te na osnovu prosjeka (ručno napraviti)
#pretvoriti u cijelu ocjenu i ispisati kao konačnu opisnu ocjenu

#korisnik unosi broj ocjena koji će unjeti
while True:
    odgovor = input("Želite li sami broj ocjena? Ako ne program će prihvaćati ocjene dok ne unesete 0. (Da / Ne): ")
    if odgovor.title() == "Da" or odgovor.title() == "Ne":        
        break        
    else:
        print("Pogrešan unos")

if odgovor.title() == "Da":
    kolikoOcjena = int(input("Unesite broj ocjena koji će te unjeti: "))

    for ocjena in range(kolikoOcjena):

        numerickaOcjena = int(input("Unesite numeričku vrijednost ocjene (1-5): "))

        if numerickaOcjena in range(1,6):
            uneseneOcjene.append(numerickaOcjena)
        else:
            print(popisOcjena[0])

    print(uneseneOcjene)

if odgovor.title() == "Ne":
    while True:
        numerickaOcjena = int(input("Unesite numeričku vrijednost ocjene (1-5) ili 0 za izlaz: "))

        if numerickaOcjena in range(1,6):
            uneseneOcjene.append(numerickaOcjena)
        else:
            print(popisOcjena[0])
            break
    print(uneseneOcjene)
if len(uneseneOcjene) > 0:
    suma = 0
    for ocjena in uneseneOcjene:
        suma += ocjena

    prosjek = suma / len(uneseneOcjene)

    print(f"Vaša završna ocjena je {popisOcjena[round(prosjek)]}")