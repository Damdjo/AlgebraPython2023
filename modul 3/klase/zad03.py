class TelevizijskiAparat():
    """ Tevelizor """

    def __init__(self, dijagonala, sirina, visina, proizvodac, model, program=0, glasnoca=0, je_ukljucen=False):
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.program = program
        self.glasnoca = glasnoca
        self.je_ukljucen = je_ukljucen



    def ukljuci(self):
        self.je_ukljucen = True

    def promjeni_program(self, novi_program):
        if self.je_ukljucen != False:
            if novi_program < 100:        
                self.program = novi_program
        else:
            print("Televizor nije ukljucen")

    def podesi_glasnocu(self, smjer_promjene = " "): # + , - , 0 (mute)
        if self.je_ukljucen != False:
            match smjer_promjene:
                case "+":
                    if self.glasnoca < 20:
                        self.glasnoca += 1
                    else:
                        pass
                case "-":
                    if self.glasnoca > 0:
                        self.glasnoca -= 1
                    else:
                        pass
                case "0":
                    self.glasnoca = 0
                case _:
                    pass
        else:
            print("Televizor nije ukljucen")
        

class covjek():
    def __init__(self, visina, tezina, spol, datum_rodenja, raspolozenje = "sretan",  je_ziv=True):
        self.visina = visina
        self.tezina = tezina
        self.spol = spol
        self.datum_rodenja = datum_rodenja
        
        self.raspolozenje = raspolozenje
        self.je_ziv = je_ziv

    
                
    def promjeni_podatak(self, kategorija, vrijednost):
        match kategorija:
            case "visina":
                self.visina = vrijednost
            case "tezina":
                self.tezina = vrijednost
            case "spol":
                self.spol = vrijednost
            case "datum_rodenja":
                self.datum_rodenja = vrijednost          
            case "raspolozenje":
                self.raspolozenje = vrijednost
            case "je_ziv":
                match vrijednost:
                    case True:
                        self.je_ziv = vrijednost
                    case False:
                        self.je_ziv = vrijednost
                    case _:
                        pass
    def info(self):
        print (f"\n\tVisina: {self.visina} \n\tTežina: {self.tezina} \n\tSpol: {self.spol} \n\tDatum rođenja: {self.datum_rodenja} \n\tRaspoloženje:{self.raspolozenje}  \n\tŽiv/a: {self.je_ziv}")




tv_dnevni_boravak = TelevizijskiAparat(55, 124, 79, "Grundig", "Extra55", 5, 10)
print()
print(f"Proizvođač: {tv_dnevni_boravak.proizvodac}")
print(f"Dijagonala: {tv_dnevni_boravak.dijagonala}")
print("\n\n")

if tv_dnevni_boravak.je_ukljucen:
    print(f"Status: TV u dnevnom je uključen")
else:
    print(f"Status: TV u dnevnom je isključen")

tv_dnevni_boravak.ukljuci()

if tv_dnevni_boravak.je_ukljucen:
    print(f"Status: TV u dnevnom je uključen")
else:
    print(f"Status: TV u dnevnom je isključen")



print(f"Tv je na programu: {tv_dnevni_boravak.program}, na jačini zvuka: {tv_dnevni_boravak.glasnoca}")
for broj in range(25):  
    tv_dnevni_boravak.podesi_glasnocu("-")
tv_dnevni_boravak.promjeni_program(19)

print(f"Tv je na programu: {tv_dnevni_boravak.program}, na jačini zvuka: {tv_dnevni_boravak.glasnoca}")

osoba1 = covjek(170,70,"M","31.1.1995")
osoba2 = covjek(180,80,"Ž","31.1.1993")

print (f"Osoba 1: ")
#osoba1.info()
osoba1.promjeni_podatak("težina",190)
osoba1.promjeni_podatak("spol",90)
osoba1.info()

print (f"Osoba 2: ")
osoba2.info()