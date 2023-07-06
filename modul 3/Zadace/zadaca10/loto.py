#napraviti loto generator fiksni u GUI
#možemo koristiti pack, place ili grid ############ Za znatiželjne probati sva 3
#program izbacuje loto za eurojackpot
#2 labela u kojima će se prikazivati kombinacije 1.(5x50) 2.(2x12)
#centrirano piše Eurojackpot
#na dnu je gumb u kojem piše eurojackpot ili daj kombinaciju



#stari kod, izmijenjen da ostane samo Eurojackpot opcija
import random, os



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
    
    for komb in range(kolikoBrojeva):
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

def unosKombinacija(brojKombinacija,kolikoBrojeva,doKojegBroja,imaBonus=False):
    "Koliko kombinacija će se unositi, koliko brojeva svaka kombinacija ima, do kojeg broja će se generirati brojevi od 1 do unesenog argumenta, ima li igra bonus brojeve koje treba generirati"
    global status
    listTotal = []
    listBonusUsr = []
    listBonusRand = []

    for komb in range(brojKombinacija):
        userList = []
        for broj in range(kolikoBrojeva):
            check = True
            userNumInput = None
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
        #bonus brojevi ako ih se traži    
        if imaBonus and status == 3:
            bonusUser,bonusRand = bonusBroj(2)
            bonusUser.sort()
            listBonusUsr = bonusUser
            bonusRand.sort()
            listBonusRand = bonusRand

        listTotal.append(userList)
    return listTotal, listBonusUsr, listBonusRand

def bonusBroj(kolikoBonusBr):
    global status
    bonusUsrList = []
    bonusRandList = []
    if status == 3:
        for unos in range(kolikoBonusBr):
            tempBonus = int(input(f"Unesite {unos+1}. bonus broj: "))
            bonusUsrList.append(tempBonus)
        bonusRandList = vrtiBrojeve(2,12)
    return bonusUsrList, bonusRandList



def Eurojackpot():
    print("Odabrali ste Eurojackpot")
    brojKombinacija = int(input("Unesite broj kombinacija koje želite unjeti: "))
    uneseneKombinacije, bonusUsr, bonusRand = unosKombinacija(brojKombinacija,5,50,True)
    return uneseneKombinacije, bonusUsr, bonusRand

    


def provjeraPogBrojeva(userList,kolikoBrojeva,doKojegBroja,bonusListaUser=[],bonusListaRand=[]):
    global status
    
    for lista in range(len(userList)):
        tempList = userList[lista]
        randList = vrtiBrojeve(kolikoBrojeva,doKojegBroja)
        tempList.sort()
        randList.sort()
        pogodci = set(tempList).intersection(randList)
        pogodciBonus = set(bonusListaUser).intersection(bonusListaRand)        
        
        print("*"*60)
        print(f"\nKombinacija {lista+1}. \n\nUneseni brojevi: \t\t", end = "")
        for broj in tempList:
            broj = int(broj)
            if broj < 10:
                print(f" {broj}", end = " ")
            else:
                print(broj, end = " ")
        
        
        print("\nUneseni bonus brojevi su: \t", end = "")
        for broj in bonusListaUser:
            broj = int(broj)
            if broj < 10:
                print(f" {broj}", end = " ")
            else:
                print(broj, end = " ")
        print("")
        print(f"\n\nNasumično generirani brojevi: \t", end = "")
        for broj in randList:
            broj = int(broj)
            if broj < 10:
                print(f" {broj}", end = " ")
            else:
                print(broj, end = " ")
        
        print("\nGenerirani bonus brojevi su: \t", end = "")
        for broj in bonusListaRand:
            broj = int(broj)
            if broj < 10:
                print(f" {broj}", end = " ")
            else:
                print(broj, end = " ")

        print("\n")
        if pogodci != set():
            print("Pogođeni su brojevi: \t", end = "")
            for broj in pogodci:
                broj = int(broj)
                if broj < 10:
                    print(f" {broj}", end = " ")
                else:
                    print(broj, end = " ")
        else:
            print("Niste pogodili nijedan broj!")
        
        print()
        
        if pogodciBonus != set():
            print("Pogođeni su bonus brojevi: ", end = "")
            for broj in pogodciBonus:
                if broj < 10:
                    print(f" {broj}", end = " ")
                else:
                    print(broj, end = " ")
        else:
            print("Niste pogodili nijedan bonus broj!")
        print("\n","*"*60,sep = "")
    
    status = 0

def check_if_int(list:list):
    tempList = []
    for broj in list:
        try:
            int(broj)
        except ValueError as e:
            print(e)
        else:
            tempList.append(int(broj))
    print("*******",tempList)
    return tempList

def tkinterProvjera(userList,randList,bonusListaUser=[],bonusListaRand=[]):
    global status
    #os.system("cls")
    poruka_reg = ""
    poruka_bon = ""
    tempList = check_if_int(userList)
    tempListBonus = check_if_int(bonusListaUser)
    randList = randList
    tempList.sort()
    randList.sort()
    pogodci = set(tempList).intersection(randList)
    pogodciBonus = set(tempListBonus).intersection(bonusListaRand)        
    
    print("*"*60)
    print(f"\n\nUneseni brojevi: \t\t", end = "")
    for broj in tempList:
        if broj < 10:
            print(f" {broj}", end = " ")
        else:
            print(broj, end = " ")
    
    
    print("\nUneseni bonus brojevi su: \t", end = "")
    for broj in tempListBonus:
        if broj < 10:
            print(f" {broj}", end = " ")
        else:
            print(broj, end = " ")
    print("")
    print(f"\n\nNasumično generirani brojevi: \t", end = "")
    for broj in randList:
        if broj < 10:
            print(f" {broj}", end = " ")
        else:
            print(broj, end = " ")
    
    print("\nGenerirani bonus brojevi su: \t", end = "")
    for broj in bonusListaRand:
        if broj < 10:
            print(f" {broj}", end = " ")
        else:
            print(broj, end = " ")

    print("\n")
    if pogodci != set():
        print("Pogođeni su brojevi: \t", end = "")
        poruka_reg = "Pogođeni su brojevi: "
        for broj in pogodci:
            if broj < 10:
                print(f" {broj}", end = " ")
                poruka_reg += str(f"{broj} ")
            else:
                print(broj, end = " ")
                poruka_reg += str(f"{broj} ")
    else:
        print("Niste pogodili nijedan broj!")
        poruka_reg = "Niste pogodili nijedan broj!"
    
    print()
    
    if pogodciBonus != set():
        print("Pogođeni su bonus brojevi: ", end = "")
        poruka_bon = "Pogođeni su bonus brojevi: "
        for broj in pogodciBonus:
            if broj < 10:
                print(f" {broj}", end = " ")
                poruka_bon += str(f"{broj} ")
            else:
                print(broj, end = " ")
                poruka_bon += str(f"{broj} ")
    else:
        print("Niste pogodili nijedan bonus broj!")        
        poruka_bon = "Niste pogodili nijedan bonus broj!"
    print("\n","*"*60,sep = "")
    
    status = 0
    return poruka_reg, poruka_bon

def main():
    status = 3

    unos, bUsr, bRand = Eurojackpot()
    provjeraPogBrojeva(unos,5,50, bUsr, bRand)

if __name__ == "__main__":
    main()



#kraj stari kod


