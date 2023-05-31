clanovi = {
    4782: "Mate",
    9720: "Ivana",
    1538: "Jure",
    9348: "Marica"

}

print(clanovi)

for idClana in clanovi.keys():
    print(idClana)

for imeClana in clanovi.values():
    print(imeClana)

for idClana, imeClana in clanovi.items():
    print(f"Clan s brojem iskaznice {idClana} je {imeClana}")

clanovi[9348]= "Mare"
print(clanovi)

clanske = {
    3562:[],
    2654: ["Mate", "Matić", "A1",(1950,2023)]
}

clanske[3562].append("Mirko")

print(clanske[3562])

print(clanske[2654][3][1])

clanske[2654][3][1]=2024