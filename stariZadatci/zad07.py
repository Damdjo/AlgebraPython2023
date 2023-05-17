#prikaz RGB zapisa Google-ovih boja u HEX boje i obrnuto

crvena = 0xea4335 
crvenaR = 0xea
crvenaG = 0x43
crvenaB = 0x35



print(f"Zapis boja u RGB: {int(crvenaR)} {int(crvenaG)} {int(crvenaB)}")

#pretvorba iz RGB u HEX

konverzija = int(str(crvenaR)+str(crvenaG)+str(crvenaB))


print(hex(konverzija))
print(int(crvena))
