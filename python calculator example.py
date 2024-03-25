from tkinter import *
from tkinter import messagebox
import string
from struct import pack
import tkinter
from tkinter.ttk import Button

class Ventana:

    def __init__(self,inter):
        self.interfaz=inter 
        self.interfaz.geometry("500x500")
        self.interfaz.title("PROBANDO")
        self.num1 = IntVar()
        self.num2 = IntVar()
        self.dibujarVentana()

    def dibujarVentana(self):
        tkinter.Label(self.interfaz,text="Escribe un numero").place(x=10,y=10)
        tkinter.Entry(self.interfaz,textvariable=self.num1).place(x=20,y=30)
        tkinter.Entry(self.interfaz,textvariable=self.num2).place(x=20,y=80)
        tkinter.Button(self.interfaz,command=self.sumar,text="Sumar").place(x=50,y=110)
    def sumar(self):
        s=self.num1.get()+self.num2.get()
        messagebox.showinfo("Resultado","El Resultado es: "+str(s))      

obj = Ventana(Tk())
obj.interfaz.mainloop()
    

