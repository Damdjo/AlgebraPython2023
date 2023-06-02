# mute metodi dodati mogućnost da spremi zadnju vrijednost prije mute-a te ju vrati nakon ponovnog unosa vrijednosti 0
# urediti/napraviti novu metodu koja će mijenjati status "je_ukljucen" iz False u True i obrnuto (da prebacuje između te dvije vrijednosti)
# smisliti jos neke svoje dodatne metode npr. između više objekata tipa televizora pregledati koji ima najveću dijagonalu

class TelevizijskiAparat():
    """ Tevelizor """

    def __init__(self, dijagonala, sirina, visina, proizvodac, model, program=0, glasnoca=0, je_ukljucen=False, pre_mute = 0, is_muted = False):
        self.dijagonala = dijagonala
        self.sirina = sirina
        self.visina = visina
        self.proizvodac = proizvodac
        self.model = model
        self.program = program
        self.glasnoca = glasnoca
        self.je_ukljucen = je_ukljucen
        self.pre_mute = pre_mute
        self.is_muted = is_muted



    def ukljuci(self):
        match self.je_ukljucen:
            case True:
                self.je_ukljucen = False
            case False:
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
                    
                    match self.is_muted:
                        case False:
                            self.pre_mute = self.glasnoca
                            self.glasnoca = 0
                            self.is_muted = True
                        case True:
                            self.glasnoca = self.pre_mute
                            self.is_muted = False
                case _:
                    pass
        else:
            print("Televizor nije ukljucen")






tv_dnevni_boravak = TelevizijskiAparat(55, 124, 79, "Grundig", "Extra55", 5, 10)
tv_spavaca_soba = TelevizijskiAparat(40, 100, 62, "Sony", "Sony 40\"")
tv_kupaona = TelevizijskiAparat(30, 80, 51, "NOA", "NOA Waterproof 30")


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
for broj in range(5):  
    tv_dnevni_boravak.podesi_glasnocu("-")
tv_dnevni_boravak.promjeni_program(19)

print(f"Tv je na programu: {tv_dnevni_boravak.program}, na jačini zvuka: {tv_dnevni_boravak.glasnoca}")

#tv sa max dijagonalom
lista_televizora = [tv_dnevni_boravak, tv_kupaona, tv_spavaca_soba]
maxDijagonala = 0
for tv in lista_televizora:
    
    if tv.dijagonala > maxDijagonala:
        maxDijagonala = tv.dijagonala
print( maxDijagonala)

for broj in range(5):  
    tv_dnevni_boravak.podesi_glasnocu("+")
    
print(f"Tv je na programu: {tv_dnevni_boravak.program}, na jačini zvuka: {tv_dnevni_boravak.glasnoca}")

tv_dnevni_boravak.podesi_glasnocu("0")

print(f"Tv je na programu: {tv_dnevni_boravak.program}, na jačini zvuka: {tv_dnevni_boravak.glasnoca}")

tv_dnevni_boravak.podesi_glasnocu("0")

print(f"Tv je na programu: {tv_dnevni_boravak.program}, na jačini zvuka: {tv_dnevni_boravak.glasnoca}")