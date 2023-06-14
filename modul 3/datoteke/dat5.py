try:
    with open("m3/datoteke/adresar.txt", "r") as file_reader:
        file_data = file_reader.read()
        print(file_data)
except Exception as e:
    print(f"Greška: {e}")

print()
try:
    with open("m3/datoteke/adresar.txt", "r") as file_reader:
        for red in file_reader:
            dijelovi_retka = red.split(";")
            print(f"ID: {dijelovi_retka[0]}, Ime: {dijelovi_retka[1]}, Prezime: {dijelovi_retka[2]}, Mob: {dijelovi_retka[3]}")
except Exception as e:
    print(f"Greška: {e}")