numbers = []
for broj in range(100):
    print(broj, end=" ")
    numbers.append(broj)
print()
print()

for number in numbers:
    print(number, end=" ")
print()
print()

print(numbers)
print()

djeljiviSa7 = []
for broj in range(0,100,7):
    print(broj, end=" ")
    djeljiviSa7.append(broj)

print()
print()
print(len(djeljiviSa7))


granica = int(input("Unesi gornju granicu: "))
lista = []

for broj in range(granica):
    lista.append(int(input(f"Unesite {broj+1}. broj:")))

print(lista)
    

