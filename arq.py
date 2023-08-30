import random 

def jogo_de_adivinhacao():
    num_aleat = random.randint(1, 50)
    tentativas = 0

    print("Vamos jogar Acerte o Número!")
    print("Pensei em um número de 1 a 50, tente adivinhar!")

    while True:
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1

        if tentativa < num_aleat:
            print("Tente um número maior.")
        elif tentativa > num_aleat:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

jogo_de_adivinhacao()