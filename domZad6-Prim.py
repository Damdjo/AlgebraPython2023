
#Implementacija funkcija u program iz zadatka 23 (primarni brojevi) 

check = True

listaBrojeva = [1, 2]

def userInput():
    uneseniBroj = int(input("Unesite cijeli broj u rasponu od 10 do 1000: "))
    if uneseniBroj < 10 or uneseniBroj > 1000:
        print("Krivi unos!")
    return uneseniBroj

def primeCheck(num):
    global listaBrojeva    
    #provjera primarnog broja
    isPrime = True
    for broj in range(2,num):
        if testBroj%broj==0:
            isPrime = False
            break
    if isPrime:
        listaBrojeva.append(testBroj)  


        
##
# Main program
##


while check:
    
    #provjera unosa
    uneseniBroj = userInput()
    if uneseniBroj < 10 or uneseniBroj > 1000:
        continue
    for testBroj in range(3, uneseniBroj):
        primeCheck(testBroj)
    
    print(f"U rasponu od 0 do {uneseniBroj}, primarni brojevi su:", end =" ")
    for broj in listaBrojeva:
        print(broj, end=" ")   
    
    check = False



    