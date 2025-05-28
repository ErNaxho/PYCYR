import tkinter as tk
from tkinter import messagebox

def suma():
    try:
        resultado = float(entry1.get()) + float(entry2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def resta():
    try:
        resultado = float(entry1.get()) - float(entry2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicacion():
    try:
        resultado = float(entry1.get()) * float(entry2.get())
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def division():
    try:
        divisor = float(entry2.get())
        if divisor != 0:
            resultado = float(entry1.get()) / divisor
            label_resultado.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

ventana = tk.Tk()
ventana.title("Calculadora Básica")

tk.Label(ventana, text="Número 1:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(ventana)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Número 2:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(ventana)
entry2.grid(row=1, column=1, padx=10, pady=10)

tk.Button(ventana, text="Sumar", command=suma).grid(row=2, column=0, padx=10, pady=10)
tk.Button(ventana, text="Restar", command=resta).grid(row=2, column=1, padx=10, pady=10)
tk.Button(ventana, text="Multiplicar", command=multiplicacion).grid(row=3, column=0, padx=10, pady=10)
tk.Button(ventana, text="Dividir", command=division).grid(row=3, column=1, padx=10, pady=10)

label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()