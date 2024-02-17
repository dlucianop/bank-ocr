import tkinter as tk
from tkinter import filedialog
import os
import re
from numeros import representaciones

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
        indice = 0
        for linea in file:
            indice += 1
            if indice % 4 == 0:
                continue
            num_cuenta.append(linea)
            if len(num_cuenta) == 3:
                encontrar_coincidencia(num_cuenta, representaciones)
                num_cuenta = []
            print()
            print()
                
    print("Done")



def encontrar_coincidencia(num_cuenta, representaciones):
    digitos = [[] for _ in range(9)]
    for fila in num_cuenta:
        grupo_actual = []
        for indice, columna in enumerate(fila):
            if (indice + 1) % 4 != 0:
                grupo_actual.append(columna)
            if len(grupo_actual) == 3:
                matriz_indice = (indice + 1) // 4
                digitos[matriz_indice].append(grupo_actual)
                grupo_actual = [] 

    for indice, digito in enumerate(digitos):
        digito_format = [''.join(row) for row in digito]
        coincidencia = False
        for key, value in representaciones.items():
            if len(digito_format) == 2:
                digito_format.insert(0, '   ')
            if value == digito_format:
                print("Digito coincidente {}".format(key))
                coincidencia = True
                break
        if coincidencia == False:
            print("Digito no coincidente {}".format("?"))


def validation_second_h():
    pass

def verification_third_h():
    pass

index()