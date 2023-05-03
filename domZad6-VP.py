#Implementacija funkcija u program iz zadatka 18/ domaće zadaće 4 (IF tablica) 



vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes', 'ST 001 ZZ',2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dost voz', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dost voz', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
}

listaAdd = ["KLJUČ", "TIP", "IME PROIZVOĐAČA", "REGISTARSKU OZNAKU", "GODINU PROIZVODNJE", "CIJENU (EUR)"]
checkList = [0, "string1", "string2", "string3", 4, 5.0]

# FUNKCIJA ZA DODAVANJE/IZMJENU RETKA U TABLICI
def addItemToDict():
    global vozni_park
    #dodaj checkValue funkciju
    tempList = []
    tempKey = 0
    tempStr = ""
    tempInt = 0
    tempFloat = 0.0
    prolaz = True
    for num in range(len(listaAdd)):
        if num == 0 or num == 4:                        
            tempInt = int(input(f"Unesite vrijednost za {listaAdd[num]} vozila (int): "))
            if num == 0:    
                prolaz = doubleCheck(tempInt)
                if prolaz == False:
                    break
                
            tempList.append(tempInt)

        elif num == 5:
            tempFloat = float(input(f"Unesite vrijednost za {listaAdd[num]} vozila (float): "))
            tempList.append(tempFloat)
        else:
            tempStr = input(f"Unesite vrijednost za {listaAdd[num]} vozila (string): ")
            tempList.append(tempStr)
    print(tempList)
    if prolaz == False:
        print("Greška")

    else:
        tempKey = tempList[0]
        tempList.pop(0)
        vozni_park.update({tempKey: tempList})


def deleteItemFromDict():
    global vozni_park
    row = int(input(f"Unesite redni broj vozila koje želite izbrisati: "))
    prolaz = doubleCheck(row)
    if prolaz == True:
        vozni_park.pop(row)  
    else:
        print("Prekid radnje!")   
        
        
    
    


def doubleCheck(dictKey):
    global status
    if dictKey in vozni_park.keys():
        doubleCheck = input("Jeste li sigurni da želite urediti/obrisati već postojeće vozilo? (y/n):")
        if doubleCheck == "n":
            return False
        elif doubleCheck == "y":
            return True
        else:
            print("Krivi unos")
            return False
    


"""
CEKAM DOK NE RADIMO TRY EXCEPT
def checkValue(tempType):

    #Provjera unesene vrijednosti kada se odabere opcija 2 u izborniku
    #1. argument je trenutni unos, a 2. odgovarajuća vrijednost 
    #iz tablice checkList

    while True:
        userInput = input(f"Unesite vrijednost za {listaAdd[tempType]} vozila: ")
        global checkList
        if type(userInput) == type(checkList[tempType]):
            break

        elif type(userInput) != type(checkList[tempType]) and type(checkList[tempType]) == int:
            int(userInput)
            break
        
        elif type(userInput) != type(checkList[tempType]) and type(checkList[tempType]) == float:
            float(userInput)
            break
        
        else:
            print(type(userInput))
            print("Krivi unos!")
            return True
    return userInput
"""      


# ISPIS TABLICE
def iFace():
    print()
    headerTop = f"ID\t  Tip\t\tProizvođač\tRegistarska\tGodina prve\tCijena"
    headerBot = f"  \t     \t\t          \toznaka     \tregistracije\t(EUR)      "
    headerUndeline = "_"*80
    print(headerTop, "\n", headerBot, "\n", headerUndeline, sep="")
    for key, value in vozni_park.items():
        print(f"{key}", end = "\t")
        
        for item in value:
            if len(str(item)) >= 8:
                print(f"{item}", end="\t")
            
            elif len(str(item)) > 5 and len(str(item)) < 8:
                print(f"{item}", end="\t\t")
            
            elif len(str(item)) <= 5:
                print(f"{item}", end="\t\t")        
            
            else:
                print(f"{item}", end="\t\t\t") 

        print()
    print()

iFace()

def menu():
    global status
    print("*"*80)
    print(" "*37,"MENI"," "*37)
    print("*"*80)
    print()
    print("\t1. Ispis tablice vozila")
    print("\t2. Dodavanje novog/uređivanje postojećeg vozila")
    print("\t3. Brisanje vozila")
    print()
    print("\t0. Izlaz")    
    print("\n","*"*80) 
    status = int(input("\n\tUnesite željenu akciju: "))
       


status = -1
while status != 0:
    menu()
    if status == 1:
        iFace()
    elif status == 2:
        addItemToDict()
    elif status == 3:
        deleteItemFromDict()
    else:
        continue
    

print("\nHvala na korištenju!")
print(vozni_park)


"""iter = 0
for item in (checkList):
    print(type(item),"item")
    
    print(type(checkList[iter]),checkList[iter],"lista")
    iter+=1

for item in checkList:
    print(type(item))
"""

"""print(checkValue(0,0))
print(checkValue("0",1))
print(checkValue("0",2))
print(checkValue("0",3))
print(checkValue(0,4))
print(checkValue(0.0,5))"""