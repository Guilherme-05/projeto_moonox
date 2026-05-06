import random

simbolos = ["🎰","🎉","🎲","💎"]
saldo = 20.0

print("= = = = = = Cassino Senai = = = = = =")
while saldo >= 2:
    input("\nPressione Enter para girar (Custa R$2)")
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
