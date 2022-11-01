import random

def jogar():

    print("****************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("****************************")

    # numero_secreto = 42
    numero_secreto = round(random.randrange(1, 100))
    print(numero_secreto)
    tentativas = 0
    # rodada = 1
    pontos = 1000

    print("qual o nível de dificuldade?")
    print("(1) fácil (2) médio (3) difícil")

    nivel = int(input("defina o nível: "))

    if (nivel == 1):
        tentativas = 20;
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    # while (rodada <= tentativas): # executa enquanto tentativas for maior que zero
    for rodada in range(1, tentativas + 1):
        print("tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("adivinhe o número entre 1 e 100: ")  # input do usuário
        # type(chute_str) #tipagem da variável

        print("você digitou: ", chute_str)
        chute_int = int(chute_str)  # converte a var chute_str de str para int
        
        if (chute_int < 1 or chute_int > 100):
            print("número inválido")
            continue

        acertou = numero_secreto == chute_int  # guarda como variável a condição de igualdade
        maior = numero_secreto < chute_int # guarda como variável a condição de maior que
        menor = numero_secreto > chute_int # guarda como variável a condição de menor que

        if (acertou): # se acertou true, executa:
            print("você acertou e fez {} pontos!".format(pontos))
            break
        else: # se acertou false, executa:
            if (maior): # se maior true, executa:
                print("você errou! o seu chute foi maior")
            elif (menor): # se menor true, executa:
                print("você errou! o seu chute foi menor")
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

        # rodada = rodada + 1 # incrementa a cada rodada

    print("fim de jogo")

    # if (numero_secreto == chute_int): # compara para ver se as var são iguais e retorna -> true ou false
    #     print("você acertou") # para true
    # else:
    #     print("você errou") # para false

if (__name__ == "__main__"):
    jogar()