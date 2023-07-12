from typing import Optional, Tuple, Union
import database.user_db as db
import customtkinter as ctk  ########### pip install customtkinter ##########

#DOKUMENTACIJA: https://customtkinter.tomschimansky.com/documentation
#GITHUB:        https://github.com/TomSchimansky/CustomTkinter/tree/master

import os
os.chdir("modul 3/smartkey_damjan_jaksic_V1")


#pocetne varijable
db_path = "database/user_accounts.db"
user_pin = ""

#user cheatsheet
#(userID,   username,   PIN,    is_admin,   active)
#(1,        'admin',    123456, 1,          1)


####funkcije
#pozvoni
def pozvoni() -> str | None:
    print("DING-DONG")
    return "DING-DONG"

#otkljucaj
def otkljucaj():
    pass
#ukucavanje keypada
def keypad_press(value):
    global user_pin
    match value:
        case "Enter":
            print(user_pin)
            check_pin(user_pin)
        case "C":
            print("C")            
            app.status_text.delete("2.0","end")            
            app.status_text.insert("2.0","\n")
            user_pin = ""
        case _:
            if len(user_pin) < 6:
                user_pin += (value)
                app.status_text.insert("3.0","*")
    #return value
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

#provjera jel pin dobar
def check_pin(arg_list):
    data = db.ispis_racuna(2,"PIN",arg_list,db_path=db_path)
    app.active_user = data #type: ignore
    #check admin
    if app.active_user[4] == 1:
        userTable(app.admin_info_panel)
        print("admin!")
    #check aktivan
    if app.active_user[3] == 1:
        print("aktivan!")

#klase

class keypad:
    def __init__(self, app):
        keypad_buttons = [[" "," "," ","Enter"],["1","2","3"],["4","5","6"],["7","8","9"],[" ","0","C"]]

        total_rows = len(keypad_buttons)
        total_columns = len(keypad_buttons[0])

        for row in range(total_rows):
            if row == 0:
                for column in range(total_columns):
                    self.button_var = ctk.StringVar(value=keypad_buttons[row][column])
                    self.entry = ctk.CTkButton(app, textvariable = self.button_var, width=60, height=50, command= lambda i = self.button_var.get(): keypad_press(i))
                    self.entry.grid(row = row, column = column, padx = 4, pady = 4)
            else:
                for column in range(total_columns-1):
                    self.button_var = ctk.StringVar(value=keypad_buttons[row][column])
                    self.entry = ctk.CTkButton(app, textvariable = self.button_var, width=60, height=50, command= lambda i = self.button_var.get(): keypad_press(i))
                    self.entry.grid(row = row, column = column, padx = 4, pady = 4)

class userTable:
    def __init__(self, app):
        data = get_table_data(1)
        
        total_rows = len(data)
        total_columns = len(data[0])

        for row in range(total_rows):
            for column in range(total_columns):
                match column:
                    case 1:                        
                        self.entry = ctk.CTkEntry(app, width=80)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])
                            
                    case 2:
                        self.entry = ctk.CTkEntry(app, width=120)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])
                    case 6:
                        self.entry = ctk.CTkEntry(app, width=80,)
                        self.entry.grid(row = row+1, column = column, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, "Ima RFID")
                    


class App(ctk.CTk):
    def __init__(self):
        super().__init__()       
        self.active_user = ()
        # prozor
        self.title("Placeholder naziv")
        self.geometry(f"{700}x{900}")

        # definiranje grida
        self.grid_columnconfigure((0,2), weight= 0) # type: ignore
        self.grid_columnconfigure((1), weight= 1) # type: ignore
        self.grid_rowconfigure(0, weight= 0) # type: ignore
        self.grid_rowconfigure((1,2,3,4), weight= 2) # type: ignore

    #####panel s gumbima
        self.panel_s_gumbima = ctk.CTkFrame(self, width = 700)
        self.panel_s_gumbima.grid(row = 0, column = 0, columnspan = 3, sticky = "nsew")
        self.panel_s_gumbima.grid_columnconfigure((0,2), weight=0) #type: ignore
        self.panel_s_gumbima.grid_columnconfigure(1, weight=1) #type: ignore
        #pozvoni button
        self.pozvoni_button = ctk.CTkButton(self.panel_s_gumbima, width = 90, text= "Pozvoni", command=pozvoni) # type: ignore
        self.pozvoni_button.grid(row= 0, column = 0, padx = (30,30), pady= (60,20), sticky = "sw")

        #otkljucaj button
        self.otkljucaj_button = ctk.CTkButton(self.panel_s_gumbima, width = 90, text= "Otključaj", command=otkljucaj)
        self.otkljucaj_button.grid(row= 0, column = 2, padx = (30,30), pady= (60,20), sticky = "se")

    #####pin panel 
        self.pin_panel = ctk.CTkFrame(self, width=700)
        self.pin_panel.grid(row = 1, rowspan = 3, column = 0, sticky = "nsew")
        self.pin_panel.grid_rowconfigure((0,1),weight=1) #type: ignore
        
        #keypad
        self.keypad_frame = ctk.CTkFrame(self.pin_panel, fg_color="transparent")
        self.keypad_frame.grid(row = 1, rowspan = 2, column = 0, sticky = "nsew", padx = 30, pady= 70)
        self.keypad = keypad(self.keypad_frame)

        #status frame         
        self.status_frame = ctk.CTkFrame(self.pin_panel, width=350)
        self.status_frame.grid(row = 1, rowspan = 2, column = 1, columnspan = 2, sticky = "nsew", padx =0, pady= 70)
        self.status_frame.grid_columnconfigure(1,weight=1)
        self.status_title = ctk.CTkLabel(self.status_frame, text = "Status i poruke")
        self.status_title.grid(row = 0, column = 0, sticky = "new")
        self.status_text = ctk.CTkTextbox(self.status_frame, width=350, fg_color="transparent")
        self.pin_input = ctk.StringVar(value="#")
        self.status_text.insert("0.0",f"Enter PIN:\n")
        self.status_text.grid(row = 1, column = 0, sticky = "new")
        


        #admin panel 
        self.admin_panel = ctk.CTkFrame(self, width=700)
        self.admin_panel.grid(row = 5, rowspan = 2, column = 0, sticky = "nsew", pady = (0,10))
        self.admin_info_panel = ctk.CTkScrollableFrame(self.admin_panel,width = 300, corner_radius=0)
        self.admin_info_panel.grid(row = 0, rowspan = 2, column = 0, sticky = "nsew")
        self.admin_input_panel = ctk.CTkFrame(self.admin_panel,width = 400, corner_radius=0, fg_color="transparent")
        self.admin_input_panel.grid(row = 0, rowspan = 3, column = 1,columnspan = 2, sticky = "new")
        self.admin_input_panel.grid_rowconfigure((0,1,2),weight=10) #type: ignore
        self.admin_input_panel.grid_rowconfigure(3,weight=0) #type: ignore
        #ime
        self.name_label = ctk.CTkLabel(self.admin_input_panel, text ="Name: ")
        self.name_label.grid(row = 0, column = 0, padx= 10, pady=10)
        self.name_entry = ctk.CTkEntry(self.admin_input_panel, placeholder_text="Input name:")
        self.name_entry.grid(row = 0, column = 1, padx= 10, pady=10)
        #prezime
        self.surname_label = ctk.CTkLabel(self.admin_input_panel, text ="Surname: ")
        self.surname_label.grid(row = 1, column = 0, padx= 10, pady=10)
        self.surname_entry = ctk.CTkEntry(self.admin_input_panel, placeholder_text="Input surname:")
        self.surname_entry.grid(row = 1, column = 1, padx= 10, pady=10)

        #pin
        self.pin_label = ctk.CTkLabel(self.admin_input_panel, text ="PIN: ")
        self.pin_label.grid(row = 2, column = 0, padx= 10, pady=10)
        self.pin_entry = ctk.CTkEntry(self.admin_input_panel, placeholder_text="Input PIN:")
        self.pin_entry.grid(row = 2, column = 1, padx= 10, pady=10)

        #checkbox
        self.checkbox_frame = ctk.CTkFrame(self.admin_input_panel,width = 385, height = 50)
        self.checkbox_frame.grid(row = 4, column = 0, columnspan = 2, sticky = "sew")
        #active
        self.active_check = ctk.CTkCheckBox(self.checkbox_frame, text="Active")
        self.active_check.grid(row=0, column = 0, padx = (30,10), pady = 10)
        #admin
        self.admin_check = ctk.CTkCheckBox(self.checkbox_frame, text="Admin")
        self.admin_check.grid(row=0, column = 1, padx = 10, pady = 10)
        #rfid
        self.rfid_check = ctk.CTkCheckBox(self.checkbox_frame, text="RFID")
        self.rfid_check.grid(row=0, column = 2, padx = 10, pady = 10)



#main
app = App()
app.mainloop()