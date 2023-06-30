def main():
    print('U mainu modula helpers')
    password='adljaldjflajdf'
    print(validate_password(password))

def meni(lista_u_meniju:list, izlaz:bool=True) -> None:
    print('*'*30)
    print(' '*12,'MENI',' '*12)
    print('*'*30)
    for broj, stavka in enumerate(lista_u_meniju):
        print(f'\t{broj+1}. {stavka}')
    if izlaz:
        print('\t0. Izlaz/Log out')

def validate_password(uneseni_password:str, broj_znakova:int=6) -> bool:
    #print(len(uneseni_password))
    if len(uneseni_password)>=broj_znakova:
        return True
    return False

if __name__=='__main__':
    main()



