import tkinter as tk

def mostrar_ventana2():
    ventana1.withdraw()
    ventana2.deiconify()

def regresar():
    ventana2.withdraw()
    ventana1.deiconify()

ventana1 = tk.Tk()
label1 = tk.Label(ventana1, text= "ESTA ES MI VENTANA")
ventana1.geometry("600x400")
ventana1.config(bg="#F14444")

label1.pack()
btn1=tk.Button(ventana1, text= "ir a ventana 2", command=mostrar_ventana2)
btn1.pack()

ventana2 = tk.Tk()
label2 = tk.Label(ventana2, text= "ESTA ES MI VENTANA 2")
ventana2.geometry("600x400")
ventana2.config(bg="#F14444")

label2.pack()
btn2=tk.Button(ventana2, text= "ir a ventana 1", command=regresar)
btn2.pack()

ventana2.withdraw()

ventana1.mainloop()