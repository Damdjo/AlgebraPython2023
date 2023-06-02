class Osoba:

    """Klasa osoba"""
    def __init__(self, ime, oib, adresa):
        self.ime = ime
        self.oib = oib
        self.adresa = adresa

class TvrtkaOsoba(Osoba):
    def __init__(self,ime, oib, adresa, broj_djelatnika, pravni_oblik = "d.d."):
        super().__init__(ime, oib, adresa)        
        self.broj_djelatnika = broj_djelatnika
        self.pravni_oblik = pravni_oblik
    
    
mate = Osoba("Mate", "12345678910", "Karlovačka 11")


print(f"{mate.ime} ima oib: {mate.oib} i živi na adresi: {mate.adresa}")


matedd = TvrtkaOsoba("Mate d.d.", "12345678910", "Zadarska 3",22)


print(f"Tvrtka \"{matedd.ime}\" ima oib: {matedd.oib}, nalazi se na adresi: {matedd.adresa}, ima {matedd.broj_djelatnika} djelatnika i oblika je {matedd.pravni_oblik}")


#Keyed argumenti, možemo zaobići redosljed argumenata u klasi/funkciji

stipe = Osoba(adresa="Matoševa 23", oib= "55646498413", ime="Stipe")
print(f"{stipe.ime} ima oib: {stipe.oib} i živi na adresi: {stipe.adresa}")

