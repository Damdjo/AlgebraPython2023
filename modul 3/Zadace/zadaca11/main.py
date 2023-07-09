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
    #data = db.ispis_racuna(1,db_path=db_path)
    data = db.ispis_racuna(1,db_path=db_path)
    print(data)
    #print(data)
###funkcije za admin segmentirani meni

#mijenja između menija tako da ostale gasi
def change_seg_menu(selected_option):    
    app.focus() 
    match selected_option:
        case "Show user list":
            app.center_admin_show_user.grid() ####Stisnuti gumb
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid_remove()
            show_all_users()
        case "Add user":
            clear_add_user()
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid() ####Stisnuti gumb
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid_remove()
        case "Modify user":
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
                print(ins_query)
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
#funkcija koja se izvrši kada se klikne jedan od gumbiju
def seg_button_change(value):
    global admin_seg_btn_menu
    admin_seg_btn_menu = value
    print(admin_seg_btn_menu)
    change_seg_menu(admin_seg_btn_menu)

    



def db_action(event):
    #ovo sam bindao na login button i samo jednom pokrenuo da se kreira baza sa hardkodiranim admin userom
    """ 
    db.create_table(db_path)
    admin_hardcode = ("admin","admin123","IT","5")
    test = db.make_insert_query(admin_hardcode)    
    db.db_execute(test, db_path)
    """
    pass

#klase
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
        
    #####sidebar 1 gdje je login + profil info
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
        
    #####sidebar 2 sa podatcima ( u pocetku sakriven)
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


    #####CENTER START
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
        #Center tab button
        ##################
        self.center_seg_button_text = ctk.StringVar(value = "")
        self.center_seg_button = ctk.CTkSegmentedButton(self.center_switch_frame,width=600, command=seg_button_change, variable=self.center_seg_button_text)
        self.center_seg_button.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = (0, 5), sticky = "nsew")
        self.center_seg_button.configure(values = ["Show user list","Add user","Modify user","Delete user"])
        #Center tab
        ###Show user tab 
        self.center_admin_show_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_show_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_show_user = ctk.CTkLabel(self.center_admin_show_user, text= "Show user list".center(20), width=560)
        self.admin_show_user.grid(row = 1, column = 0, padx = 20, pady = 5)
        

        #self.center_admin_show_user.grid_remove()

        ###Add tab  
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
        
        self.add_dept = ctk.CTkOptionMenu(self.center_admin_add_user, width = 120, values=department_list, command=get_add_user_dept_dropdown)
        self.add_dept.grid(row = 1, column = 3, padx = 5, pady = 5)

        self.add_level = ctk.CTkOptionMenu(self.center_admin_add_user, width = 75, values = level_list)
        self.add_level.grid(row = 1, column = 4, padx = (5,15), pady = 5)
        #confirm button
        self.add_confirm = ctk.CTkButton(self.center_admin_add_user, width = 75, text = "Confirm", command=add_user_submit)
        self.add_confirm.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 25)
        #clear button
        self.add_confirm = ctk.CTkButton(self.center_admin_add_user, width = 75, text = "Clear input",
                                          command=clear_add_user, fg_color= ("gray15", "gray34"), hover_color= ("gray17","gray24"))
        self.add_confirm.grid(row = 2, column = 2, columnspan = 2, padx = 5, pady = 25)
        self.add_error_log = ctk.CTkLabel(self.center_admin_add_user, width = 480, text = "")
        self.add_error_log.grid(row = 3, column = 0, columnspan = 5, padx = 5, pady = 5)

        #remove menu grid
        self.center_admin_add_user.grid_remove()

        ###Modify user tab  
        self.center_admin_modify_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_modify_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_modify_user = ctk.CTkLabel(self.center_admin_modify_user, text= "Modify user".center(20), width=560)
        self.admin_modify_user.grid(row = 1, column = 0, padx = 20, pady = 5)


        self.center_admin_modify_user.grid_remove()

        ###Delete user tab  
        self.center_admin_delete_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_delete_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_delete_user = ctk.CTkLabel(self.center_admin_delete_user, text= "Delete user".center(20), width=560)
        self.admin_delete_user.grid(row = 1, column = 0, padx = 20, pady = 5)


        self.center_admin_delete_user.grid_remove()


        #Sakrivanje menija dok se korisnik ne ulogira
        #self.center_frame.grid_remove()
        
        


            

        
        
         
        
        
        
       














app = App()
app.mainloop()
