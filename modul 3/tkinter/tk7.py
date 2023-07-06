import tkinter as tk

def zbroji():
    txt_entry_rezultat.delete(0, tk.END)
    prvi_broj = int(txt_entry_prvi_br.get()) 
    drugi_broj = int(txt_entry_drugi_br.get()) 
    rezultat = prvi_broj + drugi_broj
    txt_entry_rezultat.insert(tk.END,rezultat)

def handle_btn1_oduzmi(event):
    txt_entry_rezultat.delete(0, tk.END)
    rezultat = int(txt_entry_prvi_br.get()) - int(txt_entry_drugi_br.get())
    txt_entry_rezultat.insert(tk.END,rezultat)

root = tk.Tk()
root.title("Kalkulator")
root.geometry("600x400")

label_prvi_br = tk.Label(root, text= "Prvi broj")
label_prvi_br.grid(column=0, row=0, padx=5, pady=5)
txt_entry_prvi_br = tk.Entry(root, bd=3)
txt_entry_prvi_br.grid(column=1,row=0, padx=5, pady=5)

label_drugi_br = tk.Label(root, text= "Drugi broj")
label_drugi_br.grid(column=0, row=1, padx=5, pady=5)
txt_entry_drugi_br = tk.Entry(root, bd=3)
txt_entry_drugi_br.grid(column=1,row=1, padx=5, pady=5)

button_zbroji = tk.Button(root, text="Zbroji", command=zbroji)
button_zbroji.grid(column=0,row=2, padx=5, pady=5)

button_oduzmi = tk.Button(root, text="Oduzmi")
button_oduzmi.grid(column=1,row=2, padx=5, pady=5)
button_oduzmi.bind("<ButtonRelease-1>", handle_btn1_oduzmi)

label_rezultat = tk.Label(root, text="Rezultat")
label_rezultat.grid(column=0,row=3, padx=5, pady=5)
txt_entry_rezultat = tk.Entry(root)
txt_entry_rezultat.grid(column=1,row=3, padx=5, pady=5)



root.mainloop()
