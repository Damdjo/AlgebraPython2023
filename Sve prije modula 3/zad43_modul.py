#pripremimo modul koji ćemo koristiti

#napišimo funkciju addNumberToList (lista:list, broj:int) -> bool
#testiramo nalazi li se broj u listi
#ukoliko se nalazi vraćamo False
#ukoliko se ne nalazi, dodajemo ga u listu i vraćamo True

def main():





    #print("Ušli smo u main")
    listaBrojeva = [4, 11, 17, 7, 9]
    print(top3(listaBrojeva))
    print(topn(listaBrojeva,3))
   

    """broj = 10

    if addNumberToList(listaBrojeva,broj):
        print(f"U listu je dodan broj {broj}")
    else:
        print(f"Broj {broj} se već nalazi u listi")

    print(listaBrojeva)
   

    listaOpcija = ["Ulaz", "Dodaj", "Ukloni"]
    meni(listaOpcija,False)
    """


def addNumberToList(lista:list, broj:int) -> bool:
    
    if broj in lista:
        return False
    else:
        lista.append(broj)
        return True
    

#napraviti funkciju koja prima listu stavki u meniju i ispisuje ih numerički od 1
# zadnja opcija je 0. Izlaz/Logout

def meni(listaOpcijaZaMeni:list, izlaz:bool = True) -> None:
    print("*"*30)
    print(" "*12,"MENI"," "*12)
    print("*"*30)
    print()
    for broj, opcija in enumerate(listaOpcijaZaMeni):
        print(f"\t{broj+1}. {opcija}")
    if izlaz:
        print(f"\t0. Izlaz")
    print()
    print

#dodati funkciju top_3 u modul koja prima listu i vraća listu od tri najveća broja
#primjeniti je na kraju prethodnog programa i ispisati u obliku:
#Najveći brojevi:
# 1. 92
# 2. 73
# 3. 42

def top3(lista:list) -> None:
    """Funkcija prima listu (lista) te će proći kroz nju i vratiti najveća 3 broja"""
    listOfTop3 = [0]
    listOfTop3.append(lista[0])
    if len(lista) < 3:
        print("Lista nema dovoljan broj brojeva da bi se ispisala najveća 3 broja!")
        return None
    for item in lista:
        
        if item > min(listOfTop3) and len(listOfTop3)<3:
            listOfTop3.append(item)
        elif item > min(listOfTop3) and len(listOfTop3)>=3:
            listOfTop3.append(item)
            listOfTop3.remove(min(listOfTop3))
    listOfTop3.sort()    
    return listOfTop3


        






 
#u modul dodati funkciju top_n koja prima listu i broj n o kojem ovisi broj najvecih npr. top_n(lista, 3)
        

def topn(lista:list, n:int) -> None:
    """Funkcija prima listu (lista) te će proći kroz nju i vratiti najvećih (n) brojeva"""
    listOfTopN = [0]
    listOfTopN.append(lista[0])
    if len(lista) < n:
        print(f"Lista nema dovoljan broj brojeva da bi se ispisala najveća/ih {n} broja/eva!")
        return None
    for item in lista:
        
        if item > min(lista) and len(listOfTopN)<n:
            listOfTopN.append(item)
        elif item > min(lista) and len(listOfTopN)>=n:
            listOfTopN.append(item)
            listOfTopN.remove(min(listOfTopN))
    listOfTopN.sort()      
    return listOfTopN










if __name__ == "__main__":
    main()
    