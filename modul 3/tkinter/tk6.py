import os
import tkinter as tk
os.chdir("m3/tkinter")

unesena_slova=""

def handle_keypress(event):
    global unesena_slova
    key = str(event.keysym)    
    
    if key == "BackSpace":
        unesena_slova = unesena_slova[:-1]
        label_text_var.set(unesena_slova)
    else:
        unesena_slova += str(event.char)
        label_text_var.set(unesena_slova)


def mouse_click_press(event):
    event = str(event)[-14:-13]    
    match event:
        case "1":
            label_text_var.set("Lijevi klik")
        case "2":
            label_text_var.set("Kotacic klik")
        case "3":
            label_text_var.set("Desni klik")

def pokret_misa(event):
    event = str(event)[25:].center(20)
    label_mouse_var.set(f"Koordinate miša su: {event}")
            


def brisi_sve():
    global unesena_slova
    unesena_slova = ""
    label_text_var.set("")

root = tk.Tk()
root.title("Events1")
root.geometry("600x400")

label_text_var = tk.StringVar()
label_text_var.set("Mjesto za prikaz slova")
label_mouse_var = tk.StringVar()
label_mouse_var.set("Koordinate miša u prozoru su: ".center(20))


label_naslov = tk.Label(root,text="Key event", font=("Segoe UI", 24), fg="red")
label_naslov.grid(column=0,row=0)

label_ispis = tk.Label(root, textvariable = label_text_var, font=("Segoe UI", 24), fg="red")
label_ispis.grid(column=0,row=1)

label_mouse_coord = tk.Label(root, textvariable = label_mouse_var, font=("Segoe UI", 24), fg="red")
label_mouse_coord.grid(column=0,row=2)

button_brisanje = tk.Button(root, text="Obriši sve", font=("Segoe UI", 12), command=brisi_sve)
button_brisanje.grid(column=0,row=3, pady=(10,0))



root.bind("<Key>", handle_keypress)
root.bind("<ButtonRelease-1>", mouse_click_press)
root.bind("<ButtonRelease-2>", mouse_click_press)
root.bind("<ButtonRelease-3>", mouse_click_press)
root.bind("<Motion>", pokret_misa)

root.mainloop()