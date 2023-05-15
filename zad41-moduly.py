#napisati funkciju koja će za zadana dva broja ispisati parne brojeve između (uključujući) ta dva broja
#funkciju nazvati parni

def parni(pocBroj,krajBroj):
    listaParnih = []
    for broj in range(pocBroj,krajBroj+1):
        if int(broj)%2==0:
            listaParnih.append(broj)    
    return listaParnih

def parniLista(lista):
    listaParnih = []
    for broj in lista:
        if int(broj)%2==0:
            listaParnih.append(broj)    
    return listaParnih

def neParni(pocBroj,krajBroj):
    listaNeParnih = []
    for broj in range(pocBroj,krajBroj+1):
        if broj%2==1:
            listaNeParnih.append(broj)    
    return listaNeParnih

def neParniLista(lista):
    listaNeParnih = []
    for broj in lista:
        if broj%2!=0:
            listaNeParnih.append(broj)    
    return listaNeParnih

def maximum(lista):
    maxBroj = int(lista[0])
    for broj in lista:
        if int(broj) > maxBroj:
            maxBroj = int(broj)
    return maxBroj

def maximumMod(lista):
    parnaLista = parniLista(lista)
    if parnaLista != None:
        maxParni = parnaLista[0]
        for broj in parnaLista:
            if int(broj) > int(maxParni):
                maxParni = int(broj)
        return maxParni
    else:
        return None

def minimum(lista):
    minBroj = 0
    for broj in lista:
        if minBroj == 0 and 0 not in lista:
            minBroj = int(lista[0])
        if int(broj) < minBroj:
            minBroj = int(broj)
    return minBroj






parnaLista = parni(7,17)
neParnaLista = neParni(7,17)

print(parnaLista,"\n", neParnaLista)

testList = ["2","3","4","5","6","7","8","9","10",]


print("Lista brojeva kao stringovi","\n",maximumMod(testList))


