vozni_park = {
    1 : ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45000.00],
    2 : ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47000.00],
    3 : ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78000.00],
    4 : ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97000.00],
    5 : ['Kombi', 'Mercedes', 'ST 001 ZZ', 2013, 12000.00],
    6 : ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35000.00],
    7 : ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9000.00],
    8 : ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9300.00]
} 

headerTop = f"ID\t  Tip\t\tProizvođač\t\tRegistarska\tGodina prve\t\tCijena"
headerBot = f"  \t     \t\t          \t\toznaka     \tregistracije\t\t(EUR)      "
headerUndeline = "_"*105
print(headerTop, "\n", headerBot, "\n", headerUndeline, sep="")
for key, value in vozni_park.items():
    print(f"{key}", end = "\t")
    for item in value:
        print(f"{item}", end="\t\t")
    print()
print()

#vozni_park.clear()

#value1 = vozni_park.pop(1,"No type found")
#value10 = vozni_park.pop(10,"No type found")

headerTop = f"ID\t  Tip\t\tProizvođač\t\tRegistarska\tGodina prve\t\tCijena"
headerBot = f"  \t     \t\t          \t\toznaka     \tregistracije\t\t(EUR)      "
headerUndeline = "_"*105
print(headerTop, "\n", headerBot, "\n", headerUndeline, sep="")
for key, value in vozni_park.items():
    print(f"{key}", end = "\t")
    for item in value:
        print(f"{item}", end="\t\t")
    print()
print()

#print(value1, "\n", value10)

#value7 = vozni_park.popitem()

print()
print()
headerTop = f"ID\t  Tip\t\tProizvođač\tRegistarska\tGodina prve\tCijena"
headerBot = f"  \t     \t\t          \toznaka     \tregistracije\t(EUR)      "
headerUndeline = "_"*80
print(headerTop, "\n", headerBot, "\n", headerUndeline, sep="")
for key, value in vozni_park.items():
    print(f"{key}", end = "\t")
    
    for item in value:
        if len(str(item)) >= 8:
            print(f"{item}", end="\t")
        
        elif len(str(item)) > 5 and len(str(item)) < 8:
            print(f"{item}", end="\t\t")
        
        elif len(str(item)) <= 5:
            print(f"{item}", end="\t\t")        
        
        else:
            print(f"{item}", end="\t\t\t") 

    print()
print()

"""print(value7)
print(value7[0])
print(value7[1])
print(value7[1])"""