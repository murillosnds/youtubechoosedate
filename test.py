import webbrowser
import tkinter as tk
from tkinter import messagebox

def buscar_videos():
    pesquisa = entry_pesquisa.get()
    ano_inicial = entry_ano_inicial.get()
    ano_final = entry_ano_final.get()

    if not pesquisa or not ano_inicial or not ano_final:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")
        return

    google = (f"https://www.google.com/search?q=site%3Ayoutube.com+{pesquisa}&tbm=vid&"
              f"source=lnt&tbs=cdr%3A1%2Ccd_min%3A1%2F01%2F{ano_inicial}%2C"
              f"cd_max%3A1%2F1%2F{ano_final}&tbm=vid")
    
    webbrowser.open(google)

# Configurando a interface gráfica
root = tk.Tk()
root.title("Busca de Vídeos no YouTube")

tk.Label(root, text="Pesquisa:").grid(row=0, column=0, padx=10, pady=10)
entry_pesquisa = tk.Entry(root)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Ano Inicial:").grid(row=1, column=0, padx=10, pady=10)
entry_ano_inicial = tk.Entry(root)
entry_ano_inicial.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Ano Final:").grid(row=2, column=0, padx=10, pady=10)
entry_ano_final = tk.Entry(root)
entry_ano_final.grid(row=2, column=1, padx=10, pady=10)

button_buscar = tk.Button(root, text="Buscar Vídeos", command=buscar_videos)
button_buscar.grid(row=3, columnspan=2, pady=20)

root.mainloop()
