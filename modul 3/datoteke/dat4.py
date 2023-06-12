
counter = 1

while True:
    ime = input("Unesite ime kontakta: ")
    prezime = input("Unesite prezime kontakta: ")
    tel_broj = input("Unesite telefonski broj kontakta: ")
    try:
        with open("m3/datoteke/adresar.txt", "a") as file_writer:
            file_writer.write(f"{counter}; {ime}; {prezime}; {tel_broj}\n")
            counter += 1        
    except Exception as e:
        print(f"Dogodila se greška {e}")        
    

    match input("Želite li unjeti novi kontakt (da/ne): ").capitalize():
        case "Ne":
            break
        case _:
            continue