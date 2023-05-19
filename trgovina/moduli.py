def sucelje(lista:list, izlaz:bool=True) -> None:
    print('*'*30)
    print(' '*12,'MENI',' '*12)
    print('*'*30)
    for broj, stavka in enumerate(lista):
        print(f'\t{broj+1}. {stavka}')
    if izlaz:
        print('\t0. Izlaz')