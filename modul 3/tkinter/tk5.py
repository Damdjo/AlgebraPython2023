import os
import tkinter as tk
os.chdir("m3/tkinter")

root = tk.Tk()
root.title('Pokušaj sa gridom')

root.columnconfigure(0, weight=1, minsize=75)
root.columnconfigure(1, weight=1, minsize=190)

root.rowconfigure(0, weight=1, minsize=190)
root.rowconfigure(1, weight=1, minsize=90)

frame0 = tk.Frame(root, relief=tk.RAISED,
                  borderwidth=1)
frame0.grid(column=0, row=0, padx=15, pady=15)
label_frame0 = tk.Label(frame0,text="Labl0 Fr0").pack(padx=15, pady=15)

frame1 = tk.Frame(root, relief=tk.RAISED,
                  borderwidth=1)
frame1.grid(column=0, row=1, padx=15, pady=15)
label_frame0 = tk.Label(frame1,text="Labl1 Fr1").pack(padx=15, pady=15)

frame2 = tk.Frame(root, relief=tk.RAISED,
                  borderwidth=1)
frame2.grid(column=1, row=0, padx=15, pady=15)
label_frame0 = tk.Label(frame2,text="Labl1 Fr2").pack(padx=15, pady=15)

frame3 = tk.Frame(root, relief=tk.RAISED,
                  borderwidth=1)
frame3.grid(column=1, row=1, padx=15, pady=15)
label_frame0 = tk.Label(frame3,text="Labl3 Fr3").pack(padx=15, pady=15)








root.mainloop()