#pripremimo modul koji ćemo koristiti

#napišimo funkciju addNumberToList (lista:list, broj:int) -> bool
#testiramo nalazi li se broj u listi
#ukoliko se nalazi vraćamo False
#ukoliko se ne nalazi, dodajemo ga u listu i vraćamo True

def main():





    """print("Ušli smo u main")
    listaBrojeva = [4, 11, 17, 7, 9]
    broj = 10

    if addNumberToList(listaBrojeva,broj):
        print(f"U listu je dodan broj {broj}")
    else:
        print(f"Broj {broj} se već nalazi u listi")

    print(listaBrojeva)
    """

    listaOpcija = ["Ulaz", "Dodaj", "Ukloni"]
    meni(listaOpcija,False)


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
        












if __name__ == "__main__":
    main()
    