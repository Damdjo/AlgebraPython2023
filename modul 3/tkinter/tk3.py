import os
import tkinter as tk
os.chdir("m3/tkinter")

def click():
    label.config(text = "izmjenjeni tekst\n u tri\nreda",
                 font=("Segoe UI", 16), fg = "red").pack(padx=30,pady=40)


root = tk.Tk()

root.title("Treca sreca")
root.geometry("600x500")

label = tk.Label(root, text="Poruka\nu dva reda",
                 font=("Segoe UI", 16))
label.pack(padx=30,pady=40)

button_click = tk.Button(root, text = "Stisni me!", command = click).pack(padx=10,pady=10)

image_in_label = tk.PhotoImage(file="python-logo.png").subsample(7)
label_image = tk.Label(root, text="Poruka sa slikom",
                       font=("Segoe UI", 16),
                       image=image_in_label,
                       compound=tk.LEFT).pack(padx=30,pady=40)





root.mainloop()