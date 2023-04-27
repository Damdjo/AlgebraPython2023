"""sustav menija za kalkulator
Napisati program koji će ispisati meni u oblilu
    Meni:
    1. Zbrajanje
    2. Oduzimanje
    3. Najveci
    4. Najmanji
    0. Izlaz

1 korisnik unosi 2 broja, prikazuje se recenica u obliku " zbroj je..."

2. Korisnik unosi 2 broja, prikazuje se recenica u obliku " razlika je ..."

3. Korisnik unosi jedan po jedan broj, prvi se postavlja kao max, a zatim svaki sljedeci uspoređuje 
s tim brojem i postavlja na max ako je veci, ako se unese 0, ispisuje se 
zadnji uhvaceni najveci broj u obliku " najveci broj je ..."

4. Isto kao za 3 " najmanji broj je ..."

Nakon zavrsetka svake od opcija, iznova se prikazuje meni 1,2,3,4,0

nema korištenja lista
"""
status = -1
while status != 0:
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
    status = int(input("Unesite željenu akciju: "))
    print()
    
    if status == 1:
        #Zbrajanje
        prviBroj = int(input("Unesite prvi broj za zbrajanje: "))
        drugiBroj = int(input("Unesite drugi broj za zbrajanje: "))
        print(f"\nZbroj {prviBroj} i {drugiBroj} je {prviBroj+drugiBroj}")
    
    elif status == 2:
        #Oduzimanje
        prviBroj = int(input("Unesite prvi broj za oduzimanje: "))
        drugiBroj = int(input("Unesite drugi broj za oduzimanje: "))
        print(f"\nRazlika {prviBroj} i {drugiBroj} je {prviBroj+drugiBroj}")
    
    elif status == 3:
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
    
    elif status == 4:
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
print("Hvala na korištenju")