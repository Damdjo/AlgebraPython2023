import os
import tkinter as tk
os.chdir("m3/tkinter")

root = tk.Tk()
root.title('Treca sreca')
root.geometry('600x400')

btn_image = tk.PhotoImage(file="python.gif")
button_image = tk.Button(root, text="Gumb sa slikom",
                         image= btn_image,
                         compound=tk.LEFT).place(x=150,y=75)

label = tk.Label(root, text="Neki label")
label.place(x=150,y=120)

root.mainloop()