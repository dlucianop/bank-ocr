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
                numeros = encontrar_coincidencia(num_cuenta, representaciones)
                num_cuenta = []
                print(numeros)
            print()
            print()
                
    print("Done")

def encontrar_coincidencia(num_cuenta, representaciones):
    digitos = [[] for _ in range(9)]
    for fila in num_cuenta:
        grupo_actual = []
        for indice, columna in enumerate(fila):
            grupo_actual.append(columna)
            if (indice + 1) % 4 == 0:
                matriz_indice = (indice + 1) // 4 - 1
                digitos[matriz_indice].append(grupo_actual)
                grupo_actual = [] 

    for i, matriz in enumerate(digitos, 1):
        print(f"Digito {i}:")
        for grupo in matriz:
            print(''.join(grupo))
        print()

def validation_second_h():
    pass

def verification_third_h():
    pass

index()