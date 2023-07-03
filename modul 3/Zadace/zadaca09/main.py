import os, sqlite3
os.chdir("modul 3/Zadace/zadaca09") #mijenjanje direktorija gdje se terminal pokreće

db_path = "accounts.db"
# START funkcije 

#Funkcija koja će izvršiti query iz argumenta
def db_execute (query_to_execute:str):
    connection = None
    try:
        connection = sqlite3.connect("accounts.db")
    
    except sqlite3.IntegrityError as IntErr:
        print(f"Database error: {IntErr}")
        return None
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
    else:
        cursor = connection.cursor()
        cursor.execute(query_to_execute)  
        print("Success")  
        
    finally:
        if connection:
            connection.commit()
            connection.close()

#Funkcija koja sa cursorom executea insert_query u kojem se nalazi argument values_tuple sa vrijednostima (username, password, department, level)
#  te sa kojom unosimo nove korisnike u bazu

def db_insert (values_tuple:tuple):
    columns_tuple = ("userID", "username", "password", "department", "level")
    ### u query-ju su sa sliceom odabrani svi stupci izuzev prvog "userID" zato što se on sam unosi###
    insert_query =f"""
    INSERT INTO users {columns_tuple[1:]} 
    VALUES {values_tuple}
    """
    connection = None
    try:
        connection = sqlite3.connect(db_path)
    
    except sqlite3.IntegrityError as IntErr:
        print(f"Database error: {IntErr}")
        return None
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")

    else:
        cursor = connection.cursor()
        cursor.execute(insert_query)  
        print("Success")  
        
    finally:        
        if connection:
            connection.commit()
            connection.close()


#Funkcija SELECT koja isto tako i ispisuje vrijednosti koje dohvati
def ispis_racuna (type:int, column:str="", value="", select_query:str="SELECT * FROM users") -> tuple:
    """
    Funkcija ima 3 tipa rada\n
    Tip 1: unosi se samo broj 1 kao prvi argument te funkcija ispisuje cijelu tablicu users\n
    Tip 2 ispisuje pretraženo:  1. argument broj 2\n\t
    2. argumentstupac prema kojem pretražujemo
    3. argument vrijednost u tom stupcu
    Tip 3 vraća pretraženo kao listu: 1. argument broj 3\n\t
    2. argumentstupac prema kojem pretražujemo
    3. argument vrijednost u tom stupcu
    """

    match type:
        case 1:
            select_query = "SELECT * FROM users"
        case 2:
            select_query = f"""
            SELECT * FROM users
            WHERE "{column}" = "{value}"
            """
        case 3:
            select_query = f"""
            SELECT * FROM users
            WHERE "{column}" = "{value}"
            """

    connection, data_cur = None, None
    try:
        connection = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
    else:
        cursor = connection.cursor()
        match type:
            case 1:
                cursor.execute(select_query)
            case 2:
                cursor.execute(select_query)
            case 3:
                cursor.execute(select_query)
                data_cur = cursor.fetchall()
                

        if type == 1 or type == 2:                
            data_cur = cursor.fetchall()
            print(f"{'userID'.center(6)} | {'Username'.center(12)} | {'Password'.center(25)} | {'Department'.center(10)} | {'Level'.center(4)}")
            print("-"*70)
            for row in data_cur:
                print(f"{str(row[0])[:6].center(6)} | {str(row[1])[:12].center(12)} | {str(row[2])[:25].center(25)} | {str(row[3])[:10].center(10)} | {str(row[4])[:4].center(4)}")
        
    finally:
        if connection and data_cur and type == 2:            
            connection.close()
            return data_cur[0]
        elif connection and data_cur and type == 3:
            connection.close()
            return data_cur[0]
    return ()
        
def check_login() -> list:
    """
    funkcija koja koristeći 3 tip funkcije "ispis_racuna" provjerava username i password koje je korisnik unjeo te ako postoji takva kombinacija vraća
    listu [username, odjel, level]
    """
    while True:
        os.system("cls")        
        usr_uname = input("Username: ")
        usr_pword = input("Password: ")
        if usr_uname == "" or usr_pword == "":
            print("Username/password incorrect!")
            enter_to_continue()
            continue
        try:
            check = ispis_racuna(3,"username",usr_uname)
        
        except sqlite3.Error as sql_err:
            print(f"Login error: {sql_err}")

        else:
            if check != ():
                db_pword = check[2]
                if usr_pword == db_pword:
                    return [usr_uname, check[3], check[4]]                
                else:
                    print("Username/password incorrect!")
                    enter_to_continue()
            
def enter_to_continue():
    """funckija pauzira kod dok se ne stisne enter"""
    input("Press enter to continue...")

def iface(user_data:list):
    """Funckija za ispis sučelja"""
    #popis opcija menija po odjelima
    odjel_admin = ["Dodaj novog usera", "Uredi postojećeg usera", "Izbriši usera", "Ispis popisa usera"]
    odjel_nabava = ["PLACEHOLDER_NABAVA_1", "PLACEHOLDER_NABAVA_2", "PLACEHOLDER_NABAVA_3", "PLACEHOLDER_NABAVA_4"]
    odjel_HR = ["PLACEHOLDER_HR_1", "PLACEHOLDER_HR_2", "PLACEHOLDER_HR_3", "PLACEHOLDER_HR_4"]

    

    
    print("*"*60)
    print(f"User: {str(user_data[0]).capitalize()}".center(25)," "*17, f"Odjel: {user_data[1]}".center(18))
    print("\n")
    match str(user_data[1]).upper():
        case "IT":
            options_list = odjel_admin
        case "NABAVA":
            options_list = odjel_nabava
        case "HR":
            options_list = odjel_HR
    print("  MENI:")
    for broj, opcija in enumerate(options_list):
        print(f"\t{broj+1}. {str(opcija).capitalize()}")
    print(f"\n\t0. Izlaz")

def choices(user_data:list):
    status = -1    
    while status != 0:
        os.system("cls")        
        iface(user_data)
        try:
            status = int(input("\nUnesite odabir: "))

        except ValueError as e:
            print(f"Unos mora biti broj!")
            enter_to_continue()
            continue
        else:
            odjel = user_data[1]
        
        match odjel:
            case "IT": # Za sada je napravljen samo ovaj meni, ostali su placeholderi
                match status:
                    case 0:
                        print("Izlaz iz programa")
                        break
                    case 1: # Slucaj gdje se dodaje novi korisnik, traži se unos svih podataka te ima double check da je sve dobro uneseno
                        os.system("cls")
                        print("Unos novog usera\n")
                        username = input("\tUnesite username: ")
                        password = input("\tUnesite password: ")
                        odjel = input("\tUnesite odjel: ")
                        level = input("\tUnesite level: ")
                        to_insert = (f"{username}",f"{password}",f"{odjel}",f"{level}")
                        print(f"Uneseni podatci su:\nUser: {username} | Pass: {password} | Odjel: {odjel} | Level: {level}")
                        input_check = input("\nJeste li sigurni da želite potvrditi navedeno? (DA/NE)\n\n\tOdabir: ")
                        match input_check.upper():
                            case "DA":
                                db_insert(to_insert)
                            case _:
                                pass
                        
                    case 2:
                        os.system("cls")
                        print("Uređivanje postojećeg usera\n")

                        try:
                            edit_user = int(input("Unesite id usera kojeg želite urediti: "))
                        except ValueError as val:
                            print(f"Krivi unos: {val}")
                            enter_to_continue()
                            continue


                        exists_check = ispis_racuna(3,"userID",edit_user) #3. Tip funkcije vraća () ako zapis ne postoji 
                        if exists_check == ():                            # to možemo ovdje iskoristiti da se ne ispiše tablica stupaca bez ikakvog sadržaja
                            print("Navedeni user ne postoji!")
                            enter_to_continue()
                            continue
                        unchanged = ispis_racuna(2,"userID",edit_user)[1:] #spremamo original, slice tako da ne uzimamo userID
                        print("Polja koja ne želite mijenjati ostavit prazna!")
                        enter_to_continue()
                        is_changed = True #defaultno postavljamo kao True te se kod svakog unosa provjerava da nije prazan
                        username = input("\tUnesite username: ")
                        if username =="":
                            username = unchanged[0]
                        else:
                            is_changed = False # 
                        password = input("\tUnesite password: ")
                        if password =="":
                            password = unchanged[1]
                        else:
                            is_changed = False
                        odjel = input("\tUnesite odjel: ")
                        if odjel =="":
                            odjel = unchanged[2]
                        else:
                            is_changed = False
                        level = input("\tUnesite level: ")
                        if level =="":
                            level = unchanged[3]
                        else:
                            is_changed = False

                        if is_changed: # ako su svi unosi prazni tj. ništa novo nije uneseno onda se izvršava sljedeće
                            print("Podatci nisu izmjenjeni (Ništa novo nije uneseno)!")                        
                            enter_to_continue()
                            continue

                        #ukoliko je neki od unosa promjenjen onda se nastavlja sa izvršavanjem
                        new = (f"{username}",f"{password}",f"{odjel}",f"{level}")
                        update_query = f"""
                        UPDATE users 
                        SET username = '{username}', password = '{password}', department = '{odjel}', level = {level}
                        WHERE userID = {edit_user}
                        """

                        #ispis sa starim i novim podatcima
                        os.system("cls")
                        print(f"{''.center(6)} | {'Username'.center(12)} | {'Password'.center(25)} | {'Department'.center(10)} | {'Level'.center(4)}")
                        
                        print(f"STARO  | {str(unchanged[0])[:12].center(12)} | {str(unchanged[1])[:25].center(25)} | {str(unchanged[2])[:10].center(10)} | {str(unchanged[3])[:4].center(4)}")
                        
                        print(f" NOVO  | {str(new[0])[:12].center(12)} | {str(new[1])[:25].center(25)} | {str(new[2])[:10].center(10)} | {str(new[3])[:4].center(4)}")
                        double_check = input("\nJeste li sigurni da želite potvrditi navedeno? (DA/NE)\n\n\tOdabir: ")
                        match double_check.upper():
                            case "DA":                                
                                db_execute(update_query)
                            case _:
                                pass
                        

                    case 3:                        
                        os.system("cls")
                        print("Brisanje usera\n")
                        
                        del_user = int(input("Unesite id usera kojeg želite izbrisati: "))
                        delete_query = f"DELETE FROM users WHERE userID = '{del_user}'"
                        exists_check = ispis_racuna(3,"userID",del_user) #3. Tip funkcije vraća () ako zapis ne postoji 
                        if exists_check == ():                           # to možemo ovdje iskoristiti da se ne ispiše tablica stupaca bez ikakvog sadržaja
                            print("Navedeni user ne postoji!")
                            enter_to_continue()
                            continue
                        os.system("cls")
                        #Budući da je kod nastavio, možemo ispisati tablicu koja će sadržavati usera 
                        ispis_racuna(2,"userID",del_user)
                        double_check = input("\nJeste li sigurni da želite izbrisati usera? (DA/NE)\n\n\tOdabir: ")
                        match double_check.upper():
                            case "DA":                                
                                db_execute(delete_query)
                            case _:
                                pass
                    case 4:
                        os.system("cls")
                        print("Popis usera\n")
                        ispis_racuna(1)
                        enter_to_continue()
                    
                    #case 5:
                        #db_execute("SELECT * FROM accounts")


#END funkcije



#Kreiranje tablice usera

create_query ="""
CREATE TABLE users (
userID INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
department TEXT NOT NULL,
level INTEGER NOT NULL
)
"""

conn = None #ovo stavim zato što u finally varijabla bude podcrtana crveno
try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(create_query)
    cursor.close()
    

except sqlite3.Error as db_err:
    if str(db_err) == "table users already exists": #Ne ispisuje ništa u slučaju da tablica već postoji, a ako postoji neki drugi error onda njega ispisuje
        pass
    else:
        print(f"Create error: {db_err}")

finally:
    if conn:        
        conn.close()

#kraj kreiranje tablice




### MAIN ###
def main():
    
#Hardcodiranje admin usera na prvom pokretanju
    #to_insert = ("admin","admin123","IT","5")
    #db_insert(to_insert)
    
    usr_data = check_login()
    choices(usr_data)
        
        
main()
