numbers = []
for number in range(0,101):
    numbers.append(number)

#print(numbers)
HlNum = numbers[20:(45+1):6]
print(HlNum)

HlNum7 = numbers[14:(63+1):7]
print(HlNum7)

#hipotetsi ne znamo koliko je velka lista
#odaberi indexe od 20 do kraja liste

DvadesetDoKraja = numbers[20:]
print(DvadesetDoKraja)

DoDvadeset = numbers[:21]
print(DoDvadeset)

Parni = numbers[::2]
print(Parni)

print(numbers[-1])
print(numbers[0:3])
print(numbers[-4:-1])
print(numbers[:-9])
print(numbers[::-1])
print(numbers[:-3:-1])

print(numbers[10:20:-1])