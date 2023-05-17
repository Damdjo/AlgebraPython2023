"""
print("Program za kvadriranje brojeva")


"""
broj1 = 5
broj2 = 0
try:
    rezultat = broj1/broj2
except ZeroDivisionError:
    print("Nije moguće dijeliti sa nulom")
else:
    print(rezultat)
print()

while True:
    usrInput = input("Unesite broj: ")
    try:
        broj = int(usrInput)
    except ValueError as e:
        print("Dogodila se pogreška: ", e)
        continue
    else:
        print("Else block",broj**2)
        break
    finally:
        print("Finally block")    