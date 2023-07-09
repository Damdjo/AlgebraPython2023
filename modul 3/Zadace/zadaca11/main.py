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
#funkcije

#Ulogiranje u program
def sign_in(event):
    global logged_in
    uname = app.sidebar_uname_input.get()
    pword = app.sidebar_pword_input.get()
    message, logged_in = db.check_login(uname,pword,db_path)
    app.event_log_text.set(message)
    # ovo zamijeni sidebar sa drugim ako je login uspješan
    if logged_in:
        app.sidebar_login_frame.grid_remove()
        app.sidebar_user_frame.grid()
        app.center_frame.grid()
    

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
    
def test_seg(event):
    text = app.center_seg_button_text.get()
    print(text)

def seg_button_change(value):
    global admin_seg_btn_menu
    print(admin_seg_btn_menu)
    admin_seg_btn_menu = value

    match admin_seg_btn_menu:
        case "Show user list":
            app.center_admin_show_user.grid() ####Stisnuti
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid_remove()
        case "Add user":
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid() ####Stisnuti
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid_remove()
        case "Modify user":
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid() ####Stisnuti
            app.center_admin_delete_user.grid_remove()
        case "Delete user":
            app.center_admin_show_user.grid_remove()
            app.center_admin_add_user.grid_remove()
            app.center_admin_modify_user.grid_remove()
            app.center_admin_delete_user.grid() ####Stisnuti
        case _:
            pass



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
        self.grid_columnconfigure((1,2,3), weight= 0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1,2,3,4), weight= 1)
        
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
        self.center_frame.grid_rowconfigure((1,2,3,4), weight = 1)
        #Center title
        self.center_title_text = ctk.StringVar()
        self.center_title_text.set("PLACEHOLDER")
        self.center_title = ctk.CTkLabel(self.center_frame, textvariable = self.center_title_text, font=("", 28) ,width=600, height=75, corner_radius=10, fg_color=("gray86", "gray17"))
        self.center_title.grid(row = 0, column = 1, columnspan = 2, padx = 20, pady = (5, 0), sticky = "n")
      ###Center frame #POTENCIJALNO SAMO ZA ADMINA, NOVI ZA USERE  
        self.center_switch_frame = ctk.CTkFrame(self.center_frame, width=600, corner_radius=5, fg_color="transparent")
        self.center_switch_frame.grid(row = 1, column = 1, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "ns")
        self.center_switch_frame.grid_rowconfigure(1, weight=1)
        ##################
        #Center tab button
        ##################
        self.center_seg_button_text = ctk.StringVar(value = "")
        self.center_seg_button = ctk.CTkSegmentedButton(self.center_switch_frame, command=seg_button_change, variable=self.center_seg_button_text)
        self.center_seg_button.grid(row = 0, column = 1, padx = 5, pady = (0, 5), columnspan = 2, sticky = "nsew")
        self.center_seg_button.configure(values = ["Show user list","Add user","Modify user","Delete user"])
        #Center tab
        ###Show user tab 
        self.center_admin_show_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_show_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_show_user = ctk.CTkLabel(self.center_admin_show_user, text= "Show user list")
        self.admin_show_user.pack()
        self.center_admin_show_user.grid_remove()
        ###Add tab  
        self.center_admin_add_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_add_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_add_user = ctk.CTkLabel(self.center_admin_add_user, text= "Add user")
        self.admin_add_user.pack()
        self.center_admin_add_user.grid_remove()
        ###Modify user tab  
        self.center_admin_modify_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_modify_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_modify_user = ctk.CTkLabel(self.center_admin_modify_user, text= "Modify user")
        self.admin_modify_user.pack()
        self.center_admin_modify_user.grid_remove()
        ###Delete user tab  
        self.center_admin_delete_user = ctk.CTkFrame(self.center_switch_frame, width=600, corner_radius=5)
        self.center_admin_delete_user.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, padx = 20, pady = 5, sticky = "nsew")
        self.admin_delete_user = ctk.CTkLabel(self.center_admin_delete_user, text= "Delete user")
        self.admin_delete_user.pack()
        self.center_admin_delete_user.grid_remove()


        #Sakrivanje menija dok se korisnik ne ulogira
        self.center_frame.grid_remove()
        
        


            

        
        
         
        
        
        
       



"""
self.center_tabview = ctk.CTkTabview(self.center_frame, width=800)
        self.center_tabview.grid(row = 1, column = 1, padx = 5, pady = (0, 5), sticky = "nsew")
        #tabs
        self.center_tabview.add("Show user list")
        self.center_tabview.tab("Show user list").grid_columnconfigure(0, weight=1)
        self.center_tabview.add("Add user")
        self.center_tabview.tab("Add user").grid_columnconfigure(1, weight=1)
        self.center_tabview.add("Modify user")
        self.center_tabview.tab("Modify user").grid_columnconfigure(2, weight=1)
        self.center_tabview.add("Delete user")
        self.center_tabview.tab("Delete user").grid_columnconfigure(3, weight=1)
"""










app = App()
app.mainloop()
