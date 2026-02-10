# M1-p3_design
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class CompiladorIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Diseño de Compilador Kotlin")
        self.root.geometry("800x600")

        # --- Variables de control ---
        self.archivo_actual = None

        # --- Creación de Widgets ---
        self.crear_menu()
        self.crear_area_edicion()
        self.crear_consola()

    def crear_menu(self):
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # 1. Menú Archivo
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(label="Abrir", command=self.abrir_archivo)
        menu_archivo.add_command(label="Guardar", command=self.guardar_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Limpiar pantalla", command=self.limpiar_pantalla)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Cerrar", command=self.root.quit)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        # 2. Menú Editar (Básico)
        menu_editar = tk.Menu(barra_menu, tearoff=0)
        menu_editar.add_command(label="Deshacer", command=lambda: self.editor.edit_undo())
        menu_editar.add_command(label="Rehacer", command=lambda: self.editor.edit_redo())
        # Opción extra solicitada: Insertar void main
        menu_editar.add_separator()
        menu_editar.add_command(label="Insertar 'void main'", command=self.insertar_main)
        barra_menu.add_cascade(label="Editar", menu=menu_editar)

        # 3. Menú Compiladores (Fases)
        menu_compiladores = tk.Menu(barra_menu, tearoff=0)
        fases = [
            "Análisis Léxico", 
            "Análisis Sintáctico", 
            "Análisis Semántico", 
            "Generación de Código Intermedio", 
            "Generación de Código Objeto"
        ]
        for fase in fases:
            menu_compiladores.add_command(label=fase, command=lambda f=fase: self.log_consola(f"Ejecutando: {f}..."))
        barra_menu.add_cascade(label="Compiladores", menu=menu_compiladores)
        
        # 4. Menú Variables (Tipos)
        menu_variables = tk.Menu(barra_menu, tearoff=0)
        menu_tipos = tk.Menu(menu_variables, tearoff=0)
        
        # Diccionario de tipos y sus librerías asociadas (si aplica)
        self.tipos_config = {
            "int": None,          # int es nativo, no suele requerir include específico extra
            "float": None,
            "String": "string.h"  # Requiere string.h
        }

        for tipo, lib in self.tipos_config.items():
            menu_tipos.add_command(label=tipo, command=lambda t=tipo, l=lib: self.insertar_variable(t, l))
        
        menu_variables.add_cascade(label="Tipos", menu=menu_tipos)
        barra_menu.add_cascade(label="Variables", menu=menu_variables)

        # 5. Menú Ejecutar
        menu_ejecutar = tk.Menu(barra_menu, tearoff=0)
        menu_ejecutar.add_command(label="Ejecutar Código", command=lambda: self.log_consola("Iniciando ejecución..."))
        barra_menu.add_cascade(label="Ejecutar", menu=menu_ejecutar)

        # 6. Menú Ayuda (Librerías)
        menu_ayuda = tk.Menu(barra_menu, tearoff=0)
        menu_librerias = tk.Menu(menu_ayuda, tearoff=0)
        
        librerias = ["stdio.h", "conio.h", "math.h", "string.h", "stdlib.h", "ctype.h"]
        for lib in librerias:
            menu_librerias.add_command(label=lib, command=lambda l=lib: self.insertar_libreria(l))
            
        menu_ayuda.add_cascade(label="Librerías", menu=menu_librerias)
        menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Ayuda", "Compilador v1.0\nEstudiante: Erick Mancillas"))
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    def crear_area_edicion(self):
        # Frame principal para editor
        frame_editor = tk.Frame(self.root)
        frame_editor.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        label = tk.Label(frame_editor, text="Editor de Código Fuente", anchor="w")
        label.pack(fill=tk.X)

        self.editor = scrolledtext.ScrolledText(frame_editor, wrap=tk.WORD, font=("Consolas", 12), undo=True)
        self.editor.pack(fill=tk.BOTH, expand=True)

    def crear_consola(self):
        # Frame inferior para consola
        frame_consola = tk.Frame(self.root, height=150)
        frame_consola.pack(fill=tk.X, side=tk.BOTTOM, padx=5, pady=5)
        
        label = tk.Label(frame_consola, text="Consola / Salida", anchor="w")
        label.pack(fill=tk.X)

        self.consola = scrolledtext.ScrolledText(frame_consola, height=8, bg="#f0f0f0", font=("Consolas", 10))
        self.consola.pack(fill=tk.BOTH, expand=True)
        self.consola.config(state=tk.DISABLED) # Solo lectura

    # --- Funcionalidades Lógicas ---

    def insertar_libreria(self, nombre_lib):
        """Inserta el include de la librería en la posición actual del cursor."""
        texto_include = f"#include <{nombre_lib}>\n"
        self.editor.insert(tk.INSERT, texto_include)
        self.log_consola(f"Librería agregada: {nombre_lib}")

    def insertar_variable(self, tipo, libreria_necesaria):
        """
        Inserta el tipo de variable y, si se requiere, agrega la librería
        automáticamente al inicio del archivo si no existe.
        """
        # 1. Insertar el tipo en el cursor
        self.editor.insert(tk.INSERT, f"{tipo} ")
        
        # 2. Verificar e insertar librería si es necesario
        if libreria_necesaria:
            contenido = self.editor.get("1.0", tk.END)
            include_str = f"#include <{libreria_necesaria}>"
            
            if include_str not in contenido:
                self.editor.insert("1.0", include_str + "\n")
                self.log_consola(f"Librería requerida agregada automáticamente: {libreria_necesaria}")
            
    def insertar_main(self):
        estructura_main = "\nvoid main() {\n\n\t// Escribe tu código aquí\n\n}\n"
        self.editor.insert(tk.INSERT, estructura_main)

    def limpiar_pantalla(self):
        self.editor.delete("1.0", tk.END)
        self.log_consola("Pantalla limpia.")

    def log_consola(self, mensaje):
        self.consola.config(state=tk.NORMAL)
        self.consola.insert(tk.END, ">> " + mensaje + "\n")
        self.consola.see(tk.END)
        self.consola.config(state=tk.DISABLED)

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(defaultextension=".c", filetypes=[("Archivos C/C++", "*.c *.cpp"), ("Todos", "*.*")])
        if ruta:
            try:
                with open(ruta, "r") as f:
                    contenido = f.read()
                self.editor.delete("1.0", tk.END)
                self.editor.insert("1.0", contenido)
                self.archivo_actual = ruta
                self.log_consola(f"Archivo abierto: {ruta}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")

    def guardar_archivo(self):
        if self.archivo_actual:
            try:
                with open(self.archivo_actual, "w") as f:
                    contenido = self.editor.get("1.0", tk.END)
                    f.write(contenido)
                self.log_consola(f"Guardado en: {self.archivo_actual}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            ruta = filedialog.asksaveasfilename(defaultextension=".c", filetypes=[("Archivos C/C++", "*.c *.cpp")])
            if ruta:
                self.archivo_actual = ruta
                self.guardar_archivo()

if __name__ == "__main__":
    root = tk.Tk()
    app = CompiladorIDE(root)
    root.mainloop()