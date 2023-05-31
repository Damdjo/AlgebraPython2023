# SKLADISTE
# PRODAJA
# ADMINISTRACIJA
# KUPAC

admin =     {"id":"0001", "username":"admin",       "password": "admin123",     "odjel":"admin"}
skladiste = {"id":"0010", "username":"skladiste",   "password": "skladiste123", "odjel":"skladiste"}
prodaja =   {"id":"0020", "username":"prodaja",     "password": "prodaja123",   "odjel":"prodaja"}
kupac =     {"id":"0100", "username":"kupac",       "password": "kupac123",     "odjel":"kupac"}

radnici = [admin, skladiste, prodaja]

kupci = [kupac]

def main():
    user = login()
    print(user)

def login() -> str:

    """provjerava usernama i password te vraća odgovarajući odjel i bool logged in koji označuje da je netko trenuto ulogiran"""
    
    while True:              
    
        usr_input_username = input("Username: ")
        usr_input_password = input("Password: ")      

        for user in radnici:
            if user["username"] == usr_input_username and user["password"] == usr_input_password:
                odjel = user["odjel"]
                logged_in = True
                return odjel, logged_in           

        for user in kupci:
            if user["username"] == usr_input_username and user["password"] == usr_input_password:
                odjel = user["odjel"]
                logged_in = True
                return odjel, logged_in       
        print("Korisničko ime ili lozinka nisu ispravni")
    
def logout() -> bool:
    logged_in = False
    return logged_in

        
    
           

if __name__ == "__main__":
    main()