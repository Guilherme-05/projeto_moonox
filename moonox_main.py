import tkinter as tk
from tkinter import ttk

import random

simbolos = ["🎭","🎁","🎃","💎","🎲"]
saldo = 20.0
custo_giro = 2

def main():
    root = tk.Tk()
    root.title("Moonox - Projeto") # Título da Janela.
    root.geometry("720x400") # Tamanho da Janela.
    root.resizable(True, True) # Redimensionar a Janela livremente.

    label = ttk.Label(root,
        text="Janela Principal",
        font=("TkDefaultFont", 20))
    
    label.pack(expand=True)

    def nickel():
        cnickel = tk.Tk()
        cnickel.title("🎰 Caça Nickel")
        cnickel.geometry("720x400")
        cnickel.resizable(True, True)

        global saldo
        if saldo < custo_giro:
            resultado_label.config(text="Saldo insuficiente!", fg="red")
            return
        
        saldo -= custo_giro

        resultado = [random.choice(simbolos) for _ in range(3)]

        slot1.config(text=resultado[0])
        slot1.config(text=resultado[1])
        slot1.config(text=resultado[2])

        if resultado[0] == resultado[1] == resultado[2]:
            premio = 20
            saldo += premio
            resultado_label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
        else:
            resultado_label.config(text="😥 Tente novamente...", fg="black")
        
        saldo_label.config(text=f"Saldo: R$ {saldo: .2f}")



    btn = ttk.Button(root,
        text = "Open",
        command = nickel)
    
    btn.pack(side="left",
             pady=15,
             padx=25)
    
    btn2 = ttk.Button(root,
        text = "Leave",
        command = root.destroy)
    
    btn2.pack(side="left",
              pady=15,
              padx=10)
    
    

    root.mainloop()



if __name__ == "__main__":
    main()