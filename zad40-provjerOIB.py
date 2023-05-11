#zad40 provjera OIB-a 
# https://regos.hr/app/uploads/2018/07/KONTROLA-OIB-a.pdf  

def lengthOIB(input):
    return len(str(input))

def provjera(broj):
    # 1. korak - prva znamenka + 10
    broj = str(broj)
    ostBroj = int(str(broj[0])) + 10
    # 6. korak
    #petlja koja će ponavljati korake 2,3,4,5  na brojevima 2-11 OIB-a
    for ostaliBrojevi in range(1,len(broj)):
        
        # 2. korak - broj iz koraka 1 ako je program tek krenuo ili broj iz koraka 6 ako je prošao prvi korak podijelimo sa 10, ako je dobiveni broj 0, broj je 10
        ostatak = ostBroj%10
        if ostatak == 0:
            ostatak = 10
        # 3. korak - broj iz koraka 2 pomnoži se sa 2
        umnozak = ostatak * 2
        # 4. korak - umnožak iz koraka 3 modulo 11
        umnozak %= 11
        # 5. korak - sljedeća znamenka u unesenom OIB-u zbroji se sa ostatkom iz koraka 4.
        ostBroj = umnozak + int(broj[ostaliBrojevi])
        
    return ostBroj
    




# unos OIB-a koji će biti provjeren, mora sadržavati 11 brojeva
OIB = 0
while lengthOIB(OIB) != 11:
    OIB = int(input("Unesite OIB za provjeru: "))
    if lengthOIB(OIB) != 11:
        print("Krivi unos, pokušajte ponovno!")




check = provjera(OIB)
# 7. korak provjerava je li zadnja znamenka 0
if (11 - check)%10 == 0:
    print(f"OIB {OIB} je ispravan!")
else:
    print("Uneseni OIB je neispravan")

