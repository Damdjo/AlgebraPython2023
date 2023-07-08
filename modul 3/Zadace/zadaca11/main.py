from typing import Optional, Tuple, Union
import database.user_db as db
import customtkinter as ctk
import os
os.chdir("modul 3/Zadace/zadaca11/")

#boja interfacea
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

#init varijable
db_path = "database/user_accounts.db"
logged_in = False
#funkcije
def sign_in(event):
    global logged_in
    uname = app.sidebar_uname_input.get()
    pword = app.sidebar_pword_input.get()
    message, logged_in = db.check_login(uname,pword,db_path)
    app.event_log_text.set(message)
    
    if logged_in:
        app.sidebar_login_frame.grid_remove()
        app.sidebar_user_frame.grid()
    

    print()

def sign_out(event):
    global logged_in
    app.sidebar_uname_input.delete(0,ctk.END)
    app.sidebar_pword_input.delete(0,ctk.END)
    app.event_log_text.set("")
    
    if logged_in:
        logged_in = False
        app.sidebar_user_frame.grid_remove()
        app.sidebar_login_frame.grid()
    
    

def test(event):
    ctk.set_appearance_mode("light")
    

columns = db.columns_tuple
def db_action(event):    
    #db.create_table(db_path)
    #admin_hardcode = ("admin","admin123","IT","5")
    #test = db.make_insert_query(admin_hardcode)    
    #db.db_execute(test, db_path)    
    #message = db.ispis_racuna(1,db_path=db_path)
    #app.event_log_text.set(message)
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
        self.grid_rowconfigure((0,1,2), weight= 1)
        
        #sidebar 1 gdje je login + profil info
        self.sidebar_login_frame = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar_login_frame.grid(row = 0, column = 0, rowspan = 4, sticky="nsew")
        self.sidebar_login_frame.grid_rowconfigure(6, weight=1)    
    
    
        #login title
        self.sidebar_top_label = ctk.CTkLabel(self.sidebar_login_frame, text="LOGIN", font = ctk.CTkFont(size = 20, weight="bold"))
        self.sidebar_top_label.grid(row = 0, column = 0, padx = 50, pady = (50, 20))
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
        
        #sidebar 2 sa podatcima ( u pocetku sakriven)
        self.sidebar_user_frame = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar_user_frame.grid(row = 0, column = 0, rowspan = 4, sticky="nsew")
        self.sidebar_user_frame.grid_rowconfigure(6, weight=1)
    
        self.sidebar_top_label = ctk.CTkLabel(self.sidebar_user_frame, text="WELCOME", font = ctk.CTkFont(size = 20, weight="bold"))
        self.sidebar_top_label.grid(row = 0, column = 0, padx = 50, pady = (50, 20))

        self.sidebar_submit_btn = ctk.CTkButton(self.sidebar_user_frame, width = 75, text="Sign out")
        self.sidebar_submit_btn.grid(row = 3, column = 0, padx = 15, pady = (10,0))
        self.sidebar_submit_btn.bind("<ButtonRelease-1>", sign_out)

        self.sidebar_user_frame.grid_remove()



            

        
        
        
        
        
        
        
       














app = App()
app.mainloop()
