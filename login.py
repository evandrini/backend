import tkinter as tk
from tkinter import messagebox

def validar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de 6 caracteres.")
    elif '@' not in email:
        messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'.")
    else:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

# Criando a janela principal
root = tk.Tk()
root.title("Login")

# Criando os widgets
label_email = tk.Label(root, text="E-mail:")
label_senha = tk.Label(root, text="Senha:")
entry_email = tk.Entry(root)
entry_senha = tk.Entry(root, show="*")

button_login = tk.Button(root, text="Login", command=validar_login)

# Posicionando os widgets na interface usando grid
label_email.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
label_senha.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_email.grid(row=0, column=1, padx=10, pady=5)
entry_senha.grid(row=1, column=1, padx=10, pady=5)
button_login.grid(row=2, columnspan=2, padx=10, pady=10)

# Rodando o loop principal
root.mainloop()
