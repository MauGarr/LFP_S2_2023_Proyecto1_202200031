
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

# Crear la ventana
ventana = Tk()

ventana.title("Menú")
ventana.iconbitmap("spiderman.ico")
ventana.geometry("650x350")
ventana.resizable(True, True)

#Creando el menu
menu = Menu(ventana)
ventana.config(menu=menu, bg= "light blue")

def cargar_archivo():
    filename = askopenfilename()
    img = Image.open(filename)
    new_img = img.resize((300, 200))
    render = ImageTk.PhotoImage(new_img)
    img1 = Label(ventana, image = render)
    img1.image = render
    img1.place(x=400, y=210)

def salir():
    salir = messagebox.askquestion("Salir", "¿Desea salir del programa?")
    if salir == 'yes':
        ventana.quit()

Archivo = Menu(menu, tearoff = 0)
Archivo.add_command(label = "Abrir", command = cargar_archivo)
Archivo.add_command(label = "Guardar")
Archivo.add_command(label = "Guardar como")
Archivo.add_separator()
Archivo.add_command(label = "Salir", command = salir)


Analizar = Menu(menu, tearoff = 0)

Errores = Menu(menu, tearoff = 0)
Reporte = Menu(menu, tearoff = 0)

menu.add_cascade(label = "Archivo", menu = Archivo)
menu.add_cascade(label = "Analizar", menu = Analizar)
menu.add_cascade(label = "Errores", menu = Errores)
menu.add_cascade(label = "Reporte", menu = Reporte)

# Ejecutar la ventana
ventana.mainloop()







# Botón de menu
# btn_menu= Button(ventana, text="Continuar", font = ("Courier", 14), bg = "white", fg = "black", command=verificar_credenciales)
# btn_menu.pack()














