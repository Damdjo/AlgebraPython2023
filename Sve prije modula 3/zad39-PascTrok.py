"""#zad39 - Pascalov trokut
#Unijeti broj redova pascalovog trokuta (do max 10)
#formatirano ispisati koristeći tabulator
#                  1
#              1       1
#          1       2       1
#      1       3       3       1

*****************************NE RADI**************************************

brojRedova = int(input("Unesite broj redova za Pascalov trokut: "))

previousRow = []
currentRow = []
counter = 0
counterTab = brojRedova

def formulaZaIspis():
    global previousRow
    global currentRow
    global counter
    global counterTab

    #brojac
    counter = 0
    #
    currentRow = previousRow

    
    currentRow.append(1)
    print("\t"*counterTab, end = "")
    for int in currentRow:
        
        counter = 0
        if  counter < len(currentRow)/2:
            if len(previousRow) > 2 and counter != currentRow[0]:
                print(previousRow[int]+previousRow[int+1], end = "\t\t")
                counter += 1
            elif int == currentRow[0]:
                print(int, end = "\t\t")
                counter += 1
            elif int == currentRow[-1]:
                print(int, end = "\t\t")
                counter += 1
            elif len(previousRow) > 2:
                print(previousRow[int]+previousRow[int+1], end = "\t\t")
                counter += 1
        elif counter >= len(currentRow)/2:
            if len(previousRow) < 2:
                print(previousRow[int]+previousRow[int+1], end = "\t\t")
                counter -= 1
            elif int == currentRow[0]:
                print(int, end = "\t\t")
                counter -= 1
            elif int == currentRow[-1]:
                print(int, end = "\t\t")
                counter -= 1
            elif len(previousRow) < 2:
                print(previousRow[int]+previousRow[int+1], end = "\t\t")
                counter -= 1
        else:
            print("????")
        print(f"c={counter}!", end ="")
            
    
    #print(f"podjela {len(currentRow)/2}",len(currentRow),end = "")
    print()
    counterTab -= 1
    previousRow = currentRow

for broj in range(brojRedova):
    formulaZaIspis()

"""