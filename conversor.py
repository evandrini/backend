import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        cm = float(entrada_cm.get())
        metros = cm / 100
        label_resultado.config(text=f"{cm} cm = {metros} metros")
        
    except ValueError:
        messagebox.showerror("Número inválido", "Por favor, insira um valor válido.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Conversor de Centímetros para Metros")

tk.Label(janela, text="Digite o valor em centímetros:").pack(pady=10)
entrada_cm = tk.Entry(janela, width=10)
entrada_cm.pack()

tk.Button(janela, text="Converter", command=converter).pack(pady=10)
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()
