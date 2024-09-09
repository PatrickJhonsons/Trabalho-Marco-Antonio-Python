import random


def determinar_vencedor(jogada_usuario, jogada_computador):
    if jogada_usuario == jogada_computador:
        return "Empate"
    elif (jogada_usuario == 0 and jogada_computador == 2) or \
         (jogada_usuario == 1 and jogada_computador == 0) or \
         (jogada_usuario == 2 and jogada_computador == 1):
        return "Você ganhou!"
    else:
        return "Você perdeu!"


def jogar():
    
    jogada_computador = random.randint(0, 2)

    
    jogada_usuario = int(input("Digite sua jogada (0 é Pedra, 1 é Papel, 2 é Tesoura): "))

    
    if jogada_usuario not in [0, 1, 2]:
        print("Número inválido. Digite 0 é Pedra, 1 é Papel ou 2 para Tesoura.")
        return

    
    jogadas = ["Pedra", "Papel", "Tesoura"]
    print(f"PC jogou: {jogadas[jogada_computador]}")
    print(f"Você jogou: {jogadas[jogada_usuario]}")

    
    resultado = determinar_vencedor(jogada_usuario, jogada_computador)
    print(resultado)


jogar()
