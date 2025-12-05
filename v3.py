#importamos la biblioteca
import tkinter as tk
from tkinter import ttk

#configuracion de todos los frames 
color_fondo = "#7988BB"
color_menu = "#1D2D52E8"
color_texto = "#FFFFFF"
fuente_titulo =("Arial",16,"bold")
fuente_texto =("Arial", 12)

#ventana principal
root=tk.Tk()
root.title("Software de deteccion de addiciones")
root.geometry("900x500")
root.config(bg=color_fondo)

#configuramos el frame del menú lateral
menu_frame=tk.Frame(root,bg=color_menu,width=200)
menu_frame.pack(side="left", fill="y")

#contenido del frame de la derecha
contenido_frame=tk.Frame(root,bg=color_fondo)
contenido_frame.pack(side="right", fill="both", expand=True)
#funcion para cambiar a las siguientes ventanas

def mostrar_pagina(nombre):
    for witget in contenido_frame.winfo_children():
        witget.destroy()
        paginas[nombre]()

#paginas bienvenida
def pagina_bienvenida():
    tk.Label(contenido_frame, text="aqui va el titulo de mi pagina", font=fuente_titulo, bg=color_fondo).pack(pady=30)
    tk.Label(contenido_frame, text="aqui va el contenido de la página", bg=color_fondo,font=fuente_texto).pack(pady=10)
#pagina de registro

def pagina_registro():
    tk.Label(contenido_frame, text="Registro de ususario", font=fuente_texto).pack()
    tk.Entry(contenido_frame, width=40).pack(pady=5)

#pagina del test
def pagina_test():
    tk.Label(contenido_frame, text="test de bienestar", font=fuente_titulo, bg=color_fondo).pack(pady=20)
    tk.Label(contenido_frame, text="Responde las siguientes preguntas para conocer tu nivel de bienestar", wraplength=600, bg=color_fondo).pack(pady=10)
    ttk.Button(contenido_frame, text="Iniciar test").pack(pady=20)


#diccionario de las paginas

paginas = {
"bienvenida": pagina_bienvenida,
"registro": pagina_registro,
"test": pagina_test,
}

#botones de menú lateral
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x",pady=5, padx=10)

ttk.Button(menu_frame, text="salir", command=root.quit).pack(side="bottom", pady=10)
#mostrar pagina inicial
pagina_bienvenida()

root.mainloop()
