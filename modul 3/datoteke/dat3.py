
counter = 1

while True:
    ime = input("Unesite ime kontakta: ")
    prezime = input("Unesite prezime kontakta: ")
    tel_broj = input("Unesite telefonski broj kontakta: ")
    try:
        file_writer = open("m3/datoteke/adresar.txt", "a")
        file_writer.write(f"{counter}; {ime}; {prezime}; {tel_broj}\n")
        counter += 1
        
    except Exception as e:
        print(f"Dogodila se greška {e}")        
    else:
        file_writer.close()
    #finally: 
        #file_writer.close() ovo svijetli crveno iz nekog razloga, ali radi...

    match input("Želite li unjeti novi kontakt (da/ne): ").capitalize():
        case "Ne":
            break
        case _:
            continue