# ADMINISTRACIJA
# Logiranje s korisnickim imenom-lozinkom(admin-admin)
# Uvid u stanje na skladistu
# Uvid u broj izdanih računa
# Uvid u promet (u Eurima)
# Jos ideja???


def koliko_racuna(broj_racuna:int) -> None:

      
    match broj_racuna:
        case 0:
            print("Nije izdan niti jedan račun!")
        case 1:
            print(f"Izdan je ukupno {broj_racuna} račun!")
        case _:
            print(f"Izdano je ukupno {broj_racuna} računa!")


def promet(dict_svih_racuna:dict) -> int:
    total = 0
    for value in dict_svih_racuna.values():
        for dict in value:
            total += dict["ukupno"]
    return total