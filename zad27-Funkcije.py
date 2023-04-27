


def meni():

    """ Prazno ispisuje default meni """

    print()
    print("*"*60)
    print(" "*27,"MENI"," "*27)
    print("*"*60)
    print()

def zbroj(a,b):
    """ Zbroj 2 unesena argumenta """
    return a+b

def povrsina(a,b,brojStranica):
    """ Funkcija podrzava povrsinu trokuta (br-str = #) i cetverokuta (br-str=4)"""
    if brojStranica == 4:
        return a*b
    elif brojStranica == 3:
        return a*b/2
    else:
        return 0

meni()
print(f"Zbroj brojeva 5 i 7 je {zbroj(5,7)}")
print()

ta = 5
tb = 7
tbs = 3

ca = 4
cb = 7
cbs = 4

print(f"Površina poligona sa {tbs} strana/e je {povrsina(ta,tb,tbs)}")
print(f"Površina poligona sa {cbs} strana/e je {povrsina(ca,cb,cbs)}")
print(f"Površina poligona sa strana/e je {povrsina(4,4,7)}")
