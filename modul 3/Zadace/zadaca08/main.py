#pronaći naredbu kojom ćemo zapisati nešto u bazu podataka
#isto tako naredbu za isčitavanje zapisa iz tablice

# napraviti u 2 zasebne datoteke ( jedna za zapisivanje, druga za čitanje podataka)



import sqlite3, os, json
os.chdir("m3/zadace/zadaca08")


from modules_db import scrape_ADM
from modules_db import cijena_znakici


preskoceni = []




create_query = """
CREATE TABLE komponente (
sifra_artikla STRING PRIMARY KEY,
naziv TEXT NOT NULL,
dostupnost TEXT NOT NULL,
cijena_EUR FLOAT NOT NULL ,
cijena_Kn FLOAT NOT NULL 
);
"""

select_query = """
SELECT * FROM komponente;
"""

drop_query = """
DROP TABLE komponente;
"""

columns_db = ("sifra_artikla", "naziv", "dostupnost", "cijena_EUR", "cijena_Kn")
def db_insert (table_name, columns_tuple:tuple, values_tuple:tuple, commit_check:bool=True):
    failed = False
    insert_query = f"""
    INSERT INTO {table_name} {columns_tuple}
    VALUES {values_tuple};
    """
    connection = None
    try:
        connection = sqlite3.connect("ADM.db")
    
    except sqlite3.IntegrityError as IntErr:
        print(f"Database error: {IntErr}")
        return None

    
        
    
    except sqlite3.Error as e:
        print(f"Database error: {e}") 
    
        
    else:
        cursor = connection.cursor()
        try:
            cursor.execute(insert_query)
        except sqlite3.IntegrityError as sq3e:
            print(f"Database error: {sq3e}")
            failed = True
            input("Press Enter to continue...")
        except sqlite3.OperationalError as OpErr:
            print(f"Database error: {OpErr}")
        else:            
            pass
          
        print("Success")  
        
    finally:
        
        if connection:
            if not failed:
                while True:
                    if commit_check:
                        try:
                            
                            yes_no = input("Commit changes?\n\t1.Yes\n\t2.No\n\n Input: ")
                            int(yes_no)
                            
                        except ValueError as e:
                            print(e)
                        
                        else:
                            match int(yes_no):
                                case 1:
                                    """
                                    try:
                                        connection.commit()
                                    except sqlite3.IntegrityError as sq3e:
                                        print(f"Database error: {sq3e}")
                                        input("Press Enter to continue...")
                                    else:
                                        connection.commit()
                                        """
                                    connection.commit()
                                    break
                                case 2:
                                    break
                    else:
                        connection.commit()
                        break
            
            connection.close()










def db_execute (insert_query:str):
    connection = None
    try:
        connection = sqlite3.connect("ADM.db")
    
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


def db_select (kategorija:str="", select_query:str="SELECT * FROM komponente;"):
    connection = None
    kategorija = kategorija.replace("-","_")
    kategorija_meni = kategorija.replace("_"," ")
    if kategorija != "":
        select_query = f"""
            SELECT * FROM {kategorija};
            """
    try:
        connection = sqlite3.connect("ADM.db")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
    else:
        cursor = connection.cursor()
        cursor.execute(select_query)
        
        data_cur = cursor.fetchall()
        
        os.system("cls")
        print(f"Baza {kategorija_meni}".upper())
        print(f"{'Šifra artikla'.center(13)} | {'Naziv'.center(60)} | {'Dostupnost'.center(22)} | {'Cijena €'.center(20)} | {'Cijena KN'.center(24)}")
        print("-"*145)
        for row in data_cur:
            print(f"{str(row[0])[:13].center(13)} | {str(row[1])[:60].center(60)} | {str(row[2])[:22].center(22)} | {str(row[3])[:20].center(20)} | {str(row[4])[:14].center(24)}")

        
    finally:
        if connection:
            connection.close()




def data_from_json(kategorija:str, json_path:str, check:bool=True):
    data = {}
    try:
        with open(json_path,"r", encoding="utf-8") as fr:
            names = fr.read()
            data = json.loads(names)
            
            fr.close()
    except Exception as e:
        print(f"Error {e}")
    #print(data)
    if data != {}:
        for item in data.values():
            print(item)
            item_tuple = (item["sifra_artikla"],item["naziv"], item["dostupnost"], item["cijena_€"], item["cijena_Kn"])
            db_insert(kategorija, columns_db, item_tuple, check)

           
def get_data_dict():
    try:
        with open("site_data/kategorije.json", "r", encoding="utf-8") as fr:
            data = fr.read()
            data = json.loads(data)
            fr.close()
    except Exception as e:
            print(e)
    else:        
        return data

def iface(lista:list, izlaz:bool=False, kategorija:str="") -> None:
    """
    lista -> lista sa popisom opcija koja se printaju jedan ispod druge sa rednim brojevima\n    
    ***od opcija izlaz i login_logout samo jedna može biti aktivna***\n
    ***izlaz -> ako je True onda se na kraju ispiše opcija 0. Izlaz\n
    ***login_logout -> ako je True onda se na kraju ispiše opcija 0. Logout
                    -> možemo proslijediti i argument odjel koji će se ispisazi uz MENI
    """   
    
    
    meni =  kategorija
    
    
    
    
    meni.upper()
    duzina = int(50/2-len(meni)/2)

    print('*'*50)
    print(' '*duzina,meni,)
    print('*'*50)
    for broj, stavka in enumerate(lista):
        print(f'\t{broj+1}. {stavka}')
    if izlaz :
        print('\n\t0. Izlaz')    
def enter_to_continue():
    input("Press enter to continue...")

def main():
    data = ""
###########################################################################
###########################################################################
    pull_data, create_table, transfer_data = True, True, True       ##### Ponovno kreiranje baze i ucitavanje podataka sa neta
###########################################################################
###########################################################################
    if pull_data:
        scrape_ADM.get_data()    
        try:
            with open("site_data/kategorije.json", "r", encoding="utf-8") as fr:
                data = fr.read()
                data = json.loads(data)                
                for value in data.values():
                    cijena_znakici.sterilize(f"{value}_data","site_data/podatci/")
                    print(value," sterilized!")
                fr.close()
        except Exception as e:
            print(e)
    kategorije = {}
    kategorije = get_data_dict()    
    
    if create_table:
        for kategorija in kategorije.values():
            kategorija = kategorija.replace("-","_")
            create_query = f"""
                CREATE TABLE {kategorija} (
                sifra_artikla STRING PRIMARY KEY,
                naziv TEXT NOT NULL,
                dostupnost TEXT NOT NULL,
                cijena_EUR FLOAT NOT NULL ,
                cijena_Kn FLOAT NOT NULL 
                );
                """
            db_execute(create_query)

    lista_kategorija = []
    for value in kategorije.values():
        value = value.replace("-","_")
        lista_kategorija.append(value)

    if transfer_data:
        for kategorija in lista_kategorija:
            data_from_json(kategorija,f"site_data/podatci/{kategorija}_data.json", False)
    
    
    status = 0
    while status != -1:
        iface(lista_kategorija,True, "MAIN")
        status = input("Unesite odabir: ")
        try: 
            status = int(status)
        except ValueError: 
            print("Unos mora biti broj!")
            enter_to_continue()

        #db_insert("laptopi", columns_db, ("123","naziv laptopa","nono","123","456"))
        
        match status:
            case 0:
                print("Izlaz")
                break
            case 1:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 2:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 3:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 4:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 5:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 6:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 7:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 8:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 9:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 10:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 11:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 12:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 13:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            case 14:
                db_select(lista_kategorija[status-1])
                enter_to_continue()
            

    #db_execute(drop_query)
    #db_execute(create_query)
    
    
    #db_insert(columns_db[1:],("adam","adam@email.com"))
    #db_select(select_query)
    #db_select("","SELECT * FROM racunala")
    
    #db_select("","SELECT * FROM komponente WHERE naziv LIKE '%DDR%' AND naziv LIKE '%MHz%'")
    

main()
