import tkinter as tk
from tkinter import END, messagebox, ttk
# M1-p3_design 


class datos: 
    def __init__(self):
        self.nombre=""
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre  

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.nombre=""
        self.config(width=200,height=200)
        self.title("Practica 1")
        self.label_nombre=tk.Label(self,text="Ingrese Nombre:")
        self.label_nombre.place(x=60,y=0)
        self.entry_nombre=tk.Entry(self,width=20)
        self.entry_nombre.place(x=60,y=40)
        self.boton_mostrar=tk.Button(self,text="Mostrar",command=lambda:self.mostrar())
        self.boton_mostrar.place(x=60,y=80)

    def mostrar(self):
        salida=""
        self.ob = datos()
        self.ob.setNombre(self.entry_nombre.get())
        salida=self.ob.getNombre()
        messagebox.showinfo(title="Datos",message=salida)
        
if __name__=="__main__":
    app=App()
    app.mainloop()
        
        
class datos: 
    def __init__(self):
        self.nombre=""
    def setNombre(self,nombre):
        self.nombre=nombre
    def getNombre(self):
        return self.nombre