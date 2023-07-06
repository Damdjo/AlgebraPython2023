# u gornjem dijelu:
#   USERNAME
#   PASSWORD

# Tri korisnika (admin, skladiste, blagajna)

#u donjem dijelu (ovisno o gore):
#   meni koji se pojavi, sve u jednom labelu, ali ispis različit, izlazom se briše donji dio
#       Admin: 
#               pozdrav Admin\n
#               1. uredi korisnike\n
#               2. uredi profil\n
#               0. izlaz\n
#       Skladistar: 
#               pozdrav Skladistar\n
#               1. dodaj robu\n
#               2. salji u MP\n
#               0. izlaz\n
#       Blagajna: 
#               pozdrav Blagajna\n
#               1. izdaj račun\n
#               2. povrat robe\n
#               0. izlaz\n

import tkinter as tk
users = {
    1:{"username":"admin", "password":"admin123"},
    2:{"username":"skladiste", "password":"skladiste123"},
    3:{"username":"blagajna", "password":"blagajna123"}
}

status = 0
meni_status = 0

def meni_keypress(event):
    global status, meni_status

    key = event.char
    print(key)


def login(event):
    global status
    sub_uname = uname_enter.get()
    sub_pword = pword_enter.get()

    for key, dict in users.items():
        if dict["username"] == sub_uname and dict["password"] == sub_pword:
            status = key

    
    match status:
        case 0:
            trgovina_meni_text.set("")
        case 1:
            string = """
            pozdrav Admin\n\t
            1. uredi korisnike\n\t
            2. uredi profil\n\t
            0. izlaz\n"""
            trgovina_meni_text.set(string)
        case 2:
            string = """
            pozdrav Skladistar\n\t
            1. dodaj robu\n\t
            2. salji u MP\n\t
            0. izlaz\n"""
            trgovina_meni_text.set(string)
        case 3:
            string = """
            pozdrav Blagajna\n\t
            1. izdaj račun\n\t
            2. povrat robe\n\t
            0. izlaz\n"""
            trgovina_meni_text.set(string)


root = tk.Tk()
root.title("Trgovina")
root.geometry("400x600")

login_frame = tk.Frame(root,height=200, background="Blue", width=400)
login_frame.grid(column=0,row=0, padx=5,pady=5)

trgovina_frame = tk.Frame(root,height=400, bg="Red",width=400)
trgovina_frame.grid(column=0,row=1, padx=5,pady=5)

#login frame
uname_label = tk.Label(login_frame,text="Username: ")
uname_label.grid(column=0,row=0, padx=5,pady=5)
uname_enter = tk.Entry(login_frame)
uname_enter.grid(column=1,row=0, padx=5,pady=5)

pword_label = tk.Label(login_frame,text="Password: ")
pword_label.grid(column=0,row=1, padx=5,pady=5)
pword_enter = tk.Entry(login_frame)
pword_enter.grid(column=1,row=1, padx=5,pady=5)

login_btn = tk.Button(login_frame,text="Login")
login_btn.grid(column=0,row=2, padx=5,pady=5)
login_btn.bind("<ButtonRelease-1>", login)

#trgovina frame

trgovina_meni_text = tk.StringVar()
trgovina_meni_text.set("")
trgovina_meni = tk.Label(trgovina_frame, textvariable= trgovina_meni_text, font=("Segoe UI", 12))
trgovina_meni.grid(column=0,row=0)
trgovina_meni.bind("<Key>", meni_keypress)






root.mainloop()