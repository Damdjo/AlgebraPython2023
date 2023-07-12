from typing import Optional, Tuple, Union
import database.user_db as db
import customtkinter as ctk  ########### pip install customtkinter ##########

#DOKUMENTACIJA: https://customtkinter.tomschimansky.com/documentation
#GITHUB:        https://github.com/TomSchimansky/CustomTkinter/tree/master

import os
os.chdir("modul 3/Zadace/zadaca11/")

#boja interfacea
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

#init varijable
db_path = "database/user_accounts.db"
logged_in = False
admin_seg_btn_menu = ""
department_list = ["IT","Sales","HR","Exec"]
level_list = ["1", "2", "3", "4", "5"]
#funkcije

#Ulogiranje u program
def sign_in(event):
    global logged_in
    uname = app.sidebar_uname_input.get()
    pword = app.sidebar_pword_input.get()
    credentials, logged_in = db.check_login(uname,pword,db_path)
    app.event_log_text.set(credentials)
    
    print(credentials)# lista: [username, odjel, level]

    # ovo zamijeni sidebar sa drugim ako je login uspješan
    if logged_in:
        app.sidebar_login_frame.grid_remove()
        app.sidebar_user_frame.grid()
        app.center_frame.grid()
    print(db.ispis_racuna(1,db_path=db_path))

    print()
#Odlogiranje iz programa
def sign_out(event):
    #nakon što se pritisne sign out gumb, polja sa unosom se vraćaju na placeholder vrijednosti
    global logged_in, admin_seg_btn_menu
    app.sidebar_uname_input.delete(0,ctk.END)
    app.sidebar_pword_input.delete(0,ctk.END)
    app.event_log_text.set("")
    
    if logged_in:
        logged_in = False
        admin_seg_btn_menu = ""
        app.sidebar_user_frame.grid_remove()
        app.center_frame.grid_remove()
        app.sidebar_login_frame.grid()
        #tab close
        app.center_seg_button_text.set("")
        app.center_admin_show_user.grid_remove()
        app.center_admin_add_user.grid_remove()
        app.center_admin_modify_user.grid_remove()
        app.center_admin_delete_user.grid_remove()

    

def test(event):
    ctk.set_appearance_mode("light")



def show_all_users():
    data = db.ispis_racuna(1,db_path=db_path)
    print(data)
###funkcije za admin segmentirani meni
#funkcija koja se izvrši kada se klikne jedan od gumbiju
def seg_button_change(value):
    global admin_seg_btn_menu
    admin_seg_btn_menu = value
    change_seg_menu(admin_seg_btn_menu)
#mijenja između menija tako da ostale gasi
def change_seg_menu(selected_option):    
    app.focus() 
    match selected_option:
        case "Show user list":
            app.center_admin_show_user.grid() ####Stisnuti gumb
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid_remove()
            tablica_all = user_table(app.show_user_table_frame, data_type=1, fetch=True)
            
        case "Add user":
            clear_add_user()
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid() ####Stisnuti gumb
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid_remove()
        case "Modify user":
            clear_modify_user()
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid() ####Stisnuti gumb
            app.center_admin_delete_user.grid_remove()
        case "Delete user":
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid() ####Stisnuti gumb
        case _:
            pass

#dept drop down meni 
def get_add_user_dept_dropdown(selected_dept):
    return selected_dept

#level drop down meni 
def get_add_user_level_dropdown(selected_level):
    return selected_level

####################
###ADD USER PART
####################
#dodaje unesene podatke u bazu
def add_user_submit():
    check = True
    message = ""
    uname = app.add_uname.get()
    if uname == "":
        message +="Username cannot be empty!"
        check = False
    pword = app.add_pword.get()
    if pword == "":
        message += "*Password cannot be empty!"
        check = False
    dept = app.add_dept.get()
    if dept not in department_list:
        message += "*Department must be selected!"
        check = False
    level = app.add_level.get()
    if level not in level_list:
        message += "*Level must be selected!"
        check = False    

    if check:
        message = db.ispis_racuna(2,"username",uname,db_path=db_path)
        match message:
            case "User does not exist":
                data_tuple = (uname, pword, dept, level)
                ins_query = db.make_insert_query(data_tuple)
                db.db_execute(ins_query, db_path)                
                
            case _:
                app.add_error_log.configure(text = "Username is already taken!")
    else:
        message = message.replace("*","\n")
        app.add_error_log.configure(text = message)

                
    
    
    #ovo sam bindao na login button i samo jednom pokrenuo da se kreira baza sa hardkodiranim admin userom
    """ 
    db.create_table(db_path)
    admin_hardcode = ("admin","admin123","IT","5")
    test = db.make_insert_query(admin_hardcode)    
    db.db_execute(test, db_path)
    """
#briše sve uneseno u add user meni-ju
def clear_add_user():
    app.focus() 
    app.add_uname.delete(0,ctk.END)
    app.add_uname.configure(placeholder_text = "Username:")
    app.add_pword.delete(0,ctk.END)
    app.add_pword.configure(placeholder_text = "Password:")
    app.add_dept.set("Department")
    app.add_level.set("Level")

####################
### MODIFY USER PART
####################
def fetch_modified_user():
    app.modify_error_log.configure(text = "")
    userid = app.modify_userid.get()
    data = db.ispis_racuna(2,"userID", userid, db_path=db_path)
    if data != "User does not exist":
        app.modify_userid.configure(state = ctk.DISABLED) 
        app.modify_uname.configure(state = ctk.NORMAL, placeholder_text = data[1])
        app.modify_pword.configure(state = ctk.NORMAL, placeholder_text = data[2])
        app.modify_dept.set(data[3])
        app.modify_dept.configure(state = ctk.NORMAL)
        app.modify_level.set(data[4])
        app.modify_level.configure(state = ctk.NORMAL)
    else:
        app.modify_error_log.configure(text = "User does not exist")
    
#clear entry fields and set dropdown to default values
def clear_modify_user():
    app.focus()    
    app.modify_userid.configure( state = ctk.NORMAL)
    app.modify_userid.delete(0,ctk.END)
    app.modify_userid.configure(placeholder_text = "UserID:") 
    app.modify_uname.delete(0,ctk.END)
    app.modify_uname.configure(placeholder_text = "Username:")
    app.modify_uname.configure(state = ctk.DISABLED)
    app.modify_pword.delete(0,ctk.END)
    app.modify_pword.configure(placeholder_text = "Password:")
    app.modify_pword.configure(state = ctk.DISABLED)
    app.modify_dept.set("Department")
    app.modify_dept.configure(state = ctk.DISABLED)
    app.modify_level.set("Level")
    app.modify_level.configure(state = ctk.DISABLED)
#mijenja trenutne podatke sa unesenima
def modify_user_submit():
    id = app.modify_userid.get()
    if id == "1":
        app.modify_error_log.configure(text = "Unable to change admin account!") 
        clear_modify_user()  
    else:
        app.modify_error_log.configure(text = "")
        uname = app.modify_uname.get()
        pword = app.modify_pword.get()
        dept = app.modify_dept.get()
        level = app.modify_level.get()
        data = db.ispis_racuna(2,"userID", id, db_path=db_path)
        new_data = (id, uname, pword, dept, level)
        query = db.make_update_query(data, new_data) # type: ignore
        db.db_execute(query,db_path=db_path)

####################
### DELETE USER PART
####################
#fetch button, dobavlja usera čiji je id unesen
def fetch_selected_user():
    app.delete_error_log.configure(text = "")
    userid = app.delete_userid.get()
    data = db.ispis_racuna(2,"userID", userid, db_path=db_path)
    if data != "User does not exist":
        user_table(app.delete_user_info_frame, data_type=2, stupac="userID",vrijednost=data[0])
        print(app.delete_user_info_frame.winfo_height())
    else:
        app.delete_user_info_frame.grid_remove()
        app.delete_error_log.configure(text = "User does not exist")
#clear button
def clear_delete_user():
    app.focus()
    app.delete_userid.delete(0,ctk.END)
    app.delete_error_log.configure(text="")
    app.delete_userid_title.grid()
    app.delete_userid.grid()
#delete button
def delete_user():
    userid = app.delete_userid.get()
    if userid == "1":
        app.delete_error_log.configure(text="Cannot delete admin user!")
    else:
        delete_query = f"DELETE FROM users WHERE userID = '{userid}'"
        db.db_execute(delete_query,db_path=db_path)

def get_table_data(type:int, stupac:str="", vrijednost:str="") -> list:
    match type:
        case 1:
            data = db.ispis_racuna(1,db_path=db_path)
            return data # type: ignore
        case 2:
            data = db.ispis_racuna(2,stupac,vrijednost,db_path=db_path)
            return data # type: ignore
        case _:
            return [""]
        
        
    

#klase

class user_table:        
    def __init__(self, app, data_type, stupac = "", vrijednost = "", fetch = False):
        self.data_type = data_type
        data = get_table_data(self.data_type)
        if fetch:
            data = get_table_data(self.data_type)
            print("fetched")
        
        total_rows, total_columns = 1,1
               
        match self.data_type:
            case 1:
                total_rows = len(data)
                total_columns = len(data[0])
            case 2:
                data = [get_table_data(self.data_type, stupac, vrijednost)]
                print(data)
                total_rows = 1
                total_columns = len(data[0])
        
        titles = False
        for column in range(total_columns):
            match column:
                case 0:
                    pass
                case 1:
                    self.entry = ctk.CTkLabel(app, text = "Username", width=160)
                    self.entry.grid(row = 0, column = column, padx = 2, pady = 1)
                case 2:
                    self.entry = ctk.CTkLabel(app, text = "Password", width=160,)
                    self.entry.grid(row = 0, column = column, padx = 2, pady = 1)
                case 3:
                    self.entry = ctk.CTkLabel(app, text = "Department", width=120)
                    self.entry.grid(row = 0, column = column, padx = 2, pady = 1)
                case 4:
                    self.entry = ctk.CTkLabel(app, text = "Level", width=60)
                    self.entry.grid(row = 0, column = column, padx = 2, pady = 1)

        for row in range(total_rows):
            for column in range(total_columns):
                match column:
                    case 0:
                        match self.data_type:
                            case 1:
                                self.entry = ctk.CTkEntry(app, width=60)
                                self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                                self.entry.insert(ctk.END, data[row][column])
                            case 2:
                                pass
                    case 1:
                        self.entry = ctk.CTkEntry(app, width=160)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])
                    case 2:
                        self.entry = ctk.CTkEntry(app, width=160,)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])
                    case 3:
                        self.entry = ctk.CTkEntry(app, width=120)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])
                    case 4:
                        self.entry = ctk.CTkEntry(app, width=60)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])

class App(ctk.CTk):
    def __init__(self):
        super().__init__()       

        # prozor
        self.title("Placeholder naziv")
        self.geometry(f"{1100}x{500}")

        # definiranje grida
        self.grid_columnconfigure((1,2,3), weight= 0) # type: ignore
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1,2,3,4), weight= 1) # type: ignore
        
#+++#####sidebar 1 gdje je login + profil info
        self.sidebar_login_frame = ctk.CTkFrame(self, width=175, corner_radius=0)
        self.sidebar_login_frame.grid(row = 0, column = 0, rowspan = 5, sticky="nsew")
        self.sidebar_login_frame.grid_rowconfigure(6, weight=1)    
    
    
        #login title
        self.sidebar_top_label = ctk.CTkLabel(self.sidebar_login_frame, text="LOGIN".center(10), font = ctk.CTkFont(size = 20, weight="bold"))
        self.sidebar_top_label.grid(row = 0, column = 0, padx = 30, pady = (50, 20))
        #username
        self.sidebar_uname_input = ctk.CTkEntry(self.sidebar_login_frame, width= 150, placeholder_text="Username:")
        self.sidebar_uname_input.grid(row = 1, column = 0, padx = 5, pady = (50, 10))        
        self.sidebar_uname_input.bind("<Return>", sign_in)
        #password
        self.sidebar_pword_input = ctk.CTkEntry(self.sidebar_login_frame, width= 150, placeholder_text="Password:")
        self.sidebar_pword_input.grid(row = 2, column = 0, padx = 5, pady = (5, 20))        
        self.sidebar_pword_input.bind("<Return>", sign_in)
        #submit button
        self.sidebar_submit_btn = ctk.CTkButton(self.sidebar_login_frame, width = 75, text="Sign in")
        self.sidebar_submit_btn.grid(row = 3, column = 0, padx = 15, pady = (10,0))
        self.sidebar_submit_btn.bind("<ButtonRelease-1>", sign_in)
        #event log
        self.event_log_text = ctk.StringVar()        
        self.event_log_text.set("")
        self.sidebar_event_box = ctk.CTkLabel(self.sidebar_login_frame, textvariable = self.event_log_text, width= 150, height= 250)
        self.sidebar_event_box.grid(row = 4, column = 0,  padx = 15)
        
#+++#####sidebar 2 sa podatcima ( u pocetku sakriven)
        self.sidebar_user_frame = ctk.CTkFrame(self, width=175, corner_radius=0)
        self.sidebar_user_frame.grid(row = 0, column = 0, rowspan = 5, sticky="nsew")
        self.sidebar_user_frame.grid_rowconfigure(6, weight=1)
        self.sidebar_user_frame.grid_remove()
        #Title label
        self.sidebar_top_label = ctk.CTkLabel(self.sidebar_user_frame, text="WELCOME".center(10), font = ctk.CTkFont(size = 20, weight="bold"))
        self.sidebar_top_label.grid(row = 0, column = 0, padx = 30, pady = (50, 20))
        #Sign out button
        self.sidebar_submit_btn = ctk.CTkButton(self.sidebar_user_frame, width = 75, text="Sign out")
        self.sidebar_submit_btn.grid(row = 4, column = 0, padx = 15, pady = (10,0))
        self.sidebar_submit_btn.bind("<ButtonRelease-1>", sign_out)
        #Sakrivanje framea u početku programa, dok se korisnik ne ulogira
        self.sidebar_user_frame.grid_remove()
    #####END SIDEBAR

    #################
    #####CENTER START
    #################
    
        self.center_frame = ctk.CTkFrame(self, width=600, corner_radius=5, fg_color="transparent")
        self.center_frame.grid(row = 0, column = 1, rowspan = 5, columnspan = 2, padx = 20, pady = 5, sticky = "ns")
        self.center_frame.grid_rowconfigure(0, weight = 0)
        self.center_frame.grid_rowconfigure((1,2,3,4), weight = 1) # type: ignore
        #Center title
        self.center_title_text = ctk.StringVar()
        self.center_title_text.set("PLACEHOLDER")
        self.center_title = ctk.CTkLabel(self.center_frame, textvariable = self.center_title_text, font=("", 28) ,width=600, height=75, corner_radius=10, fg_color=("gray86", "gray17"))
        self.center_title.grid(row = 0, column = 1, columnspan = 2, padx = 20, pady = (5, 0), sticky = "n")
      ###Center frame #POTENCIJALNO SAMO ZA ADMINA, NOVI ZA USERE  
        self.center_switch_frame = ctk.CTkFrame(self.center_frame, width=600, corner_radius=5, fg_color="transparent")
        self.center_switch_frame.grid(row = 1, column = 1, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "ns")
        self.center_switch_frame.grid_rowconfigure(0, weight=0)
        self.center_switch_frame.grid_rowconfigure((1,2,3,4), weight=1) # type: ignore

        ##################
#+++++++#Center tab button
        ##################

        self.center_seg_button_text = ctk.StringVar(value = "".center(20))
        self.center_seg_button = ctk.CTkSegmentedButton(self.center_switch_frame,width=600,command=seg_button_change,  variable=self.center_seg_button_text) #
        self.center_seg_button.configure(values = ["Show user list","Add user","Modify user","Delete user"])
        self.center_seg_button.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = (0, 5), sticky = "nsew")
        #Center tab
#+++++++###Empty frame
        self.center_admin_empty = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5, fg_color="transparent")
        self.center_admin_empty.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        ################
#+++++++###Show user tab
        ################ 
        self.center_admin_show_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_show_user.grid(row = 1, column = 0, rowspan = 6, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.center_admin_show_user.grid_rowconfigure(1, weight=1)
        self.admin_show_user = ctk.CTkLabel(self.center_admin_show_user, text= "Show user".center(20), width=560)
        self.admin_show_user.grid(row = 0, column = 0, padx = 20, pady = 5)
        self.show_user_table_frame = ctk.CTkScrollableFrame(self.center_admin_show_user, width=560, corner_radius=5)
        self.show_user_table_frame.grid(row = 1, column = 0, rowspan = 5, columnspan = 2, pady = (5,0), sticky = "nsew")
        #remove/hide show user menu grid
        self.center_admin_show_user.grid_remove() 
        
        ##########
#+++++++###Add tab
        ##########
        self.center_admin_add_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_add_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.center_admin_add_user.grid_columnconfigure((0,1,2,3,4), weight=0) # type: ignore
        self.admin_add_user = ctk.CTkLabel(self.center_admin_add_user, text= "Add user".center(20), width=560)
        self.admin_add_user.grid(row = 0, column = 0,columnspan = 5, padx = 20, pady = (5,50))

        self.add_userid = ctk.CTkLabel(self.center_admin_add_user, width = 40, text="User ID: ")
        self.add_userid.grid(row = 1, column = 0, padx = (15,5), pady = 5)
        self.add_uname = ctk.CTkEntry(self.center_admin_add_user, width = 140, placeholder_text="Username: ")
        self.add_uname.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.add_pword = ctk.CTkEntry(self.center_admin_add_user, width = 140, placeholder_text="Password: ")
        self.add_pword.grid(row = 1, column = 2, padx = 5, pady = 5)
        
        self.add_dept = ctk.CTkOptionMenu(self.center_admin_add_user, width = 120, values=department_list)
        self.add_dept.grid(row = 1, column = 3, padx = 5, pady = 5)

        self.add_level = ctk.CTkOptionMenu(self.center_admin_add_user, width = 75, values = level_list)
        self.add_level.grid(row = 1, column = 4, padx = (5,15), pady = 5)
        #confirm button
        self.add_confirm = ctk.CTkButton(self.center_admin_add_user, width = 75, text = "Confirm", command=add_user_submit)
        self.add_confirm.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 25)
        #clear button
        self.add_clear = ctk.CTkButton(self.center_admin_add_user, width = 75, text = "Clear input",
                                          command=clear_add_user, fg_color= ("gray15", "gray34"), hover_color= ("gray17","gray24"))
        self.add_clear.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady = 25)
        self.add_error_log = ctk.CTkLabel(self.center_admin_add_user, width = 480, text = "")
        self.add_error_log.grid(row = 3, column = 0, columnspan = 5, padx = 5, pady = 5)
        #remove/hide add user menu grid
        self.center_admin_add_user.grid_remove()

        ##################
        ###Modify user tab after id
        ##################  
        self.center_admin_modify_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_modify_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.center_admin_modify_user.grid_rowconfigure(1, weight = 2) # type: ignore
        self.center_admin_modify_user.grid_rowconfigure((0,2,3), weight = 0) # type: ignore
        ###Input part
        self.modify_user_input_label = ctk.CTkLabel(self.center_admin_modify_user, text= "Change data:".center(20), width=560)
        self.modify_user_input_label.grid(row = 0, column = 0, padx = 20, pady = 5)        
        self.modify_user_input_frame = ctk.CTkFrame(self.center_admin_modify_user, corner_radius=5, width=580)
        self.modify_user_input_frame.grid(row = 1, column = 0, columnspan = 2, rowspan = 3, pady = 25, sticky = "nsew")
        self.modify_user_input_frame.grid_columnconfigure((0,1,2,3,4), weight = 0) # type: ignore
        self.modify_userid = ctk.CTkEntry(self.modify_user_input_frame, placeholder_text = "UserID",width=60)
        self.modify_userid.grid(row = 0, column = 0, padx = (10,2))
        self.modify_uname = ctk.CTkEntry(self.modify_user_input_frame, placeholder_text = "Username: ", width=158)
        self.modify_uname.grid(row = 0, column = 1, padx = 2)
        self.modify_uname.configure(state = ctk.DISABLED)
        self.modify_pword = ctk.CTkEntry(self.modify_user_input_frame, placeholder_text = "Password: ", width=158)
        self.modify_pword.grid(row = 0, column = 2, padx = 2)
        self.modify_pword.configure(state = ctk.DISABLED)
        self.modify_dept = ctk.CTkOptionMenu(self.modify_user_input_frame, width = 120, values=department_list)
        self.modify_dept.grid(row = 0, column = 3, padx = 2, pady = 5)
        self.modify_dept.configure(state = ctk.DISABLED)
        self.modify_level = ctk.CTkOptionMenu(self.modify_user_input_frame, width = 75, values = level_list)
        self.modify_level.grid(row = 0, column = 4, padx = 2, pady = 5)
        self.modify_level.configure(state = ctk.DISABLED)
        #fetch button
        self.modify_fetch = ctk.CTkButton(self.modify_user_input_frame, width = 60, text = "Fetch", command=fetch_modified_user)
        self.modify_fetch.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 25, sticky = "w")
        #confirm button
        self.modify_confirm = ctk.CTkButton(self.modify_user_input_frame, width = 75, text = "Confirm", command=modify_user_submit)
        self.modify_confirm.grid(row = 1, column = 2, columnspan = 2, padx = 20, pady = 25, sticky = "e")
        #clear button
        self.modify_clear = ctk.CTkButton(self.modify_user_input_frame, width = 75, text = "Clear input",
                                          command=clear_modify_user, fg_color= ("gray15", "gray34"), hover_color= ("gray17","gray24"))
        self.modify_clear.grid(row = 1, column = 3, columnspan = 2, padx = 2, pady = 25, sticky = "e")
        #error log
        self.modify_error_log_frame = ctk.CTkFrame(self.center_admin_modify_user, corner_radius=5, width=580)
        self.modify_error_log_frame.grid(row = 2, rowspan =2, column = 0, columnspan = 5, pady = (5,0), sticky = "nsew")
        self.modify_error_log = ctk.CTkLabel(self.modify_error_log_frame, width = 580, text = "")
        self.modify_error_log.grid(row = 1,  column = 0, padx = 10, pady = 25, sticky = "esw")
        #remove/hide modify user menu grid
        self.center_admin_modify_user.grid_remove()

        ##################
        ###Delete user tab
        ##################  
        self.center_admin_delete_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_delete_user.grid(row = 1, column = 0, rowspan = 5, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_delete_user = ctk.CTkLabel(self.center_admin_delete_user, text= "Delete user".center(20), width=560)
        self.admin_delete_user.grid(row = 1, column = 0, columnspan = 5, padx = 20, pady = 5)
        ###Input part    
        
        
        
        #info frame 
        self.delete_user_info_frame = ctk.CTkFrame(self.center_admin_delete_user, width=600, corner_radius=5, fg_color="transparent", height=60)
        self.delete_user_info_frame.grid(row = 1, rowspan = 1, column = 0, columnspan = 5, padx = 0, pady = 5, sticky = "nsew") 
        self.delete_user_info_frame.grid_rowconfigure((0,1), weight=0) # type: ignore      
        self.delete_userid_title = ctk.CTkLabel(self.delete_user_info_frame, text = "UserID",width=60)
        self.delete_userid_title.grid(row = 0, column = 0, padx = 2, pady = 1)
        self.delete_userid = ctk.CTkEntry(self.delete_user_info_frame, placeholder_text = "UserID",width=60)
        self.delete_userid.grid(row = 1, column = 0, padx = (10,2), pady = 10, sticky = "w")

        #button frame
        self.delete_buttons_frame = ctk.CTkFrame(self.center_admin_delete_user, width=600, corner_radius=5, fg_color="transparent")
        self.delete_buttons_frame.grid(row = 2, column = 0, columnspan = 5, padx = 0, pady = 5, sticky = "new")
        self.delete_buttons_frame.grid_columnconfigure(4, weight=1)
        #fetch button
        self.delete_fetch_button = ctk.CTkButton(self.delete_buttons_frame, width = 60, text = "Fetch", command=fetch_selected_user)
        self.delete_fetch_button.grid(row = 0, column = 0, padx = 10, pady = 25, sticky = "w")
        #delete button
        self.delete_confirm_button = ctk.CTkButton(self.delete_buttons_frame, width = 75, text = "Delete", command=delete_user)
        self.delete_confirm_button.grid(row = 0, column = 4, padx = (0, 100), pady = 25, sticky = "e")
        #clear button
        self.delete_clear_button = ctk.CTkButton(self.delete_buttons_frame, width = 75, text = "Clear input",
                                          command=clear_delete_user, fg_color= ("gray15", "gray34"), hover_color= ("gray17","gray24"))
        self.delete_clear_button.grid(row = 0, column = 4, padx = (2,10), pady = 25, sticky = "e")
        #error log
        self.delete_error_log = ctk.CTkLabel(self.center_admin_delete_user, width = 580, text = "")
        self.delete_error_log.grid(row = 3,  column = 0, padx = 10, pady = 5, sticky = "s")

        #remove/hide delete user menu grid
        self.center_admin_delete_user.grid_remove()


        #Sakrivanje menija dok se korisnik ne ulogira
        self.center_frame.grid_remove()
        
        


            

        
        
         
        
        
        
       














app = App()
app.mainloop()
