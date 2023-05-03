# IP calculator (unesi IP, SM, Izračunaj sve ostalo)

# IP adresa uobliku X.X.X.X gdje je X (0-255) "192.168.1.1"
# SM (subnet maska) 255.255.255.0 ili / 24




IPAdress = input("Unesite IP adresu u obliku X.X.X.X gdje je X (0-255): ")
SubnetMask = input("Unesite subnet masku u brojčanom obliku (broj bitova): ")

SMB = int(SubnetMask)


def BinaryBitSum(BitNum):
    SumBit = 0
    for exp in range(7,-1,-1):
        if BitNum >0:
            SumBit += 2**exp
            BitNum -= 1
    print(SumBit)
    return SumBit





IPList = IPAdress.split(".")
print(IPList)

IPListNum = []



for num in range(4):
    IPListNum.append(int(IPList[num]))

print(IPListNum)

# provjera brojeva u listi (0-255)

AOK = True
for oct in IPListNum:
    if oct < 0 and oct > 255:
        AOK = False
        print("Pogrešan unos!")
        break
if AOK:
    print("Sve ispravno!")    

broj1 = 3   #011
broj2 = 5   #101

broj3= broj1 & broj2
print(broj3)

# IP 192.168.0.1  -> 128 64 32 16 8 4 2 1 -> 2^7, 2^6,..., 2^0 -> 2**7,..., 2**0
# IPb 11000000.10101000.00000000.00000001

# SM 255.255.255.0/24 ->
# SMb 11111111.11111111.11111111.00000000

# SM 255.255.254.0/23
# SMb 11111111.11111111.11111110.00000000

broj1 = 192   #11000000
broj2 = 255   #11111111

broj3= broj1 & broj2
print(broj3)


SMList = []
if SMB < 9:
    SMList[0] = BinaryBitSum(SMB)
    SMList[1] = 0
    SMList[2] = 0
    SMList[3] = 0

    pass

elif SMB < 17:
    SMList[0] = 255
    SMList[1] = BinaryBitSum(SMB-8)
    SMList[2] = 0
    SMList[3] = 0
    
    pass

elif SMB < 25:
    SMList[0] = 255
    SMList[1] = 255
    SMList[2] = BinaryBitSum(SMB-16)
    SMList[3] = 0
    pass

else:
    SMList[0] = 255
    SMList[1] = 255
    SMList[2] = 255
    SMList[3] = BinaryBitSum(SMB-24)
    pass
