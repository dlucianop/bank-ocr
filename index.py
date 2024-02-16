import tkinter as tk
from tkinter import filedialog
import os
import re

def index():
    ventana = tk.Tk()
    ventana.title("Bank OCR")
    ventana.geometry("400x300")
    btn_seleccionar_archivo = tk.Button(ventana, text="Seleccionar Archivo", command=openFile)
    btn_seleccionar_archivo.pack(pady=10)

    ventana.mainloop()

def openFile():
    dir_actual = os.path.dirname(os.path.realpath(__file__))
    archivo = filedialog.askopenfilename(initialdir=dir_actual, title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if archivo:
        conversion_first_h(archivo)

def conversion_first_h(archivo):
    with open(archivo, 'r') as file:
        num_cuenta = []
        for linea in file:
            num_cuenta.append(re.split(r'(\s+)', linea))
            
            if len(num_cuenta) == 4:
                print(num_cuenta)
                numeration(num_cuenta)
                num_cuenta = []

def numeration(cuenta):
    """
    [0][0] [0][1] [0][2]
    [1][0] [1][1] [1][2]
    [2][0] [2][1] [2][2]"""
    for fila, lista in enumerate(cuenta):
        for columna, elemento in enumerate(lista):
            print(f"Elemento '{elemento}' en la posición ({fila}, {columna})")

def validation_second_h():
    pass

def verification_third_h():
    pass

index()