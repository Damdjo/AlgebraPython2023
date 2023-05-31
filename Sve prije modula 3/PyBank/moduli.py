import os

def enter_to_continue():
    input("Pritisnite enter da nastavite...")

def meni(lista_izbora:list, izbornik:str, izlaz:bool=False, logout:bool=False):
    
    
    print("*"*100)
    duzina = int((100-len("PyBANK ALGEBRA"))/2)
    print(" "*duzina,"PyBANK ALGEBRA",sep="")
    print("\n")
    duzina = int((99-len(izbornik))/2)
    print(" "*duzina,izbornik.upper())
    print("\n\n")
    
    if lista_izbora != None:
        for broj, izbor in enumerate(lista_izbora):
            print (f"\t{broj+1}. {izbor}")

    if izlaz:
        print (f"\n\t0. Izlaz")
    if logout:
        print (f"\n\t0. Logout")


def init():
    print("_"*100)
    print("Još niste otvorili račun. Molimo prvo kreirajte račun. Hvala!")
    print("_"*100)




















def main():
    pass 
    
    
          
    



if __name__ == "__main__":
    main()