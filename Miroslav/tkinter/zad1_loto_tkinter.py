import tkinter as tk
import random

def eurojackpot_brojeve():
    glavni_br=random.sample(range(1,51), 5)
    dodatni_br=random.sample(range(1,13), 2)
    glavni_br = sorted(glavni_br)
    dodatni_br = sorted(dodatni_br)
    glavni_label.config(text="Izvučeni glavni brojevi su: " + ', '.join(map(str, glavni_br)))
    dodatni_label.config(text="a dodatni brojevi: " + ', '.join(map(str, dodatni_br)))

root = tk.Tk()
root.title('EuroJackpot')
root.geometry('600x400')

image_in_label=tk.PhotoImage(file='HL.png').subsample(2)
label_image=tk.Label(root,
                     compound=tk.CENTER,
                     image=image_in_label)
label_image.pack(padx=75, pady=10)

btn_image=tk.PhotoImage(file='EJ.png').subsample(2)
button_image = tk.Button(root,
                         image=btn_image,
                         command=eurojackpot_brojeve,
                         compound=tk.CENTER)
button_image.pack(pady=10)

glavni_label = tk.Label(root, text='', font=('Arial', 12, 'bold italic'))
glavni_label.pack()

dodatni_label = tk.Label(root, text='', font=('Arial', 12, 'bold italic'))
dodatni_label.pack()

root.mainloop()
