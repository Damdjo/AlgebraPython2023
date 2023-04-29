
#Implementacija funkcija u program iz zadatka 24 (kalkulator) 

def meni():
    print()
    print()
    print("*"*60)
    print("\t\tKalkulator")
    print("*"*60)
    print("\t\t1. Zbrajanje")
    print("\t\t2. Oduzimanje")
    print("\t\t3. Maximum")
    print("\t\t4. Minimum")
    print("\t\t0. Izlaz")
    print("*"*60)
    global status
    status = int(input("Unesite željenu akciju: "))
    print()

def zbrajanje():
    #Zbrajanje
    prviBroj = int(input("Unesite prvi broj za zbrajanje: "))
    drugiBroj = int(input("Unesite drugi broj za zbrajanje: "))
    print(f"\nZbroj {prviBroj} i {drugiBroj} je {prviBroj+drugiBroj}")

def oduzimanje():
    #Oduzimanje
    prviBroj = int(input("Unesite prvi broj za oduzimanje: "))
    drugiBroj = int(input("Unesite drugi broj za oduzimanje: "))
    print(f"\nRazlika {prviBroj} i {drugiBroj} je {prviBroj-drugiBroj}")

def maximum():
    #Max
    maxCheck = True
    maxBroj = 0
    while maxCheck:    
        trenutniBroj = int(input("Unesite broj za provjeru maximuma: "))
        if trenutniBroj == 0:
            print(f"\nNajveći broj je: {maxBroj}")
            maxCheck = False
            break
        elif maxBroj == 0 and trenutniBroj != 0:
            maxBroj = trenutniBroj
            print("Unesite sljedeći broj ili \"0\" za izlazak")
        elif trenutniBroj > maxBroj and trenutniBroj != 0:
            maxBroj = trenutniBroj
            print("Unesite sljedeći broj ili \"0\" za izlazak") 
        else:
            print("Unesite sljedeći broj ili \"0\" za izlazak")

def minimum():
        #Min
    minCheck = True
    minBroj = 0
    while minCheck:    
        trenutniBroj = int(input("Unesite broj za provjeru minimuma: "))
        if trenutniBroj == 0:
            print(f"\nNajmanji broj je: {minBroj}")
            minCheck = False
            break
        elif minBroj == 0 and trenutniBroj != 0:
            minBroj = trenutniBroj
            print("Unesite sljedeći broj ili \"0\" za izlazak")
        elif trenutniBroj < minBroj and trenutniBroj != 0:
            minBroj = trenutniBroj
            print("Unesite sljedeći broj ili \"0\" za izlazak")  
        else:
            print("Unesite sljedeći broj ili \"0\" za izlazak")




status = -1
while status != 0:
    meni()
    
    if status == 1:
        zbrajanje()
    
    elif status == 2:
        oduzimanje()
    
    elif status == 3:
        maximum()
    
    elif status == 4:
        minimum()
print("Hvala na korištenju")
