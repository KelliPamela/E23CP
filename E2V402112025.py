import tkinter as tk
from tkinter import ttk

# -------- CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#36C4C4"
COLOR_MENU = "#00B8CC"
COLOR_TEXTO = "#36C4C4"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# -------- VENTANA PRINCIPAL --------
root = tk.Tk()
root.title("Adicción a los videojuegos")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# -------- FRAME MENÚ LATERAL --------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# -------- FRAME CONTENIDO --------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# -------- FUNCIÓN PARA CAMBIAR DE PÁGINA --------
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# -------- PÁGINAS --------
def pagina_bienvenida():
    tk.Label(contenido_frame, 
             text="Bienvenido a Nuestro Test", 
             font=FUENTE_TITULO, 
             bg=COLOR_FONDO).pack(pady=30)
    
    tk.Label(contenido_frame, 
             text="Reconoce tu uso sobre los videojuegos.", 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, 
             text="Registro de Usuario", 
             font=FUENTE_TITULO, 
             bg=COLOR_FONDO).pack(pady=20)
    
    for campo in ["Nombre", "Edad", "Correo", "Género", "Télefono"]:
        tk.Label(contenido_frame, 
                 text=f"{campo}:", 
                 bg=COLOR_FONDO, 
                 font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)

def pagina_test():
    # --- Crear un canvas con scrollbar ---
    canvas = tk.Canvas(contenido_frame, bg=COLOR_FONDO, highlightthickness=0)
    scrollbar = ttk.Scrollbar(contenido_frame, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=COLOR_FONDO)

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # --- Contenido dentro del frame con scroll ---
    tk.Label(scroll_frame, 
             text="Test Adicción sobre los videojuegos", 
             font=FUENTE_TITULO, 
             bg=COLOR_FONDO).pack(pady=20)
    
    tk.Label(scroll_frame, 
             text="Responde las siguientes preguntas para conocer tu uso en los videojuegos.", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)

    # Simulamos muchas preguntas para probar el scroll
    tk.Label(scroll_frame, 
             text="¿Has gastado dinero en videojuegos sin pensarlo bien?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Te sientes ansioso o aburrido cuando no puedes jugar?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Has jugado hasta sentir cansancio extremo o dolor físico?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Juegas videojuegos como forma de escapar de tus problemas?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Sientes que necesitas cada vez más tiempo de juego para divertirte?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Tus padres o amigos te han dicho que juegas demasiado?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Piensas que los videojuegos son la actividad más importante en tu vida?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Te cuesta imaginar un día sin jugar videojuegos?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)

    tk.Label(scroll_frame, 
             text="¿Has descuidado tu alimentación o higiene por jugar demasiado?", 
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)
    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)
    tk.Label(scroll_frame, 
             text="¿Has tenido discusiones con tu familia por pasar mucho tiempo jugando?",
             wraplength=600, 
             bg=COLOR_FONDO, 
             font=FUENTE_TEXTO).pack(pady=10)

    ttk.Combobox(scroll_frame, values=["Nunca", "A veces", "Frecuentemente", "Siempre"]).pack(pady=5)


    tk.Button(scroll_frame, 
              text="Enviar respuestas").pack(pady=20)

# -------- DICCIONARIO DE PÁGINAS --------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test
}

# -------- BOTONES DE MENÚ LATERAL --------
for nombre in paginas:
    ttk.Button(menu_frame, 
               text=nombre, 
               command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, 
           text="Salir", 
           command=root.quit).pack(side="bottom", pady=10)

# -------- MOSTRAR PÁGINA INICIAL --------
pagina_bienvenida()

# -------- BUCLE PRINCIPAL --------
root.mainloop()