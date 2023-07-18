from typing import Optional, Tuple, Union
import database.user_db as db
import customtkinter as ctk  ########### pip install customtkinter ##########
import time, threading, winsound #wait and sound function for doorbell


#DOKUMENTACIJA: https://customtkinter.tomschimansky.com/documentation
#GITHUB:        https://github.com/TomSchimansky/CustomTkinter/tree/master
#Colors:        https://www.wikipython.com/wp-content/uploads/Color-chart-capture-082321.jpg

import os
os.chdir("modul 3/smartkey_damjan_jaksic_V2")
sound = "door_bell.wav"



#pocetne varijable
db_path = "database/user_accounts.db"
user_pin = ""
admin_selected_user = ""
locked = True
admin_menu_check = False
admin_menu = False
#user cheatsheet
#(userID,   username,   PIN,    is_admin,   active)
#(1,        'admin',    123456, 1,          1)


####funkcije
#pozvoni
def pozvoni():
    winsound.PlaySound(sound,winsound.SND_ASYNC)
    app.status_text.configure(fg_color = "forestgreen")            
    app.status_text.delete("0.0","end")            
    app.status_text.insert("1.0","Bell rung\n")           
    app.status_text.insert("2.0","Please wait a moment for somebody to open the door!\n")
    #ovo je thread tako da se lijepo ispisuje u status baru i da ne zašteka cijeli program kada se koristi time.sleep
    t2 = threading.Thread(target=timer_5_sec)
    t2.start()
    
    
def timer_5_sec():
    text_index = 3.0
    for second in range (5,0,-1):                   
        app.status_text.insert(f"{text_index}",f"{second}...\n")
        print((f"{text_index}",f"{second}...\n"))
        print(text_index)
        text_index += 1.0        
        time.sleep(1)
    keypad_press("C")

#otkljucaj
def lock_unlock():
    global locked
    if locked:
        keypad(app.keypad_frame)
        app.keypad_frame.grid_configure(padx = (30,8))
        app.status_frame.grid_configure(padx = (20,10))
        app.lock_button.configure(text = "Lock")
        locked = False
    else:
        app.admin_panel.grid_remove()
        keypad_press("C")
        app.keypad_frame.destroy()        
        app.keypad_frame = ctk.CTkFrame(app.pin_panel, fg_color="transparent", width=290, height=290)
        app.keypad_frame.grid(row = 0, rowspan = 2, column = 0, sticky = "nsw",padx= (20,0))
        app.lock_button.configure(text = "Unlock")
        locked = True

#ukucavanje keypada
def keypad_press(value) -> str | None | list:
    global user_pin, admin_menu_check, admin_menu
    match value:
        case "Enter":
            print(user_pin)
            check_pin(user_pin)
        case "C":
            print("C")
            app.status_text.configure(fg_color = "transparent")            
            app.status_text.delete("0.0","end")            
            app.status_text.insert("1.0","Enter PIN:")            
            app.status_text.insert("2.0","\n")
            user_pin = ""
            #check if app will open admin panel when admin user first logs on, this part is when app shouldnt open it
            if admin_menu_check:
                error_textbox("Alarm unlocked!", "forestgreen")
                admin_menu_check = False
                admin_menu = False
        case "*":
            #check if app will open admin panel when admin user first logs on, this part is when app should open it
            if admin_menu_check:
                admin_menu_check = False
                admin_menu = True
                if admin_menu:
                    error_textbox("Opening admin panel", "forestgreen")
                    app.admin_panel.grid()
                    userTable(app.admin_info_panel)
            
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
    global admin_menu_check
    data = db.ispis_racuna(2,"PIN",arg_list,db_path=db_path)
    app.active_user = data #type: ignore
    if app.active_user != "User does not exist":
        #check admin
        if app.active_user[4] == 1 and app.active_user[5] == 1:
            admin_menu_check = True
            error_textbox("Do you want to open admin menu?\nPress '*' to open or 'C' to ignore","forestgreen")          
            
                
            
        #check aktivan
        elif app.active_user[5] == 1:
            error_textbox("Alarm unlocked!", "forestgreen")
        elif app.active_user[5] == 0:
            error_textbox("User inactive!")

    else:
        error_textbox("User does not exist!")

def refresh_user_table():
    """
    Funkcija "refresha" tablicu tako da destroya frame pa ponovno sve kreira ispocetka
    """
    app.admin_info_panel.destroy()
    app.admin_info_panel = ctk.CTkScrollableFrame(app.admin_panel,width = 300, corner_radius=0)                
    app.admin_info_panel.grid(row = 0, rowspan = 4, column = 0, sticky = "nsew")
    userTable(app.admin_info_panel)

def error_textbox(error_message, color = "maroon"):
    app.status_text.configure(fg_color = color)                                
    app.status_text.delete("0.0","end")            
    app.status_text.insert("1.0",f"{error_message}")    

def cancel():
    app.name_entry.delete(0,ctk.END)
    app.name_entry.configure(placeholder_text = "Input name:")
    app.surname_entry.delete(0,ctk.END)
    app.surname_entry.configure(placeholder_text = "Input surname:")
    app.pin_entry.delete(0,ctk.END)
    app.pin_entry.configure(placeholder_text = "Input PIN:")
    app.active_check_var.set(value = "0")
    app.admin_check_var.set(value = "0")
    app.rfid_check_var.set(value = "0")

def fill_admin_info(user_data_tuple, button_pressed = "None"):
    """
    Funkcija koja kada se stisne get gumb u tablici usera povlači podate te ih postavlja kao placeholder vrijednosti u admin info panelu 
    ili briše sve unesene vrijednosti ako se stisne cancel gumb

    """
    global admin_selected_user
    if len(user_data_tuple) == 7:
        admin_selected_user = user_data_tuple[0]
        app.name_entry.configure(placeholder_text = user_data_tuple[1])
        app.surname_entry.configure(placeholder_text = user_data_tuple[2])
        app.pin_entry.configure(placeholder_text = user_data_tuple[3])
        app.admin_check_var.set(value = str(user_data_tuple[4]))
        app.active_check_var.set(value = str(user_data_tuple[5]))
        app.rfid_check_var.set(value = str(user_data_tuple[6]))
    match button_pressed:
        case "Cancel":
            cancel()

        case "Save":
            old_data_tuple = get_table_data(2,"userID", admin_selected_user)
            id = old_data_tuple[0]   
            name = app.name_entry.get()
            surname = app.surname_entry.get()
            pin = app.pin_entry.get()
            active = app.active_check_var.get()
            admin = app.admin_check_var.get()
            rfid = app.rfid_check_var.get()
            
            print(len(pin))
            data_tuple = (id,name,surname,pin,admin,active,rfid)
            if len(pin) != 6 and len(str(old_data_tuple[3])) != 6:
                print(len(pin))
                error_textbox(f"PIN must be 6 characters long")
            
            elif id != 1:

                update_query = db.make_update_query(old_data_tuple,data_tuple) #type: ignore
                message = db.db_execute(update_query,db_path=db_path)
                if message != None:
                    error = message[32:]
                    print(error)
                    match error:
                        case "uname":
                            error_textbox(f"{error} is already taken!")
                            
                        case "PIN":
                            error_textbox(f"{error} is already taken!") 
                else:
                    refresh_user_table()
            else:
                app.status_text.configure(fg_color = "maroon")                                
                app.status_text.delete("0.0","end")            
                app.status_text.insert("1.0","Cannot change Admin user!")            
                app.status_text.insert("2.0","\nPress C to clear text!")
        
        case "Delete":
            old_data_tuple = get_table_data(2,"userID", admin_selected_user)
            id = old_data_tuple[0]   
            
            if id != 1:
                delete_query = f"DELETE FROM users WHERE userID = '{id}'"
                db.db_execute(delete_query,db_path=db_path)
                refresh_user_table()

            else:
                app.status_text.configure(fg_color = "maroon")                                
                app.status_text.delete("0.0","end")            
                app.status_text.insert("1.0","Cannot delete Admin user!")            
                app.status_text.insert("2.0","\nPress C to clear text!")
        
        case None:
            pass

        case _:
            print("*****")
            print(button_pressed)
            
            print("*****")

    


#klase

#klasa koja ispisuje keypad 
class keypad:
    def __init__(self, app):
        keypad_buttons = [[" "," "," ","Enter"],["1","2","3"],["4","5","6"],["7","8","9"],["*","0","C"]]

        self.total_rows = len(keypad_buttons)
        self.total_columns = len(keypad_buttons[0])

        for row in range(self.total_rows):
            if row == 0:
                for column in range(self.total_columns):
                    self.button_var = ctk.StringVar(value=keypad_buttons[row][column])
                    self.entry = ctk.CTkButton(app, textvariable = self.button_var, width=60, height=50, command= lambda i = self.button_var.get(): keypad_press(i)) #type: ignore
                    self.entry.grid(row = row, column = column, padx = 4, pady = 4)
            else:
                for column in range(self.total_columns-1):
                    self.button_var = ctk.StringVar(value=keypad_buttons[row][column])
                    self.entry = ctk.CTkButton(app, textvariable = self.button_var, width=60, height=50, command= lambda i = self.button_var.get(): keypad_press(i))#type: ignore
                    self.entry.grid(row = row, column = column, padx = 4, pady = 4)
    
        

#klasa koja ispisuje tablicu usera kada se ulogira user admin
class userTable:
    def __init__(self, app):
        data = get_table_data(1)
        
        total_rows = len(data)
        total_columns = len(data[0])

        for row in range(total_rows):
            match data[row][5]:
                case 0:
                    color = "maroon"
                case 1:
                    color = "forestgreen"
            for column in range(total_columns):
                match column:
                    case 1:                        
                        self.entry = ctk.CTkEntry(app, width=80, fg_color=color) #type: ignore
                        self.entry.grid(row = row+1, column = 0, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])                            
                    case 2:
                        self.entry = ctk.CTkEntry(app, width=80, fg_color=color) #type: ignore
                        self.entry.grid(row = row+1, column = 1, padx = 2, pady = 1)
                        self.entry.insert(ctk.END, data[row][column])
                    case 6:
                        self.entry = ctk.CTkEntry(app, width=80, fg_color=color) #type: ignore
                        self.entry.grid(row = row+1, column = 2, padx = 2, pady = 1)
                        match data[row][column]:
                            case 0:
                                self.entry.insert(ctk.END, "Nema RFID")
                            case 1:
                                self.entry.insert(ctk.END, "Ima RFID")

                        
            self.button_var = ctk.StringVar(value=data[row][0])
            self.fetch_button = ctk.CTkButton(app, width=20, text="Get", command = lambda i = self.button_var.get(): self.fetch_by_id(i))
            self.fetch_button.grid(row = row+1, column = 3, padx = 2, pady = 1)
    def fetch_by_id(self, id):
        global admin_selected_user    
        user = get_table_data(2,"userID", vrijednost=id)
        cancel()
        fill_admin_info(user)
        print(id)
        print(user)
    


                    


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
        #ring button
        self.ring_button = ctk.CTkButton(self.panel_s_gumbima, width = 150, height = 70, font=("",18), text= "Ring bell", command=pozvoni) # type: ignore
        self.ring_button.grid(row= 0, column = 0, padx = (30,30), pady= (60,40), sticky = "sw")

        #lock button
        self.lock_button = ctk.CTkButton(self.panel_s_gumbima, width = 150, height = 70, font=("",18), text= "Unlock", command=lock_unlock)
        self.lock_button.grid(row= 0, column = 2, padx = (30,30), pady= (60,40), sticky = "se")

    #####pin panel 
        self.pin_panel = ctk.CTkFrame(self, width=700, height=470, fg_color="transparent")
        self.pin_panel.grid(row = 1, column = 0, sticky = "new", pady=30, padx= 0)
        
        #keypad
        self.keypad_frame = ctk.CTkFrame(self.pin_panel, fg_color="transparent", width=290, height=290)
        self.keypad_frame.grid(row = 0, rowspan = 2, column = 0, sticky = "nsw",padx= (20,0))
        self.keypad_frame.grid_remove()
        

        #status frame         
        self.status_frame = ctk.CTkFrame(self.pin_panel, width=350)
        self.status_frame.grid(row = 0,rowspan =2, column = 1, sticky = "nse",padx = (330,20), pady= 0)
        print(self.status_frame._current_width)
        self.status_frame.grid_columnconfigure(1,weight=1)
        self.status_title = ctk.CTkLabel(self.status_frame, text = "Status and messages")
        self.status_title.grid(row = 0, column = 0, sticky = "new")
        self.status_text = ctk.CTkTextbox(self.status_frame, width=350,height = 270, fg_color="transparent")
        self.pin_input = ctk.StringVar(value="#")
        self.status_text.insert("0.0",f"Enter PIN:\n")
        self.status_text.grid(row = 1, column = 0, sticky = "new")
        


        #admin panel 
        self.admin_panel = ctk.CTkFrame(self, width=700)
        self.admin_panel.grid(row = 4, column = 0, sticky = "nsew", pady = (0,10))
        self.admin_info_panel = ctk.CTkScrollableFrame(self.admin_panel,width = 300, corner_radius=0)
        self.admin_info_panel.grid(row = 0, rowspan = 4, column = 0, sticky = "nsew")
        self.admin_input_panel = ctk.CTkFrame(self.admin_panel,width = 400, corner_radius=0, fg_color="transparent")
        self.admin_input_panel.grid(row = 0, rowspan = 4, column = 1,columnspan = 2, sticky = "new")
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
        self.active_check_var = ctk.StringVar(value="0")
        self.active_check = ctk.CTkCheckBox(self.checkbox_frame, text="Active", variable=self.active_check_var, onvalue="1", offvalue="0")
        self.active_check.grid(row=0, column = 0, padx = (30,10), pady = 10)
        #admin
        self.admin_check_var = ctk.StringVar(value="0")
        self.admin_check = ctk.CTkCheckBox(self.checkbox_frame, text="Admin", variable=self.admin_check_var, onvalue="1", offvalue="0")
        self.admin_check.grid(row=0, column = 1, padx = 10, pady = 10)
        #rfid
        self.rfid_check_var = ctk.StringVar(value="0")
        self.rfid_check = ctk.CTkCheckBox(self.checkbox_frame, text="RFID", variable=self.rfid_check_var, onvalue="1", offvalue="0")
        self.rfid_check.grid(row=0, column = 2, padx = 10, pady = 10)
        #buttons
        self.checkbox_frame = ctk.CTkFrame(self.admin_input_panel,width = 385, height = 50)
        self.checkbox_frame.grid(row = 5, column = 0, columnspan = 2, sticky = "sew")
        #save
        self.save_button = ctk.CTkButton(self.checkbox_frame, text="Save", width=90, command= lambda button_pressed = "Save" : fill_admin_info((),button_pressed))
        self.save_button.grid(row=0, column = 0, padx = (25,10), pady = 10)
        #cancel
        self.cancel_button = ctk.CTkButton(self.checkbox_frame, text="Cancel", width=90, command= lambda button_pressed = "Cancel" : fill_admin_info((),button_pressed))
        self.cancel_button.grid(row=0, column = 1, padx = 10, pady = 10)
        #delete
        self.delete_button = ctk.CTkButton(self.checkbox_frame, text="Delete", width=90, command= lambda button_pressed = "Delete" : fill_admin_info((),button_pressed))
        self.delete_button.grid(row=0, column = 2, padx = 10, pady = 10)

        #admin panel hide
        self.admin_panel.grid_remove()



#main
app = App()
app.mainloop()