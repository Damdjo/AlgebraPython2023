#Radimo program kojim se mozemo logirati kao admin i tada kreirati korisnike
#Svaki korisnik ima usernama, password, f.name, l.name
#pozdrav za svakog korisnika je: Dobro došli, ime prezime
#ovisno o tipu korisnika mijenjati će se meni
#minimalno moramo ponuditi izmjenu passworda +++ i eventualno neku funkciju za demo
#admin ima više ovlasti, dodaj +++, izmjeni, izbriši, onemogući korisnika
#u sličaju pogreške ispisati krivi user/pass +++
#min 6 znakova za password +++


#Treba jos napraviti funkcije za izmjenu,brisanje i blokanje korisnika


accounts = [
{"id": 1, "username":"admin", "password":"admin123", "ime":"ad", "prezime":"min", "prava":"admin", "blocked" : False },
{"id": 2, "username":"test", "password":"test123", "ime":"test_ime", "prezime":"test_prezime", "prava":"korisnik", "blocked" : False },
{"id": 2, "username":"testblocked", "password":"test123", "ime":"test_ime", "prezime":"test_prezime", "prava":"korisnik", "blocked" : True },

]

id_counter = 4

def promjeni_lozinku(logged_in_user:str) -> None:
    global accounts
    if logged_in_user != "admin":
        while True:    
            input_pword = input("Unesite vašu trenutnu lozinku: ")
            
            for dict in accounts:
                for key, item in dict.items():
                    if logged_in_user == dict["username"] and input_pword == dict["password"]:

                        input_password = input(f"Unesite vašu novu lozinku: ")
                        check, failed = password_validate(input_password)
                        match check:
                            case True:
                                dict["password"]= input_password
                                break
                            case False:
                                match failed:
                                    case "len":
                                        print("Lozinka mora sadržavati više od 6 znakova, pokušajte ponovno!")
                                    case "same":
                                        print("Unesene lozinke nisu jedanke, pokušajte ponovno!")
            else:
                print("Unesena lozinka nije ispravna!")
                break
    else:
        while True:    
            
            input_user = input("Unesite username korisnika kojem mijenjate lozinku: ")
            input_pword = input("Unesite trenutnu lozinku korisnika: ")
            
            for dict in accounts:
                for key, item in dict.items():
                    if input_user == dict["username"] and input_pword == dict["password"]:

                        new_password = input(f"Unesite novu lozinku za korisnika: ")
                        check, failed = password_validate(new_password)
                        match check:
                            case True:
                                dict["password"]= new_password
                                break
                            case False:
                                match failed:
                                    case "len":
                                        print("Lozinka mora sadržavati više od 6 znakova, pokušajte ponovno!")
                                    case "same":
                                        print("Unesene lozinke nisu jedanke, pokušajte ponovno!")
            for dict in accounts:
                for key, item in dict.items():
                    if input_user == dict["username"] and new_password != dict["password"]:
                        #print(input_user,input_pword,new_password,dict["password"])
                        print("Unesena lozinka nije ispravna!")
                        break
                    else:
                        
                        break
                        
            break        
                

                    
                              
                


def password_validate(password:str) -> bool:
    
    len_check = len(password)
    
    if len_check < 6:
        fail = "len"
        return False, fail

    password_2 = input("Ponovno unesite lozinku: ")

    if password == password_2:
        fail = "ok"        
        return True, fail
    else:
        fail = "same"
        return False, fail
    


def login() -> str:
    """
    provjerava username, password te ako je u tablici vraća prava, ime i prezime\n

    prava -> korititi će u main programu te će ovisno o tome user biti admin ili korisnik

    """
    input_uname = input("Unesite korisničko ime: ")
    input_pword = input("Unesite lozinku: ")



    for dict in accounts:
        for key, item in dict.items():
            if input_uname == dict["username"] and input_pword == dict["password"] and dict["blocked"] == False:
                logged_in = True
                blocked = False                
                return dict["prava"], dict["ime"], dict["prezime"], logged_in, input_uname, blocked
            if input_uname == dict["username"] and input_pword == dict["password"] and dict["blocked"] == True:
                print("Vaš račun je blokiran, molimo obratite se administratoru!")
                logged_in = False
                blocked = True
                return dict["prava"], dict["ime"], dict["prezime"], logged_in, input_uname, blocked
def ispis_korisnika(user_prava) -> None:
    ispis_stupci = ["id", "username","password","ime", "prezime",]
    if user_prava == "admin":
        print("*"*85)
        for stupac in ispis_stupci:
            match stupac:
                case "id":
                    print(stupac.capitalize(),"\t",end = "")
                case "username":
                    print(stupac.capitalize(),"\t\t",end = "")
                case "password":
                    print(stupac.capitalize(),"\t\t",end = "")
                case "ime":
                    print(stupac.capitalize(),"\t\t",end = "")
                case "prezime":
                    print(stupac.capitalize(),"\t\t",end = "")
        print()
        print("*"*85)

        for dict in accounts:
            for key, value in dict.items():
                if value != "admin" or value != "korisnik":
                    match key:
                        case "id":
                            print(value,"\t",end = "")
                        case "username":
                            if len(value) <= 4:
                                print(value,"\t\t\t",end = "")
                            elif len(value) <= 8:
                                print(value,"\t\t\t",end = "")
                            else:
                                print(value,"\t\t",end = "")

                        case "password":
                            if len(value) <= 4:
                                print(value,"\t\t\t",end = "")
                            elif len(value) <= 8:
                                print(value,"\t\t",end = "")
                            else:
                                print(value,"\t\t",end = "")
                        case "ime":
                            if len(value) <= 6:
                                print(value,"\t\t",end = "")
                            
                            elif len(value) <= 8:
                                print(value,"\t",end = "")
                            else:
                                print(value,"\t",end = "")
                        case "prezime":
                            if len(value) <= 4:
                                print(value,"\t\t\t")
                            elif len(value) <= 8:
                                print(value,"\t\t")
                            else:
                                print(value,"\t")
                       
            


def check_if_input_taken(za_provjeriti:str, kljuc:str) -> bool:
    for dict in accounts:
        for key, item in dict.items():
            if za_provjeriti == dict[kljuc]:                
                return True
    return False


def kreiraj_racun() -> None:
    global id_counter
    print("Odabrali ste opciju za kreiranje računa!\n")
    temp_dict = {}
    temp_dict["id"] = id_counter
    id_counter += 1

    input_list = ["username","password","ime", "prezime",]
    for key in input_list:
        match key:
            case "username":     
                while True:                    
                    input_username = input(f"Unesite {key}: ")
                    taken = check_if_input_taken(input_username,"username")
                    if taken:
                        print("Unesen username je već zauzet, pokušajte ponovno!")
                        continue
                    else:
                        temp_dict["username"]= input_username
                        break

            
            
            case "password":
                while True:                    
                    check = False
                    while not check:
                        input_password = input(f"Unesite {key}: ")
                        check, failed = password_validate(input_password)
                        match check:
                            case True:
                                temp_dict["password"]= input_password
                                break
                            case False:
                                match failed:
                                    case "len":
                                        print("Lozinka mora sadržavati više od 6 znakova, pokušajte ponovno!")
                                    case "same":
                                        print("Unesene lozinke nisu jedanke, pokušajte ponovno!")
                                
                    if check == True:
                        break    
            
            
            case "ime":                
                input_ime = input(f"Unesite {key}: ")
                temp_dict["ime"]= input_ime.capitalize()
            
            
            case "prezime":
                input_prezime = input(f"Unesite {key}: ")
                temp_dict["prezime"]= input_prezime.capitalize()
    temp_dict["prava"] = "korisnik"
    temp_dict["blocked"] = False             
    
    provjera = input("Želite li unesene podatke spremiti? (da/ne): ")
    match provjera.capitalize():
        case "Da":
            accounts.append(temp_dict)
        case "Ne":
            pass
    
    
    
    



def main():
    pass

if __name__ == "__main__":
    main()