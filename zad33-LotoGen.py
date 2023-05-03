# Loto generator
# Mora imati: MENI, broj kombinacija, ponuditi ispis N kombinacija (Random modul, nema ponavljanja brojeva), ovisno o igri napraviti formatirani ispis i vratiti se na meni
import random



def menu():
    global status
    print("\n")
    print("*"*60)
    print("*"*27,"LOTO","*"*27)
    print("*"*60)
    print("\n")
    print("1. 6/45")
    print("2. 7/39")
    print("3. Eurojackpot")
    print("0. Izlaz")
    print("\n")
    status = int(input("Odaberite željenu opciju: "))

def vrtiBrojeve(kolikoBrojeva, doKojegBroja):
    genList = []
    
    for komb in range(kolikoBrojeva+1):
        genNum = random.randint(1,doKojegBroja)
        check = True        
        while check:
            if genNum in genList:
                genNum = random.randint(1,doKojegBroja)
            else:
                check = False
                break
        genList.append(genNum)
        
    return genList

def unosKombinacija(brojKombinacija,kolikoBrojeva,doKojegBroja):
    
    listTotal = []
    for komb in range(brojKombinacija):
        userList = []
        for broj in range(kolikoBrojeva):
            check = True
            while check:
                userNumInput = int(input(f"Unesite {broj+1}. broj za {komb+1} kombinaciju: "))
                if userNumInput in userList:
                    print("Broj je već unesen!")
                elif userNumInput <= 0 or userNumInput > doKojegBroja:
                    print("Broj nije u rasponu za odabranu listu!")
                else:
                    check = False
                    break
            userList.append(userNumInput)
        listTotal.append(userList)
    return listTotal




def loto6kroz45():
    print("Odabrali ste loto 6/45")
    brojKombinacija = int(input("Unesite broj kombinacija koje želite unjeti: "))
    uneseneKombinacije = unosKombinacija(brojKombinacija,6,45)
    return uneseneKombinacije


    
def provjeraPogBrojeva(userList,kolikoBrojeva,doKojegBroja):
    for lista in range(len(userList)):
        tempList = userList[lista]
        randList = vrtiBrojeve(kolikoBrojeva,doKojegBroja)
        tempList.sort()
        randList.sort()
        print(lista+1," ",tempList,"\n   ",randList)
        print(set(tempList).intersection(randList))

        #funkcija za uređenje ispisa











status = -1

while status != 0:
    if status == -1:
        menu()    
    if status == 1:
        unos = loto6kroz45()
        provjeraPogBrojeva(unos,6,45)
        status = -1
    
    elif status == 0:
        print("Izlaz")
    
    else:
        print("Krivi odabir!")
        menu()



print("Hvala na igri")



        
