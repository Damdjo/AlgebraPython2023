


#Napraviti klase za sve tipove vozila
    #Podjela na: pomorska, zračna, cestovna, željeznička

#Za svaku podjelu napraviti podkategorije
    #npr cestovna: auto, motor, itd.

#Zajedničko za sva vozila: težina, dužina, širina, visina
    #Zajedničko za klase (pomorska, zračna, cestovna, željeznička)
        #Zajedničko za podkategorije (npr cestovna: auto, motor, itd.) 
            #Specifično za jednu vrstu (npr. motori: 2 kotača, tip motora )



class Vozila:

    """Sva vozila"""
    def __init__(self, tezina, duzina, sirina, visina):
        self.tezina = tezina
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
#POMORSKA VOZILA
class PomorskaVozila(Vozila):

    """Pomorska vozila"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta, snaga_motora):
        super().__init__(tezina, duzina, sirina, visina)
        self.vrsta = vrsta #teretni, putnički, sportski
        self.snaga_motora = snaga_motora

class Tanker(PomorskaVozila):
    """Teretni brod"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta, snaga_motora, vrsta_tereta ):
        super().__init__(tezina, duzina, sirina, visina, vrsta, snaga_motora)
        self.vrsta_tereta = vrsta_tereta

class EverGiven(Tanker):
    """Tanker Ever Given"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta, snaga_motora, vrsta_tereta, lokacija, zapeo ):
        super().__init__(tezina, duzina, sirina, visina, vrsta, snaga_motora, vrsta_tereta)
        self.lokacija = lokacija
        self.zapeo = zapeo


class Cruiser(PomorskaVozila):
    """Putnički brod"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta, snaga_motora, broj_soba ):
        super().__init__(tezina, duzina, sirina, visina, vrsta, snaga_motora)
        self.broj_soba = broj_soba

class JetSki(PomorskaVozila):
    """Sportsko pomorsko vozilo"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta, snaga_motora, boja ):
        super().__init__(tezina, duzina, sirina, visina, vrsta, snaga_motora)
        self.boja = boja 


#ZRAČNA VOZILA
class ZracnaVozila:

    """Zracna vozila"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta):
        super().__init__(self, tezina, duzina, sirina, visina)
        self.vrsta = vrsta #teretni, putnički

#CESTOVNA VOZILA
class CestovnaVozila:

    """Cestovna vozila"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta):
        super().__init__(tezina, duzina, sirina, visina)
        self.vrsta = vrsta #auto, motor, kamion, bicikl

#ZELJEZNICKA VOZILA
class ZeljeznickaVozila:

    """Zeljeznicka vozila"""
    def __init__(self, tezina, duzina, sirina, visina, vrsta):
        super().__init__(tezina, duzina, sirina, visina)
        self.vrsta = vrsta #teretni, putnički


tanker_evergiven = EverGiven(220000, 400, 60, 45,"Tanker","60000KW","Kontejneri","Sueski kanal",True)    

print("\n"*50)
print(f"Ever Given je brod težine {tanker_evergiven.tezina} tona, dužine {tanker_evergiven.duzina}M ,širine {tanker_evergiven.sirina}M i visine {tanker_evergiven.visina}M.")
print(f"Vrsta vozila je {tanker_evergiven.vrsta}, snaga motora je {tanker_evergiven.snaga_motora}KW.\nVrsta tereta koju brod prevozi su {tanker_evergiven.vrsta_tereta}.")
print(f"Brod se nalazi na lokaciji {tanker_evergiven.lokacija} i ",end="", sep ="")
if tanker_evergiven.zapeo:
    print("zapeo je.")
else:
    print("nije zapeo.")

