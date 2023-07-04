import os
import tkinter as tk
os.chdir("m3/tkinter")

def click():
    print("Stisnuo si me")

root = tk.Tk()

root.title("Drugi GUI")
root.geometry("600x400")


button = tk.Button(root, text="Gumb")




button.pack()
button_click = tk.Button(root, text="Stisni me!", command=click).pack(padx=10,pady=5)

btn_image = tk.PhotoImage(file="python.gif")
button_image = tk.Button(root, text="Gumb sa slikom",
                        image=btn_image,
                        compound=tk.LEFT,
                        relief=tk.GROOVE,
                        command=click,
                        state=tk.ACTIVE,
                        ).pack(padx=10,pady=10)


root.mainloop()