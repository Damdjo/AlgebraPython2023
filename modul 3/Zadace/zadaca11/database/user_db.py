import os, sqlite3


# START funkcije

columns_tuple = ("userID", "username", "password", "department", "level")

def make_insert_query(values_tuple:tuple) -> str:    
    insert_query =f"""
        INSERT INTO users {columns_tuple[1:]} 
        VALUES {values_tuple}
        """ 
    return insert_query

def make_update_query(old_values_tuple:tuple, new_values_tuple:tuple) -> str:
    id = old_values_tuple[0]
    uname, pword, dept, level = old_values_tuple[1], old_values_tuple[2], old_values_tuple[3], old_values_tuple[4]
    if new_values_tuple[1] != "":
        uname = new_values_tuple[1]
    if new_values_tuple[2] != "":
        pword = new_values_tuple[2]
    if new_values_tuple[3] != "":
        dept = new_values_tuple[3]
    if new_values_tuple[4] != "":
        level = new_values_tuple[4]
    update_query = f"""
    UPDATE users 
    SET username = '{uname}', password = '{pword}', department = '{dept}', level = {level}
    WHERE userID = {id}
    """ 
    return update_query


#Funkcija koja će izvršiti query iz argumenta
def db_execute (query_to_execute:str, db_path):
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
        cursor.execute(query_to_execute)  
        print("Success")  
        
    finally:
        if connection:
            connection.commit()
            connection.close()


#Funkcija SELECT koja isto tako i ispisuje vrijednosti koje dohvati
def ispis_racuna (type:int, column:str="", value="", db_path:str="user_accounts.db") -> tuple | str | list:
    """
    Funkcija ima 3 tipa rada\n
    Tip 1: unosi se samo broj 1 kao prvi argument te funkcija ispisuje cijelu tablicu users\n
    
    Tip 2 vraća pretraženo kao listu: 1. argument broj 2\n\t
        2. argumentstupac prema kojem pretražujemo
        3. argument vrijednost u tom stupcu
    """
    select_query = "SELECT * FROM users"
    match type:
        case 1:
            pass
        case 2:
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
                cursor.execute("SELECT * FROM users")
                data_cur = cursor.fetchall()
            case 2:
                cursor.execute(select_query)
                data_cur = cursor.fetchall()
                

        
    finally:
        if connection and data_cur and type == 1:            
            connection.close()
            return data_cur
        elif connection and data_cur and type == 2:
            connection.close()
            return data_cur[0]
        else:
            return "User does not exist"
    return ()
        
def check_login(usr_uname, usr_pword, db_path) -> list | str | tuple:
    """
    funkcija koja koristeći 2 tip funkcije "ispis_racuna" provjerava username i password koje je korisnik unjeo te ako postoji takva kombinacija vraća
    listu [username, odjel, level]
    """
    while True:
        os.system("cls")        
        uname = usr_uname
        pword = usr_pword
        if uname == "" or pword == "":
            return "Username/password\n incorrect!", False
        try:
            check = ispis_racuna(2,"username",uname, db_path)
        
        except sqlite3.Error as sql_err:
            return f"Login error: {sql_err}"

        else:
            if check != ():
                db_pword = check[2]
                if pword == db_pword:#slucaj username tocan, password tocan
                    return [usr_uname, check[3], check[4]], True
                else:#slucaj username tocan, password kriv
                    return "Username/password\n incorrect!" , False
            else:#slucaj username kriv
                return "Username/password\n incorrect!", False
            


#END funkcije



#Kreiranje tablice usera


def create_table(db_path:str="user_accounts.db"):
    conn = None #ovo stavim zato što u finally varijabla bude podcrtana crveno
    try:
        create_query ="""
        CREATE TABLE users (
        userID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        department TEXT NOT NULL,
        level INTEGER NOT NULL
        )
        """
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
            conn.commit()        
            conn.close()

#kraj kreiranje tablice




### MAIN ###
def main():
    
#Hardcodiranje admin usera na prvom pokretanju

    os.chdir("modul 3/Zadace/zadaca11/database")
    """db_path = "user_accounts.db"
    create_table(db_path)
    admin_hardcode = ("admin","admin123","IT","5")
    test = make_insert_query(admin_hardcode)    
    db_execute(test, db_path) """

    
    data = ispis_racuna(1)
    for row in data:
        print(row)
        
        
if __name__ == "__main__":
    main()
