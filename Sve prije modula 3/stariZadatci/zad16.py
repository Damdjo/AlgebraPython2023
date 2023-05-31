numbers = []
for num in range (0,21):
    numbers.append(num)

print()
print("Ispis liste:")
for i in numbers:
    print(i, end=" ")
print()

"""
numbers.clear()
print()
print("Ispis nakon clear():")
for i in numbers:
    print(i, end=" ")
print()
print(numbers)
"""

numbersCopy = numbers.copy()
print("Ispis numbers:")
for i in numbers:
    print(i, end=" ")
print()
print()
print("Ispis numbersCopy:")
for i in numbersCopy:
    print(i, end=" ")
print()

#numbers[0] = 15
num15InNumbers = numbers.count(15)
print(f"Broj 15 pojavljuje se {num15InNumbers} puta u listi brojevi.")

words = ["Python", "Algebra", "Programiranje"]
for i in words:
    print(i, end=" ")
print()
for i in numbers:
    print(i, end=" ")
print()
numbers.extend(words)
for i in numbers:
    print(i, end=" ")
print()



numbersIndexOfWordPython = numbers.index("Python")
print(numbersIndexOfWordPython)

#nasli smo gdje se nalazi rijec "Python"
#na to mjesto želimo staviti riječ "Java"

numbers[numbersIndexOfWordPython] = "Java"
print(numbers)

#pronađimo prvi put gdje se pojavi 15, zatim će nam taj broj biti argument za slice[::] sljedeće pretrage
#u toj pretrazi ćemo pronaći drugu pojavu broja 15


print("\n")
#određujemo na kojem će se indexu prvi puta pojaviti broj 15
numbers[0] = 15
#spremamo prvi index 
numbersIndexOfNum15 = numbers.index(15)

secondIndexList = numbers[numbersIndexOfNum15+1::]
secondIndex = secondIndexList.index(15)+numbersIndexOfNum15+1

print(f"prvi broj 15 u listi numbers je bio na indexu {numbersIndexOfNum15}, a drugi na indexu {secondIndex}")

"""
JOs nismo naucili kako se boriti sa greškama
numbers30 = numbers.index(30)
print(numbers30)
"""

print()
print("Ispis numbers:")
for i in numbers:
    print(i, end=" ")
print()

numbers.insert(11,15) 
print()
print("Ispis numbers:")
for i in numbers:
    print(i, end=" ")
print()

numbers.insert(11,words)
print()
print("Ispis numbers:")
for i in numbers:
    print(i, end=" ")
print()

print(numbers[11][2])

numbers.reverse()
print(numbers)

numbers.reverse()
print(numbers)

testList = [[1, 2], [3, 4], [5, 6]]
for subList in testList:
    subList.reverse()
testList.reverse()

print(testList)

print(words)
words.sort()
print(words)
