import datetime


rijecnikClanova = {
1 : ["Ivan",    "Ivić",     datetime.date(2023,5,23),   datetime.date(1,1,1) , "Basic"],
2 : ["Pero",    "Perić",    datetime.date(2023,1,21),   datetime.date(1,1,1) , "Premium"],
3 : ["Mate",    "Matić",    datetime.date(2023,9,2),    datetime.date(1,1,1) , "Basic"],
4 : ["Ante",    "Antić",    datetime.date(2023,5,3),    datetime.date(1,1,1) , "Premium"],
5 : ["Jerko",   "Jerkić",   datetime.date(2023,5,14),   datetime.date(1,1,1) , "Basic"],
6 : ["Ana",     "Anić",     datetime.date(2023,3,27),   datetime.date(1,1,1) , "Premium"],
7 : ["Iva",     "Ivić",     datetime.date(2023,2,12),   datetime.date(1,1,1) , "Basic"],
8 : ["Petra",   "Petrić",   datetime.date(2023,11,23),  datetime.date(1,1,1) , "Premium"],
9 : ["Jelena",  "Jelić",    datetime.date(2023,12,16),  datetime.date(1,1,1) , "Basic"],
10 : ["Marija", "Marić",    datetime.date(2023,8,2),    datetime.date(1,1,1) , "Premium"]

}
#lista naziva stupaca
listaStupaca = ["BROJ ČLANA", "IME", "PREZIME", "DATUM UČLANJENJA", "DATUM ISTEKA ČLANARINE", "VRSTA ČLANARINE"]

def datetimeConvert(string):
    tempConverted = string.split("-")
    converted = datetime.date(int(tempConverted[0]),int(tempConverted[1]),int(tempConverted[2]))
    return converted

def keyCheck(key):
    global rijecnikClanova
    if key in rijecnikClanova.keys():
        answer = input("Jeste li sigurni da želite uređivati/izbrisati već postojećeg člana? Da/Ne: ").title()
        if answer == "Da":
            return True

        else:
            return False
    else:
        return False

def izbrisiClana():
    global rijecnikClanova
    red = int(input("Unesite red člana kojeg želite izbrisati: "))
    if red in rijecnikClanova.keys():
        if keyCheck(red):
            rijecnikClanova.pop(red)
        else:
            print("Prekid radnje!")
    else:
        print("Navedeni broj nije u tablici!")


def dodajClana():
    global rijecnikClanova
    tempKey = 0 #Privremenei ključ kojim će se redak dodavati
    tempStr = ""
    tempDate = ""
    tempList = []
    print("_"*70)
    print(" "*10,"Dodavanje novog člana")
    print("_"*70,"\n")
        
    for stupac in range(len(listaStupaca)):
        #Vrijednost u int: broj člana
        if stupac == 0:
            tempKey = int(input(f"Unesite vrijednost za {listaStupaca[stupac]}: "))
            tempList.append(tempKey)
        #Vrijednosti u str: ime, prezime, vrsta članarine
        elif stupac == 1 or stupac == 2 or stupac == 5:
            
            if stupac == 5:
                check = False
                while check != True:
                    tempStr = str(input(f"Unesite vrijednost za {listaStupaca[stupac]} člana: "))
                    if tempStr == "Basic" or tempStr == "Premium":
                        check = True
                        break
                    else:
                        pass                        

            else:
                tempStr = str(input(f"Unesite vrijednost za {listaStupaca[stupac]} člana: "))
                tempList.append(tempStr)
        #Vrijednosti u datetime: datum učlanjenja i datum isteka
        else:
            tempDate = str(input(f"Unesite vrijednost za {listaStupaca[stupac]} člana (u obliku GODINA-MJESEC-DAN): "))
            tempDate = datetimeConvert(tempDate)
            tempList.append(tempDate)
    
    if keyCheck(tempList[0]):      
        tempList.pop(0)
        rijecnikClanova.update({tempKey:tempList})
    elif keyCheck(tempList[0]) == False:
        tempList.pop(0)
        rijecnikClanova.update({tempKey:tempList})
    else:
        print("Odbacivanje izmjena!")




#4. član liste = 3. član + 1 mjesec
for key, value in rijecnikClanova.items():  
    
    value[3] = rijecnikClanova[key][2]+datetime.timedelta(31)


def tablica():
    #ispis tablice sa nazivima stupaca
    headerTop = f"ID\tIme\tPrezime\tDatum     \tDatum isteka\tVrsta"
    headerBot = f"  \t   \t       \tučlanjenja\tčlanarine   \tčlanarine      "
    headerUndeline = "_"*70
    print(headerTop, "\n", headerBot, "\n", headerUndeline, sep="")
    for key, value in rijecnikClanova.items():
        print(f"{key}", end = "\t")
        for item in value:
            print(f"{item}", end="\t")
        print()
    print()

def vratiNaDefault():
    #vraća tablicu na početno stanje
    global rijecnikClanova
    rijecnikClanova = {
1 : ["Ivan",    "Ivić",     datetime.date(2023,5,23),   datetime.date(1,1,1) , "Basic"],
2 : ["Pero",    "Perić",    datetime.date(2023,1,21),   datetime.date(1,1,1) , "Premium"],
3 : ["Mate",    "Matić",    datetime.date(2023,9,2),    datetime.date(1,1,1) , "Basic"],
4 : ["Ante",    "Antić",    datetime.date(2023,5,3),    datetime.date(1,1,1) , "Premium"],
5 : ["Jerko",   "Jerkić",   datetime.date(2023,5,14),   datetime.date(1,1,1) , "Basic"],
6 : ["Ana",     "Anić",     datetime.date(2023,3,27),   datetime.date(1,1,1) , "Premium"],
7 : ["Iva",     "Ivić",     datetime.date(2023,2,12),   datetime.date(1,1,1) , "Basic"],
8 : ["Petra",   "Petrić",   datetime.date(2023,11,23),  datetime.date(1,1,1) , "Premium"],
9 : ["Jelena",  "Jelić",    datetime.date(2023,12,16),  datetime.date(1,1,1) , "Basic"],
10 : ["Marija", "Marić",    datetime.date(2023,8,2),    datetime.date(1,1,1) , "Premium"]

}
    for key, value in rijecnikClanova.items():  
    
        value[3] = rijecnikClanova[key][2]+datetime.timedelta(31)



def menu():
    global status
    print("_"*70)
    print(" "*29,"MENI"," "*29)
    print("_"*70)
    print()
    print("\t1. Ispis tablice članova")
    print("\t2. Dodavanje novog/uređivanje postojećeg člana")
    print("\t3. Brisanje člana")
    print("\t4. Vrati početnu tablicu")
    print("\t5. Provjerite članstvo")
    print("\t6. Produživanje članstva")
    
    print()
    print("\t0. Izlaz")    
    print("\n","*"*70) 
    status = int(input("\n\tUnesite željenu akciju: "))

def provjeriClanstvo():
    global rijecnikClanova
    kljucClana = 0
    pronadeno = 0
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    for clan in rijecnikClanova.values():
        if ime in clan[0] and prezime in clan[1]:
            print(f"Član je pronađen, broj članske iskaznice je \"{kljucClana}\" i datum isteka članstva je {rijecnikClanova[kljucClana][3]}")
            pronadeno = kljucClana
        kljucClana += 1
    return pronadeno

def produziClanstvo():
    global rijecnikClanova
    indexClana = int(input("Unesite broj iskaznice člana kojemu produžujete članstvo: "))
    trajanje = int(input("Unesite mjeseci za koji produžujete članstvo: "))
    mjesec = datetime.timedelta(trajanje*31)
    rijecnikClanova[indexClana][3] = rijecnikClanova[indexClana][3]+mjesec
    



status = -1
while status != 0:
    menu()
    if status == 1:
        tablica()
    elif status == 2:
        dodajClana()
    elif status == 3:
        izbrisiClana()
    elif status == 4:
        vratiNaDefault()
    elif status == 5:
        provjeriClanstvo()
    elif status == 6:
        produziClanstvo()
    elif status == 0:
        print("Izlaz")
        break
print("Hvala na korištenju")



