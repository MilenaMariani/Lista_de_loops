import random

numero_computador = random.randint(1, 10)

tentativas = 3

while tentativas > 0:
    print(f"Você tem {tentativas} tentativa(s).")
    resp_usuario = int(input("Tente adivinhar o número: "))

    if resp_usuario == numero_computador:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1

print(f"O número era: {numero_computador}!")