brojevi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for broj in brojevi:
    print(broj, end = " ")

names = ["Mate", "Stipe", "Jure"]
for name in names:
    print(name)

print()
print()

mixed = [10, "deset", True, 7.42]
print(mixed)

for element in mixed:   
    print(element)

print()

"""mixed = [10, "deset", True, 7.42]
suma = 0
print(mixed)

for element in mixed:
    sum = sum + element   
    #print(element)
print(sum)

print()"""

mixed = [10, 3.14, 5, 7.42]
sum = 0
print(mixed)

for element in mixed:
    sum += element   
    #print(element)
print(round(sum,2))

print()