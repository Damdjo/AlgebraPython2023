#zad40 provjera OIB-a 
# https://regos.hr/app/uploads/2018/07/KONTROLA-OIB-a.pdf  

def lengthOIB(input):
    return len(str(input))

def provjera(broj):
    # 1. korak
    broj = str(broj)
    ostBroj = int(str(broj[0])) + 10
    # nastaviti , treba napraviti petlju koja će ponavljati korake 2,3,4,5  na brojevima 2-11 OIB-a
    for ostaliBrojevi in range(1,len(broj)):
        
        # 2. korak
        ostatak = ostBroj%10
        if ostatak == 0:
            ostatak = 10
        # 3. korak
        umnozak = ostatak * 2
        # 4. korak
        umnozak %= 11
        # 5. korak
        ostBroj = umnozak + int(broj[ostaliBrojevi])
        
    return ostBroj
    





OIB = 0
while lengthOIB(OIB) != 11:
    OIB = int(input("Unesite OIB za provjeru: "))
    if lengthOIB(OIB) != 11:
        print("Krivi unos, pokušajte ponovno!")




check = provjera(OIB)

if check == 1 or check == 11:
    print(f"OIB {OIB} je ispravan!")
else:
    print("Uneseni OIB je neispravan")

