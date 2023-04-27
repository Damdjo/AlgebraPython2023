a = 4

#funkcija za ispis a
def ispisA():
    global a
    a = 8
    print("Unutar: ", a)
    a += 1
    print("Unutar: ", a)


print("Van: ", a)

ispisA()

print("Van: ", a)