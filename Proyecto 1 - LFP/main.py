import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as md
from tkinter import *
from tkinter import ttk
from analizador import *

dot_string = ''

class Interfaz():
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico")
        self.root.iconbitmap("spiderman.ico")
        self.root.geometry("600x400")
        self.root.configure(bg="medium orchid")
        self.archivo_actual = None

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

        btn_reporte = tk.Button(self.root, text="Reporte", command=self.reporte, padx=15, pady=10, bg="black", fg="white", font=("Arial", 11))
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
        if archivo != "":
            self.archivo_actual = archivo  # Establece la ruta del archivo actual
            self.root.title('Archivo actual - Ruta: ' + archivo)
            with open(archivo, "r") as file:
                contenido = file.read()
                self.textovacio.delete(1.0, tk.END)
                self.textovacio.insert(tk.END, contenido)

    def guardar_archivo(self):
        if self.archivo_actual is not None:
            if md.askyesno("Confirmación", "¿Deseas guardar los cambios?"):
                try:
                    with open(self.archivo_actual, 'w') as f:
                        content = self.textovacio.get('1.0', tk.END)
                        f.write(content)
                    self.textovacio.edit_modified(0)
                except Exception as e:
                    md.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
        else:
            messagebox.showerror("Error", "No se ha abierto ningún archivo para guardar.")

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
            contenido = self.textovacio.get(1.0, tk.END)  # Obtener el contenido del cuadro de texto
            instrucciones = instruccion(contenido)  # Analizar el contenido
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
        messagebox.showinfo("Se creo el Documento", "Se encontraron: " + str(noerror - 1) + " Errores")

    def reporte(self):
        global dot_string
        dot_string = 'digraph G {\n'
        dot_string += 'subgraph 0 {\n'
        dot_string += '  operaciones;\n'
        dot_string += '}\n'
        dot_string += 'subgraph A {\n'
        dot_string += '  Nodo1 [label="suma_"];\n'
        dot_string += '  Nodo2 [label=""];\n'
        dot_string += '  Nodo31 [label=""];\n'
        dot_string += '  Nodo1 -> Nodo2;\n'
        dot_string += '  Nodo1 -> Nodo31;\n'
        dot_string += '}\n'
        dot_string += 'subgraph B {\n'
        dot_string += '  Nodo4 [label="potencia_"];\n'
        dot_string += '  Nodo5 [label=""];\n'
        dot_string += '  Nodo51 [label=""];\n'
        dot_string += '  Nodo4 -> Nodo5;\n'
        dot_string += '  Nodo4 -> Nodo51;\n'
        dot_string += '}\n'
        dot_string += 'subgraph C {\n'
        dot_string += '  Nodo7 [label="resta_"];\n'
        dot_string += '  Nodo8 [label=""];\n'
        dot_string += '  Nodo81 [label=""];\n'
        dot_string += '  Nodo7 -> Nodo8;\n'
        dot_string += '  Nodo7 -> Nodo81;\n'
        dot_string += '}\n'
        dot_string += 'subgraph D {\n'
        dot_string += '  Nodo10 [label="seno_"];\n'
        dot_string += '  Nodo11 [label=""];\n'
        dot_string += '  Nodo10 -> Nodo11;\n'
        dot_string += '}\n'
        dot_string += 'subgraph E {\n'
        dot_string += '  Nodo12 [label=""];\n'
        dot_string += '  Nodo13 [label=""];\n'
        dot_string += '  Nodo131 [label=""];\n'
        dot_string += '  Nodo12 -> Nodo13;\n'
        dot_string += '  Nodo12 -> Nodo131;\n'
        dot_string += '}\n'
        dot_string += 'subgraph F {\n'
        dot_string += '  Nodo14 [label="multiplicacion_"];\n'
        dot_string += '  Nodo15 [label=""];\n'
        dot_string += '  Nodo151 [label=""];\n'
        dot_string += '  Nodo14 -> Nodo15;\n'
        dot_string += '  Nodo14 -> Nodo151;\n'
        dot_string += '}\n'
        dot_string += 'subgraph G {\n'
        dot_string += '  Nodo16 [label=""];\n'
        dot_string += '  Nodo17 [label=""];\n'
        dot_string += '  Nodo171 [label=""];\n'
        dot_string += '  Nodo16 -> Nodo17;\n'
        dot_string += '  Nodo16 -> Nodo171;\n'
        dot_string += '}\n'
        dot_string += "}\n"
        with open("resultados.dot", "w") as archivo:
            archivo.write(dot_string)
        os.system("dot -Tpng resultados.dot -o resultados.png")
        messagebox.showinfo("Generando gráfica...", "Se generó correctamente la gráfica :)")


    '''def reporte(self):
        global dot_string
        dot_string = ''
        dot_string = 'digraph G {\n'
        dot_string += "}\n"
        with open("resultados.dot", "w") as archivo:
            archivo.write(dot_string)
        os.system("dot -Tpng resultados.dot -o resultados.png")
        messagebox.showinfo("Generando gráfica...", "Se generó correctamente la gráfica :)")'''

if __name__ == "__main__":
    root = tk.Tk()
    interfaz = Interfaz(root)
    root.mainloop()
