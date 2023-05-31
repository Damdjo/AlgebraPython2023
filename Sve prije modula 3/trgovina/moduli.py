import racun
def sucelje(lista:list, izlaz:bool=False, login_logout:bool=False, odjel:str=None) -> None:
    """
    lista -> lista sa popisom opcija koja se printaju jedan ispod druge sa rednim brojevima\n    
    ***od opcija izlaz i login_logout samo jedna može biti aktivna***\n
    ***izlaz -> ako je True onda se na kraju ispiše opcija 0. Izlaz\n
    ***login_logout -> ako je True onda se na kraju ispiše opcija 0. Logout
                    -> možemo proslijediti i argument odjel koji će se ispisazi uz MENI
    """
    
    if odjel != "trgovina":
        meni = "MENI " + odjel
    else:
        meni = "Trgovina d.o.o"
    
    
    
    meni.upper()
    duzina = int(50/2-len(meni)/2)

    print('*'*50)
    print(' '*duzina,meni,)
    print('*'*50)
    for broj, stavka in enumerate(lista):
        print(f'\t{broj+1}. {stavka}')
    if izlaz and not login_logout:
        print('\n\t0. Izlaz')
    if login_logout and not izlaz:        
        print('\n\t0. Logout')

def tablicaIspis(lista_stupci:list=None,list_proizvodi:dict=None,list_finder:list=None, finder:str=None):
    """
    Obavezno:\n
    lista_stupci -> lista prema kojoj će se ispisivati stupci (svaki item u listi = stupac)\n
    
    Nije obavezno:\n
    list_proizvodi -> riječnik proizvoda iz kojeg će se izvlačiti vrijednosti za stupce\n
    list_finder -> lista vrijednosti iz kojih će se izvlačiti nazivi riječnika(npr. banana...)\n
    finder -> vrijednot sa pomoću koje se dohvaćaju specifične tablice/ispisi
    \t id = prilikom provjere stanja vraća id, opis i trenutno stanje svih proizvoda ispod navedene granice\n
    \t full = tablica sa svim stupcima i proizvodima\n
    \t racun =  \n



    """

    #ISPIS ZA STANJE
    if list_proizvodi != None and list_finder != None and finder == "id":
        print("_"*20*len(lista_stupci),"\n")
        for stupac in lista_stupci:
            if lista_stupci.index(stupac) == 0:
                print(stupac.title(),"\t\t",end="")
            elif lista_stupci.index(stupac) == 1:
                print(stupac.title(),"\t\t\t",end="")
            elif lista_stupci.index(stupac) == 2:
                print(stupac.title(),"\t",end="")
            else:
                print(stupac.title(),"\t\t",end="")
        print()
        print("_"*20*len(lista_stupci),"\n")
        
        for proizvod in list_proizvodi:
            for id in list_finder:
                if id in proizvod["id"]:
                    sifra = proizvod["id"]
                    opis = proizvod["opis"]
                    stanje = proizvod["stanje"]
                    
                    if len(sifra)<8:
                        print(sifra,"\t\t",end ="")
                    else:
                        print(sifra,"\t",end ="")
                    if len(opis)<=12:
                        print(opis,"\t\t",end="")
                    else:
                        print(opis,"\t",end="")
                    print(stanje,end="")
                    print()


    #ISPIS ZA RAČUN lista_stupci = ["Redni broj","Id","Opis", "Jed.cijena", "Kolicina", "Ukupno"]
    elif list_proizvodi != None and list_finder != None and finder == "racun":
        print("_"*20*len(lista_stupci),"\n")
        for stupac in lista_stupci:
            if lista_stupci.index(stupac) == 0:
                print("\t",stupac.title(),"\t",end="")
            elif lista_stupci.index(stupac) == 1:
                print(stupac.title(),"\t\t",end="")
            elif lista_stupci.index(stupac) == 2:
                print(stupac.title(),"\t\t\t",end="")
            elif lista_stupci.index(stupac) == 3:
                print(stupac.title(),"\t",end="")
            else:
                print(stupac.title(),"\t\t",end="")
        print()
        print("_"*20*len(lista_stupci),"\n")
        
        for proizvod in list_proizvodi:
            
            
                
            rb = proizvod["redni broj"]    
            sifra = proizvod["id"]
            opis = proizvod["opis"]                    
            cijena = proizvod["cijena"]
            stanje = proizvod["stanje"]
            kolicina = proizvod["kolicina"]
            ukupno = cijena * kolicina
        #ispis redni broj
            if len(str(rb))<=4:
                print("\t",rb,"\t",end="")
            else:
                print("\t",rb,"\t",end="")    
        #ispis sifre
            if len(sifra)<8:
                print(sifra,"\t\t",end ="")
            else:
                print(sifra,"\t",end ="")
        #ispis opisa
            if len(opis)<=12:
                print(opis,"\t\t",end="")
            elif len(opis)<=4:
                print(opis,"\t\t\t",end="")
            else:
                print(opis,"\t",end="")
        #ispis cijena
            if len(str(cijena))<=5:
                print(cijena,"\t\t",end="")
            else:
                print(cijena,"\t",end="")
        #ispis kolicina
            if len(str(kolicina))<=4:
                print(kolicina,"\t\t\t",end="")
            else:
                print(kolicina,"\t\t",end="")
        #ispis ukupno
            if len(str(ukupno))<=4:
                print(ukupno,"\t\t",end="")
            else:
                print(round(ukupno,2),"\t",end="")
            print()


    #FULL ISPIS
    

    elif list_proizvodi != None and finder == "full":
        lista_key_stupac = []
        print("_"*20*4,"\n")
        for key in list_proizvodi[0].keys():
            lista_key_stupac.append(key)
            if key == "id":
                print(key.title(),"\t\t",end="")
            elif key == "opis":
                print(key.title(),"\t\t\t\t",end="")
            elif key == "cijena":
                print(key.title(),"\t\t",end="")
            else:
                print(key.title(),"\t\t",end="")
        print()
        print("_"*20*4,"\n")
        for proizvod in list_proizvodi:
            for key in proizvod.keys():
                if key == "id":
                    if len(proizvod["id"])<8:
                        print(proizvod["id"],"\t\t",end ="")
                    else:
                        print(proizvod["id"],"\t",end ="")

                elif key == "opis":
                    if len(proizvod["opis"])<=4:
                        print(proizvod["opis"],"\t\t\t\t",end="")
                    elif len(proizvod["opis"])<=12:
                        print(proizvod["opis"],"\t\t\t",end="")
                    else:
                        print(proizvod["opis"],"\t\t",end="")

                elif key == "cijena":
                    print(proizvod["cijena"],"\t\t",end="")
                else:
                    print(proizvod["stanje"],"\t\t",end="")
            print()
    
    elif list_proizvodi != None and finder == "stanje":
        lista_key_stupac = []
        print("_"*20*4,"\n")
        for key in list_proizvodi[0].keys():
            lista_key_stupac.append(key)
            if key == "id":
                print(key.title(),"\t\t",end="")
            elif key == "opis":
                print(key.title(),"\t\t\t\t",end="")
            elif key == "stanje":
                print(key.title(),"\t\t",end="")
            else:
                None
        print()
        print("_"*20*4,"\n")
        for proizvod in list_proizvodi:
            for key in proizvod.keys():
                if key == "id":
                    if len(proizvod["id"])<8:
                        print(proizvod["id"],"\t\t",end ="")
                    else:
                        print(proizvod["id"],"\t",end ="")

                elif key == "opis":
                    if len(proizvod["opis"])<=4:
                        print(proizvod["opis"],"\t\t\t\t",end="")
                    elif len(proizvod["opis"])<=12:
                        print(proizvod["opis"],"\t\t\t",end="")
                    else:
                        print(proizvod["opis"],"\t\t",end="")

                elif key == "cijena":
                    None
                else:
                    print(proizvod["stanje"],"\t\t",end="")
            print()
        
def vrati_rijecnik(finder_value:str,  lista_proizvoda:list) -> str:
    """
    
    finder_value -> vrijednos artikla kojem je ključ "id" (npr. "abc123" koji vraća "Maslo Megle 250g")\n
    lista_proizvoda -> lista sa riječnicima u kojoj će se tračiti id iz finder_value argumenta
    
    """  
    
    
    
    for proizvod in lista_proizvoda:
        if proizvod["id"] == finder_value:
            artikl = lista_proizvoda.index(proizvod)
            return artikl
            

def confirm() -> bool:
    """
    vraća True ili False ovisno o unosu\n
    koristi se u kodu gdje želim da korisnik potvrdi određene radnje
    """
    

    while True:
        check = input("Želite li potvrditi uneseno? (da/ne): ")
        match check.capitalize():
            case "Da":
                return True
            case "Ne":
                return False
            case _:
                pass   
    
def check_if_id_taken(id:str, lista_proizvoda:list) -> bool:
    """
    id -> vrijednost ključa "id" koja će se uspoređivati sa ostalim vrijednostima u listi te vratiti True ukoliko već postoji ili False ukoliko ne\n
    \tnpr. vrijednost "abc123" je već zauzeta u artiklu "Maslo Megle 250g", a vrijednost "12345abc" nije 
    """
    
    for proizvod in lista_proizvoda:
        if id == proizvod["id"]:            
            return True
            
    #kad petlja završi nije vratilo ništa te znači da nema navedenog id-a
    return False


def enter_to_continue() -> None:
    user_input = input("Press enter to continue...")
    match user_input:
        case _:
            pass


def input_validation() -> int:
    """
    funkcija pokušava varijablu "izbor" pretvoriti u int, ako ne onda se traži ponovan unos\n
    koristi se prilikom odabira opcija u meni-u kako ne bi izbacivalo errore
    """
    izbor = input("Unesite željenu opciju: ")        
    try:        
        izbor = int(izbor)
    except ValueError:
        print ("Odabir mora biti cijeli broj!")
        enter_to_continue()
    else:         

        return int(izbor)










def main():
    pass









if __name__ == "__main__":
    main()