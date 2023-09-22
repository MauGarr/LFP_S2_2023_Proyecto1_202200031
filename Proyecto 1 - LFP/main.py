from tkinter import *
from tkinter import Menu, filedialog
from tkinter import messagebox

# Funciones para las opciones del menú Archivo
def abrir_archivo():
    archivo = filedialog.askopenfilename(
        initialdir= "./",
        filetypes = (
            ("Archivos JSON", "*.json"),
            ("Todos los archivos",  "*.*")
        )
    )
    
    if archivo:
        with open(archivo, 'r', encoding='utf-8') as file:
            texto.delete(1.0, END)
            texto.insert(END, file.read())

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".json")
    if archivo:
        with open(archivo, 'w') as file:
            file.write(texto.get(1.0, END))

def guardar_como_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".json")
    if archivo:
        with open(archivo, 'w') as file:
            file.write(texto.get(1.0, END))

def salir():
    salir = messagebox.askquestion("Salir", "¿Desea salir del programa?")
    if salir == 'yes':
        ventana.quit()

# Función para mostrar el menú Archivo
def mostrar_menu_archivo(event):
    menu_archivo.post(event.x_root, event.y_root)

# Crea la ventana principal
ventana = Tk()
ventana.title("Analizador Léxico")
ventana.iconbitmap("spiderman.ico")
ventana.geometry("600x400")

# Crea el marco azul en la parte superior donde se encuentran los botones
marco_superior = Frame(ventana, bg="blue", height=10)
marco_superior.pack(fill="x")

# Crea el área de trabajo con fondo blanco
texto = Text(ventana, bg="white")
texto.pack(pady=15, padx= 15, fill="both", expand=True)

# Crea el menú para la opción Archivo
menu_archivo = Menu(ventana, tearoff= 0)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)
menu_archivo.add_command(label="Guardar como", command=guardar_como_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
menu_archivo.config(background= "black", foreground= "white", font=("Arial", 11, "italic"))

# Creando el menú con botones
boton_archivo = Button(marco_superior, text="Archivo", bg="black", fg="white", font=("Arial", 11))
boton_archivo.pack(side="left", padx=10, pady=5)
boton_archivo.bind("<Button-1>", mostrar_menu_archivo)   

boton_analizar = Button(marco_superior, text="Analizar", bg="black", fg="white", font=("Arial", 11))
boton_analizar.pack(side="left", padx=11, pady=5)

boton_Errores = Button(marco_superior, text="Errores", bg="black", fg="white", font=("Arial", 11))
boton_Errores.pack(side="left", padx=12, pady=5)

boton_Reporte = Button(marco_superior, text="Reporte", bg="black", fg="white", font=("Arial", 11))
boton_Reporte.pack(side="left", padx=13, pady=5)

# Ejecuta la ventana
ventana.mainloop()













