import random

def main():
    
    hello("Mate")
    neprimam()
    print(slucajni())
    print(gornjiBroj(4))


def hello(ime):
    print(f"Hello {ime}")


def neprimam():
    print("*"*30)

def slucajni():
    broj = random.randint(1,10)

    return broj

def gornjiBroj(gornji):
    lista = []
    for broj in range(gornji):
        lista.append(broj)
    return lista

def zamjeni(b1, b2):
    temp = b1
    b1 = b2
    b2 = temp
    


main()