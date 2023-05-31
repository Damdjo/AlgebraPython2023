#pripremamo modul koji ćemo koristiti
 
#napišimo funkciju add_number_to_list(lista:list, broj:int) -> bool
#testirajmo nalazi li se broj u listi
#ukoliko se nalazi vraćamo False
#ukoliko se ne nalazimo dodajemo ga u listu i vraćamo True
 
def main():
 
    '''
    print('Usli smo u main dio programa')
    lista_brojeva=[4, 11, 17, 7, 9]
    dodaj_broj=9
    if add_number_to_list(lista_brojeva, dodaj_broj):
        print(f'U listu je dodan broj {dodaj_broj}')
    else:
        print(f'Broj {dodaj_broj} se već nalazi u listi')
    print(lista_brojeva)
    '''
 
    lista=['Ulaz', 'Dodaj', 'Ukloni', 'Jos nesto']
    meni(lista)
 
 
 
def add_number_to_list(lista:list, broj:int) -> bool:
    #print(__name__)
    #print('Primljeno lista:',lista)
    #print('Primljeno broj:',broj)
    if broj in lista:
        return False
    else:
        lista.append(broj)
        return True
 
 
#napraviti funkciju koja prima listu stavki u meniju i ispisuje ih numerički od 1. 
#zadnja opcija je 0. Izlaz/Logout
 
def meni(lista_u_meniju:list, izlaz:bool=True) -> None:
    print('*'*30)
    print(' '*12,'MENI',' '*12)
    print('*'*30)
    for broj, stavka in enumerate(lista_u_meniju):
        print(f'\t{broj+1}. {stavka}')
    if izlaz:
        print('\t0. Izlaz')
 
 
 
 
 
if __name__=='__main__':
    main()
 