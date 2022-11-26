import random

# organização dos códigos em funções
def mensagem_abertura():
    print("****************************")
    print("BEM VINDO AO JOGO DE FORCA")
    print("****************************")
    
def lista_palavras(nome_arquivo="personagens.txt"):
    with open(nome_arquivo) as forca_palavras:
        palavras = []
        for linha in forca_palavras:
            linha = linha.strip()
            palavras.append(linha)
    
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def input_jogador():
    chute = input("Qual letra? ")
    chute = chute.strip().upper() # ignora espaços dados no input / altera para uppercase
    return chute

def preenche_letras_corretas(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
    # if (chute.upper() == letra.upper()): # altera ambos para uppercase
        if (chute == letra):
        # print("Letra {} na posição {}".format(letra, index))
            letras_acertadas[index] = letra
        # substitui _ pela letra
        index += 1
        
def imprime_erros(erros, tentativas, chute, chutes_errados):
    desenha_forca(erros)
    print("você tem {} tentativa(s)".format(tentativas))
    chutes_errados.append(chute)
    print(chutes_errados)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def jogar():
    
    mensagem_abertura()
    aleatorio = random.randrange(0, 2)
    
    if (aleatorio == 0):
        palavra_secreta = lista_palavras("linguagens.txt")
        print("linguagens de programação")
    else:
        palavra_secreta = lista_palavras()
        print("nomes de personagens de quadrinhos")

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    # valores de funcionalidade para os loops e condicionais
    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7
    chutes_errados = []
    
    while (not enforcou and not acertou): # não enforcou (true) e não acertou (true)
        
        chute = input_jogador()
        
        if (chute in palavra_secreta):
            preenche_letras_corretas(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            tentativas -= 1
            imprime_erros(erros, tentativas, chute, chutes_errados)

        enforcou = erros == 7 # enforcou = True após 7 tentativas
        acertou = "_" not in letras_acertadas # se todos os espaços forem preenchidos, acertou = True
        print(letras_acertadas)
        
#   mensagens de fim de jogo
    if (acertou):
        ganhou()
    else:
        perdeu(palavra_secreta)



if (__name__ == "__main__"):
    jogar()


# códigos antigos

# palavra_secreta = "python".upper()
# letras_acertadas = ["_", "_", "_", "_", "_", "_"]

# palavra_secreta = lista_palavras("linguagens.txt")

# if (erros == 6):
#     break
# if ("_" not in letras_acertadas):
#     break

# if ("_" not in letras_acertadas):
#     print("você ganhou!")
# else:
#     if(erros == 6):
#         print("booho, você perdeu!")
#     else:
#         print("você tem {} tentativa(s)".format(tentativas))