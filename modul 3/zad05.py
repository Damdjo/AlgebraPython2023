class Osoba:

    """Klasa osoba"""
    def __init__(self):
        self.ime = ""
        self.oib = ""
        self.adresa = ""

class Tvrtka(Osoba):
    def __init__(self):
        super().__init__()        
        self.broj_djelatnika = 0
        self.pravni_oblik = "d.d."
    
    
mate = Osoba()
mate.ime = "Mate"
mate.oib = "12345678910"
mate.adresa = "Karlovačka 11"

print(f"{mate.ime} ima oib: {mate.oib} i živi na adresi: {mate.adresa}")


matedd = Tvrtka()
matedd.ime = "Mate d.d."
matedd.oib = "12345678910"
matedd.adresa = "Karlovačka 11"

"""
class Tvrtka:

    
    def __init__(self):
        Osoba.ime = ""
        Osoba.oib = ""
        Osoba.adresa = ""
        self.broj_djelatnika = 0
        self.pravni_oblik = ""

class Djelatnik:

    
    def __init__(self):
        self.ime = ""
        self.oib = ""
        self.adresa = ""
        self.radno_mjesto = ""
"""