

file_writer = open("m3/datoteke/ime.txt", "w")
ime = input("Unesite ime i prezime: ")
file_writer.write(ime)
file_writer.close()


file_reader = open("m3/datoteke/ime.txt", "r")
file_data = file_reader.read()
file_reader.close()
print(f"Sadržaj datoteke je \n{file_data}")