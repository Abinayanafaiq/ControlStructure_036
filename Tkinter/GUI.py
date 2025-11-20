import tkinter as tk 
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.geometry("100x100")
root.title("APLIKASI PRODI PILIHAN")
label_judul = tk.Label(root, text="APLIKASI PRODI PILIHAN")
label_judul.pack()
def HelloBack(): 
    msg=messagebox.showinfo("Prodi Teknologi Informasi","Prodi Teknologi Informasi")






button = Button(root, text="Click me", command=HelloBack)
button.place(x=50,y=90)

anu = tk.Label(root, text="nilai 1:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 2:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 3:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 4:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 5:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 6:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 7:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 8:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 9:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()

anu = tk.Label(root, text="nilai 10:")
anu.pack()

anu2 = tk.Entry(root, bd=5)
anu2.pack()
root.mainloop()