# Umjetničko klizanje (izračun bodova i rang liste) google pravila -> min, max
# ocjene od 0.0 do 6.0, najveća i najmanja se odbacuju, do 9 sudaca, minimalno 4, unosi korisnik
import random
ocjene = []
brojSudaca = 0

def ocjenaRand():
    randOcjena = round(random.uniform(0.0,6.0), 1)
    return randOcjena

def ocjenaUser(counter):
    while True:
        userInput = float(input(f"Unesite {counter+1}. ocjenu u rasponu od 0.0 - 6.0: "))
        if userInput < 0.0 or userInput > 6.0:
            print("Krivi unos!")
        elif userInput >= 0.0 and userInput <= 6.0:
            break
    return userInput

def kolikoSudaca():
    global brojSudaca
    while True:
        userInput = int(input("Unesite broj sudaca u rasponu od 4 - 9: "))
        if userInput < 4 or userInput > 9:
            print("Krivi unos!")
        elif userInput >= 4 and userInput <= 9:
            break
    
    return userInput
 
def cutMinMax(list):
    global ocjene
    max = 0.0
    min = 6.0
    for ocjena in ocjene:

        #Max
        if ocjena > max:
            max = ocjena
        else:
            pass

        #Min
        if ocjena < min:
            min = ocjena
        else:
            pass
    if min == max:
        pass
    else:
        ocjene.remove(float(max))
        ocjene.remove(float(min))
        

brojSudaca = kolikoSudaca()
status = True
while status:
    randIliNe = input("Želite li da računalo nasumično generira ocjene? (y/n): ")
    if randIliNe == "y" or randIliNe == "Y":
        for broj in range(brojSudaca):
            ocjene.append(ocjenaRand())
            status = False
            

    elif randIliNe == "n" or randIliNe == "N":
        for broj in range(brojSudaca):
            ocjene.append(ocjenaUser(broj))
            status = False
            
    else:
        print("Krivi unos!")
        status = True
        
        





print()
print(f"{brojSudaca} sudaca vas je ocjenilo sa ocjenama: ", end = "")
for ocjena in ocjene:
    print(ocjena, end = " ")
print()
cutMinMax(ocjene)
sum = 0
for broj in ocjene:
    sum += broj
sum = round((sum), 1)
prosjek = round(sum / len(ocjene),1)
print()
print("Nakon micanja najniže i najviše ocjene preostaju ocjene: ", end = "")
for ocjena in ocjene:
    print(ocjena, end = " ")
print()
print(f"\nZbroj navedenih ocjena iznosi ({sum}) te kad se podjele sa brojem preostalih ocjena ({len(ocjene)}), \n dobiveni prosjek je {prosjek}!")