import os
import random

simbolos = ["🎰","🎉","🎲","💎"]
saldo = 20.0

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print("= = = = = = Cassino Senai = = = = = =")
while saldo >= 2:
    input("\nPressione Enter para girar (Custa R$2)\n")
    limpar_tela()
    saldo -= 2

    resultado = [random.choice(simbolos) for _ in range(3)]
    print(" | ".join(resultado))

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        print(f" JACKPOT!!! Você ganhou R$ {premio}!")

    else:
        print("Não foi dessa vez...")

    print(f"Saldo Atual: R$ {saldo: .2f}")

    if saldo == 0.00:
        pergunta = input("Gostaria de Colocar mais saldo? S/N\n")
        if pergunta == "S" or pergunta == "s":
            inserir = float(input("Qual valor gostaria de inserir?\n"))
            saldo = saldo + inserir
        
        else:
            print("\nObrigado por jogar!")



