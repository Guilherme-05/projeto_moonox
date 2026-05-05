import tkinter as tk
from tkinter import ttk

import random

simbolos = ["🎭","🎁","🎃","💎","🎲"]
saldo = 20.0
custo_giro = 2

def main():
    root = tk.Tk()
    root.title("Moonox - Escolha sua Aba") # Título da Janela.
    root.geometry("720x400") # Tamanho da Janela.
    root.resizable(False, False) # Redimensionar a Janela livremente.

    label = ttk.Label(root,
        text="Escolha uma Opção",
        font=("TkDefaultFont", 20))
    
    label.pack(expand=True)

    def janela_nova():
        def mostrar_texto():
            texto = entrada.get()
            label_resultado.config(text=texto)
            entrada.delete(0, tk.END)  # limpa a barra

        aba = tk.Tk()
        aba.title("Moonox - Nova Janela")
        aba.geometry("720x400")
        aba.resizable(False, False)

        # Configurar grid (estrutura da tela)
        aba.grid_rowconfigure(0, weight=1)
        aba.grid_rowconfigure(1, weight=1)
        aba.grid_rowconfigure(2, weight=1)

        aba.grid_columnconfigure(0, weight=1)
        aba.grid_columnconfigure(1, weight=1)
        aba.grid_columnconfigure(2, weight=1)

        # 🔝 Texto no topo (centro)
        label_resultado = tk.Label(aba, text="", font=("Arial", 14))
        label_resultado.grid(row=0, column=1)

        # 🟡 Campo de entrada no meio
        entrada = tk.Entry(aba, width=40, font=("Arial", 14))
        entrada.grid(row=1, column=1)

        # 🔽 Botões embaixo
        botao = ttk.Button(aba, text="Mostrar", command=mostrar_texto)
        botao.grid(row=2, column=0, sticky="w", padx=30, pady=20)

        btn = ttk.Button(aba, text="Sair", command=aba.destroy)
        btn.grid(row=2, column=2, sticky="e", padx=30, pady=20)

    def futuro():
        desen = tk.Tk()
        desen.title("Moonox - Projeto") # Título da Janela.
        desen.geometry("720x400") # Tamanho da Janela.
        desen.resizable(False, False) # Redimensionar a Janela livremente.

        label = ttk.Label(desen,
            text="Em Desenvolvimento!",
            font=("TkDefaultFont", 20))
    
        label.pack(expand=True)

        btn = ttk.Button(desen,
            text = "Sair",
            command = desen.destroy)
    
        btn.pack(side="left",
              pady=15,
              padx=30)

    def criar_jogo():
        global slot1, slot2, slot3, resultado_label, saldo_label

        janela = tk.Tk()
        janela.title("🎰 Caça Níquel")
        janela.geometry("350x250")
        janela.resizable(False, False)

        tk.Label(janela, text="🎰 Caça Níquel", font=("Arial", 16, "bold")).pack(pady=10)

        frame_slots = tk.Frame(janela)
        frame_slots.pack(pady=10)

        slot1 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
        slot1.pack(side="left", padx=10)

        slot2 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
        slot2.pack(side="left", padx=10)

        slot3 = tk.Label(frame_slots, text="❓", font=("Arial", 30))
        slot3.pack(side="left", padx=10)

        resultado_label = tk.Label(janela, text="Clique para girar")
        resultado_label.pack()

        saldo_label = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}")
        saldo_label.pack()

        tk.Button(janela, text="Girar", command=girar).pack(pady=10)

        janela.mainloop()


    def girar():
        global saldo

        if saldo < custo_giro:
            resultado_label.config(text="Saldo insuficiente!", fg="red")
            return

        saldo -= custo_giro

        resultado = [random.choice(simbolos) for _ in range(3)]

        slot1.config(text=resultado[0])
        slot2.config(text=resultado[1])
        slot3.config(text=resultado[2])

        if resultado[0] == resultado[1] == resultado[2]:
            premio = 20
            saldo += premio
            resultado_label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
        else:
            resultado_label.config(text="😥 Tente novamente...", fg="black")

        saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")



    btn = ttk.Button(root,
        text = "Janela",
        command = janela_nova)
    
    btn.pack(side="left",
             pady=15,
             padx=40)
    
    btn2 = ttk.Button(root,
        text = "Nickel",
        command = criar_jogo)
    
    btn2.pack(side="left",
             pady=15,
             padx=30)
    
    btn3 = ttk.Button(root,
        text = "Futuro",
        command = futuro)
    
    btn3.pack(side="left",
             pady=15,
             padx=30)
    
    btn4 = ttk.Button(root,
        text = "Futuro",
        command = futuro)
    
    btn4.pack(side="left",
              pady=15,
              padx=30)
    
    btn5 = ttk.Button(root,
        text = "Sair",
        command = root.destroy)
    
    btn5.pack(side="left",
              pady=15,
              padx=30)
    
    

    root.mainloop()



if __name__ == "__main__":
    main()