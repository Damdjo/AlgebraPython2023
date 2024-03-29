import os, sqlite3


db_path = "database/user_accounts.db"

# START funkcije

columns_tuple = ("userID","name", "surname", "PIN", "is_admin", "active", "has_rfid")

def make_insert_query(values_tuple:tuple) -> str:    
    insert_query =f"""
        INSERT INTO users {columns_tuple[1:]} 
        VALUES {values_tuple}
        """ 
    return insert_query

def make_update_query(old_values_tuple:tuple, new_values_tuple:tuple) -> str:
    id = old_values_tuple[0]
    name,surname, pin, admin,active,rfid = old_values_tuple[1], old_values_tuple[2], old_values_tuple[3], old_values_tuple[4], old_values_tuple[5], old_values_tuple[6]
    if new_values_tuple[1] != "":
        name = new_values_tuple[1]
    if new_values_tuple[2] != "":
        surname = new_values_tuple[2]
    if new_values_tuple[3] != "":
        pin = new_values_tuple[3]
    if new_values_tuple[4] != "":
        admin = new_values_tuple[4]
    if new_values_tuple[5] != "":
        active = new_values_tuple[5]
    if new_values_tuple[6] != "":
        rfid = new_values_tuple[6]
    update_query = f"""
    UPDATE users 
    SET name = '{name}',surname = '{surname}', PIN = '{pin}', is_admin = '{admin}', active = {active}, has_RFID = {rfid}
    WHERE userID = {id}
    """ 
    return update_query


#Funkcija koja će izvršiti query iz argumenta
def db_execute (query_to_execute:str, db_path) -> None | str:
    connection = None
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute(query_to_execute)
    
    except sqlite3.IntegrityError as IntErr:
        return str(IntErr)
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    
        
    else:
          
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
        name TEXT NOT NULL UNIQUE,
        surname TEXT NOT NULL,
        PIN INTEGER NOT NULL UNIQUE,
        is_admin INTEGER NOT NULL,
        active INTEGER NOT NULL,
        has_rfid INTEGER NOT NULL
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

    os.chdir("modul 3/smartkey_damjan_jaksic_V2")
    db_path = "database/user_accounts.db"

    
    """ create_table(db_path)
    admin_hardcode = ("admin","adminovic",123456,1,1,1)
    test = make_insert_query(admin_hardcode)
    print(test)
    db_execute(test,db_path=db_path)
    sel_all = "SELECT * FROM users"    
    db_execute(sel_all, db_path) """

   
    
    
    """ #QUERY ZA TEST USERE
    test1 = ("test1","testic1",123458,1,1,1)
    test2 = ("test2","testic2",234567,0,1,1)
    test3 = ("test3","testic3",345678,1,0,1)
    test4 = ("test4","testic4",456789,0,0,1)
    test5 = ("test5","testic5",567890,1,1,0)
    test_list = (test1,test2,test3,test4,test5)
    for test in test_list:
        query = make_insert_query(test)
        db_execute(query,db_path=db_path) """


    
    data = ispis_racuna(1, db_path=db_path)
    for row in data:
        print(row)
        
        
if __name__ == "__main__":
    main()
