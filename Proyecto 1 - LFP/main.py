import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter import ttk
from analizador import *

class Interfaz():
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")
        self.root.iconbitmap("spiderman.ico")
        self.root.geometry("600x400")
        self.root.configure(bg="medium orchid")

        # Cuadro de texto
        self.textovacio = ScrolledText(self.root, bg="white", wrap=tk.WORD, padx=5, pady=5, font=("Arial", 12))
        self.textovacio.grid(row=1, column=0, columnspan=4, padx=50, pady=50)
        self.lineaActual = 1

        # Botón Archivo
        self.btn_archivo = tk.Button(self.root, text="Archivo", command=self.mostrar_menu_archivo, padx=15, pady=10, bg="black", fg="white", font=("Arial", 11))
        self.btn_archivo.grid(row=0, column=0, pady=(30, 0))

        # Botones en la parte superior
        btn_analizar = tk.Button(self.root, text="Analizar", command=self.analizar, padx=15, pady=10, bg="black", fg="white", font=("Arial", 11))
        btn_analizar.grid(row=0, column=1, pady=(30, 0))

        btn_errores = tk.Button(self.root, text="Errores", command=self.errores, padx=15, pady=10, bg="black", fg="white", font=("Arial", 11))
        btn_errores.grid(row=0, column=2, pady=(30, 0))

        btn_reporte = tk.Button(self.root, text="Reporte", padx=15, pady=10, bg="black", fg="white", font=("Arial", 11))
        btn_reporte.grid(row=0, column=3, pady=(30, 0))

        # Menú Archivo 
        self.menu_archivo = tk.Menu(self.root, tearoff=0, bg="black", fg="white")
        self.menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        self.menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        self.menu_archivo.add_command(label="Guardar Como", command=self.guardar_como)
        self.menu_archivo.add_separator()
        self.menu_archivo.add_command(label="Salir", command=self.salir)
        self.menu_archivo.config(font=("Arial", 11, "italic"))

    def mostrar_menu_archivo(self):
        # Muestra el menú "Archivo" como un menú emergente al hacer clic en el botón Archivo
        x, y, _, _ = self.btn_archivo.bbox("insert")
        self.menu_archivo.post(self.btn_archivo.winfo_rootx() + x, self.btn_archivo.winfo_rooty() + y)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.JSON")])
        self.root.title('Archivo actual-Ruta - ' + archivo)
        if archivo != "":
            with open(archivo, "r") as file:
                contenido = file.read()
                self.textovacio.delete(1.0, tk.END)
                self.textovacio.insert(tk.END, contenido)
        self.data = self.textovacio.get(1.0, tk.END)     

    def guardar_archivo(self):
        try:
            path = self.root.title().split('-')[1][1:]   
        except:
            path=""
        
        if path != '':        
            with open(path, 'w') as f:
                content = self.textovacio.get('1.0', tk.END)
                f.write(content)  
        self.textovacio.edit_modified(0)

    def guardar_como(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            contenido = self.textovacio.get(1.0, tk.END)
            with open(archivo, 'w') as file:
                file.write(contenido)
            messagebox.showinfo("Archivo Guardado Correctamente ", "El archivo se guardo correctamente")

    def salir(self):
        salir = messagebox.askquestion("Salir", "¿Desea salir del programa?")
        if salir == 'yes':
            self.root.quit()

    def analizar(self):
        try:
            instrucciones = instruccion(self.data)
            respuestas = operar_()
            Resultados = ''
            Operacion = 1
            configuracion = 1
            salto = "\n"
            for respuesta in respuestas:
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                    Resultados += str(f'Operacion {Operacion} es: {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n')
                    print(respuesta.operar(None))
                    Operacion += 1
            messagebox.showinfo("Analizando...", Resultados)
        except:
            messagebox.showinfo("Error", "Ha ocurrido un error al analizar el documento")

    def errores(self):
        lista_errores = getErrores()
        noerror = 1
        archivo = open('Errores.txt', 'w', encoding="utf-8")
        archivo.write('{\n')
        archivo.write('\t"errores": [\n')
        for miserrores in lista_errores:
            error = miserrores.operar(noerror)
            noerror += 1
            print (error)
            archivo.write(error)
        archivo.write('\t\t]\n')
        archivo.write('}')
        messagebox.showinfo("Se creo el Documento", "Se encontraron: " + str(noerror - 1) + "Errores")

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()
