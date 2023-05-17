check = True

listaBrojeva = [1, 2]

while check:
    
    #provjera unosa
    uneseniBroj = int(input("Unesite cijeli broj u rasponu od 10 do 1000: "))
    if uneseniBroj < 10 or uneseniBroj > 1000:
        print("Krivi unos!")
        continue

    for testBroj in range(3, uneseniBroj):
        #provjera primarnog broja
        isPrime = True
        for broj in range(2,testBroj):
            if testBroj%broj==0:
                isPrime = False
                break
        if isPrime:
            listaBrojeva.append(testBroj)      

            
    
    
    
    print(f"U rasponu od 0 do {uneseniBroj}, primarni brojevi su:", end =" ")
    for broj in listaBrojeva:
        print(broj, end=" ")   
    
    check = False



    