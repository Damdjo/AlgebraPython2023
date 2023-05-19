def sucelje(lista:list, izlaz:bool=True) -> None:
    print('*'*30)
    print(' '*12,'MENI',' '*12)
    print('*'*30)
    for broj, stavka in enumerate(lista):
        print(f'\t{broj+1}. {stavka}')
    if izlaz:
        print('\t0. Izlaz')

def tablicaIspis(lista_stupci:list=None,list_proizvodi:dict=None,list_finder:list=None, finder:str=None):
    """
    Obavezno osim ako je full ispis:\n
    lista_stupci -> lista prema kojoj će se ispisivati stupci (svaki item u listi = stupac)\n
    
    Nije obavezno:\n
    list_proizvodi -> riječnik proizvoda iz kojeg će se izvlačiti vrijednosti za stupce\n
    list_finder -> lista vrijednosti iz kojih će se izvlačiti nazivi riječnika(npr. banana...)\n
    finder -> vrijednot sa pomoću koje se dohvaćaju specifične tablice/ispisi
    \t id = prilikom provjere stanja vraća id, opis i trenutno stanje svih proizvoda ispod navedene granice
    \t full = tablica sa svim stupcima i proizvodima



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
                    if len(proizvod["opis"])<=12:
                        print(proizvod["opis"],"\t\t\t",end="")
                    else:
                        print(proizvod["opis"],"\t\t",end="")

                elif key == "cijena":
                    print(proizvod["cijena"],"\t\t",end="")
                else:
                    print(proizvod["stanje"],"\t\t",end="")
            print()
        

# proizvod={'id':'abc123', 'opis':'Maslo Megle 250g', 'cijena':18.90, 'stanje':132}

        

                    








stupciTab =  ["Id", "Opis", "Stanje","test","test2"]


def main():
    pass









if __name__ == "__main__":
    main()