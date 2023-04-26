#for petlja
print("for")
for broj in range(10):
    print(broj, end=" ")
print()



#for petlja neparni

for broj in range(1, 10, 2):
    print(broj, end=" ")
print()


for broj in range(10):
    if broj % 2 != 0:
        print(broj, end=" ")
print()

for broj in range(10):
    if broj % 2 == 0:
        continue        #ako je uvjet ispunjen, preskoci ostatak koda u bloku i vrati se na pocetak petlje
    print(broj, end=" ")
print()

#test breaka na ocjenu 6
for broj in range(1, 10):
    if broj % 6 == 0:
        break        #ako je uvjet ispunjen, preskoci ostatak koda u bloku i nastavi izvršavanje izvan petlje
    print(broj, end=" ")
print()

print("While")

#while
broj = 0
while broj < 10:
    print(broj, end=" ")
    broj += 1
print()

#while neparni
broj = 0
while broj < 10:
    print(broj, end =" ")
    broj += 1
print()

broj = 1
while broj < 10:
    print(broj, end =" ")
    broj += 2
print()

broj = 0
while broj < 10:
    if broj % 2 != 0:
        print(broj, end=" ")
    broj += 1
print()

"""#ne radi kod, broj se ne povećava
broj = 0    #broj je 0
while broj < 10:    #0 < 10 -> True
    if broj % 2 == 0:   #0 % 2 == 0 -> True
        continue    #Ostavi se svega i vrati se na While
    print(broj,end =" ")
    broj+=1"""

#možda radi
broj = 0    #broj je 0
while broj < 10:    #0 < 10 -> True
    if broj % 2 == 0:   #0 % 2 == 0 -> True
        broj += 1   #broj je 1
        continue    #Ostavi se svega i vrati se na While
    print(broj,end =" ")
    broj+=1
print()
broj = 1
while broj < 10:
    if broj % 2 != 0:
        print(broj, end=" ")
    broj += 1
    if broj == 6:
        break