import tkinter as tk
from loto import *

#funkcije

def hide_lower():
    label_gen.config(text="",relief="flat")
    broj1_gen.config(text="")
    broj2_gen.config(text="")
    broj3_gen.config(text="")
    broj4_gen.config(text="")
    broj5_gen.config(text="")
    bonus1_gen.config(text="")
    bonus2_gen.config(text="") 
    pog_reg_text.config(text="",relief="flat")
    pog_bon_text.config(text="",relief="flat")


def submit_user_numbers() -> list:
    user_lista = []
    user_lista.append(broj1.get())
    user_lista.append(broj2.get())
    user_lista.append(broj3.get())
    user_lista.append(broj4.get())
    user_lista.append(broj5.get())
    user_lista.append(bonus1.get())
    user_lista.append(bonus2.get())
    
    if "" in user_lista:
        hide_lower()
        popup("Krivi unos","Brojevi su krivo uneseni!","200x60")

    

    input_ok = True
    error_msg = ""
    for broj in user_lista[:5]:
        try:
            broj = int(broj)
        except ValueError:
            hide_lower()
            popup("Krivi unos","Unos mora biti broj!","200x60")
        else:
            broj = int(broj)

        if broj > 50 or broj < 1:
            hide_lower()
            error_msg = "Brojevi moraju biti u rasponu od 1 do 50"
            input_ok = False
    for broj in user_lista[5:]:
        try:
            broj = int(broj)
        except ValueError:
            hide_lower()
            popup("Krivi unos","Unos mora biti broj!","200x60")
        else:
            broj = int(broj)
        if broj > 12 or broj < 1:
            hide_lower()
            error_msg = "Brojevi moraju biti u rasponu od 1 do 50\nBonus brojevi moraju biti u rasponu od 1 do 12"
            input_ok = False
    if error_msg !="":
        popup("Error",error_msg,"350x60") 
                
                    

                    
            
                
    if input_ok:
        return user_lista
    else:
        return []

def gumb_potvrdi():
    global generirani
    generirani = submit_user_numbers()    
    user_brojevi = generirani[:5]
    user_bonus = generirani[5:]
    random_do_50 = vrtiBrojeve(5,50)
    bonus_do_12 = vrtiBrojeve(2,12)

    if generirani != []:
        if "" in user_brojevi or "" in user_bonus:
            hide_lower()
            popup("Krivi unos","Brojevi su krivo uneseni!","200x60")
    
        elif len(set(user_brojevi)) != 5 or len(set(user_bonus)) != 2:
            hide_lower()
            popup("Krivi unos","Brojevi ne smiju imati duplikate!","265x60")
        else:                
            label_gen.config(text="Rand",relief="groove")
            broj1_gen.config(text=random_do_50[0])
            broj2_gen.config(text=random_do_50[1])
            broj3_gen.config(text=random_do_50[2])
            broj4_gen.config(text=random_do_50[3])
            broj5_gen.config(text=random_do_50[4])
            bonus1_gen.config(text=bonus_do_12[0])
            bonus2_gen.config(text=bonus_do_12[1])
            poruka_gen, poruka_bon = tkinterProvjera(user_brojevi,random_do_50,user_bonus,bonus_do_12)     
            pog_reg_text.config(text=poruka_gen,relief="ridge")
            pog_bon_text.config(text=poruka_bon,relief="ridge")
    

def popup(title, message, dimenzije):
    window = tk.Toplevel(root)
    window.geometry(dimenzije)
    window.title(title)
    tk.Label(window, text=message, font=("",12),padx=10,pady=10).grid()



    




root = tk.Tk()
root.title('Eurojackpot')

root.rowconfigure(0, weight=1, minsize=200)
root.rowconfigure(1, weight=1, minsize=200)
root.rowconfigure(2, weight=1, minsize=200)

header = tk.Frame(root,background="Blue",padx=(200),pady=(75),width="100")
header.grid(row=0)
header_title = tk.Label(header,text=("EUROJACKPOT"),font=("",34), background="Blue").pack()

body = tk.Frame(root)
body.grid(row=1)

body.columnconfigure(0, weight=1, minsize=15)
body.columnconfigure(1, weight=1, minsize=300)
body.columnconfigure(2, weight=1, minsize=75)

body.rowconfigure(0, weight=1, minsize=50)
body.rowconfigure(1, weight=1, minsize=45)
body.rowconfigure(2, weight=1, minsize=50)

input_frame = tk.Frame(body)
input_frame.grid(row=1,column=1)

#Unos brojeva i generirani
##text
broj1_text = tk.Label(input_frame,width=5,text="1. Broj",relief="groove")
broj1_text.grid(row=0,column=0,padx=(2,2))
broj2_text = tk.Label(input_frame,width=5,text="2. Broj",relief="groove")
broj2_text.grid(row=0,column=1,padx=(2,2))
broj3_text = tk.Label(input_frame,width=5,text="3. Broj",relief="groove")
broj3_text.grid(row=0,column=2,padx=(2,2))
broj4_text = tk.Label(input_frame,width=5,text="4. Broj",relief="groove")
broj4_text.grid(row=0,column=3,padx=(2,2))
broj5_text = tk.Label(input_frame,width=5,text="5. Broj",relief="groove")
broj5_text.grid(row=0,column=4,padx=(2,2))
bonus1_text = tk.Label(input_frame,width=6,text="Bonus 1",relief="groove")
bonus1_text.grid(row=0,column=7,padx=(25,4))
bonus2_text = tk.Label(input_frame,width=6,text="Bonus 2",relief="groove")
bonus2_text.grid(row=0,column=8,padx=(4,4))
##polja
broj1 = tk.Entry(input_frame,width=5)
broj1.grid(row=1,column=0,padx=(2,2))
broj2 = tk.Entry(input_frame,width=5)
broj2.grid(row=1,column=1,padx=(2,2))
broj3 = tk.Entry(input_frame,width=5)
broj3.grid(row=1,column=2,padx=(2,2))
broj4 = tk.Entry(input_frame,width=5)
broj4.grid(row=1,column=3,padx=(2,2))
broj5 = tk.Entry(input_frame,width=5)
broj5.grid(row=1,column=4,padx=(2,2))
bonus1 = tk.Entry(input_frame,width=5)
bonus1.grid(row=1,column=7,padx=(25,4))
bonus2 = tk.Entry(input_frame,width=5)
bonus2.grid(row=1,column=8,padx=(4,4))
##generiranje
label_gen = tk.Label(input_frame,width=5,text="",font=("",9))
label_gen.grid(row=3,column=0,padx=(2,2),pady=(20,0))
broj1_gen = tk.Label(input_frame,width=5,text="")
broj1_gen.grid(row=4,column=0,padx=(2,2))
broj2_gen = tk.Label(input_frame,width=5,text="")
broj2_gen.grid(row=4,column=1,padx=(2,2))
broj3_gen = tk.Label(input_frame,width=5,text="")
broj3_gen.grid(row=4,column=2,padx=(2,2))
broj4_gen = tk.Label(input_frame,width=5,text="")
broj4_gen.grid(row=4,column=3,padx=(2,2))
broj5_gen = tk.Label(input_frame,width=5,text="")
broj5_gen.grid(row=4,column=4,padx=(2,2))
bonus1_gen = tk.Label(input_frame,width=6,text="")
bonus1_gen.grid(row=4,column=7,padx=(25,4))
bonus2_gen = tk.Label(input_frame,width=6,text="")
bonus2_gen.grid(row=4,column=8,padx=(4,4))

#Poruka rezultata
poruke_frame = tk.Frame(body)
poruke_frame.grid(row=2,column=1)
pog_reg_text = tk.Label(poruke_frame,width=45,text="", font=("",12))
pog_reg_text.grid(row=0,column=0,padx=(2,2),pady=(10,0))
pog_bon_text = tk.Label(poruke_frame,width=45,text="", font=("",12))
pog_bon_text.grid(row=1,column=0,padx=(2,2),pady=(10,10))

#Submit brojevi
submit_frame = tk.Frame(body)
submit_frame.grid(row=3,column=1)
submit_btn = tk.Button(submit_frame, text="Potvrdi",width=15,height=1,command=gumb_potvrdi).grid(row=0,column=0,pady=(25,0))



root.mainloop()