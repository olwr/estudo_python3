import forca # nome do arquivo forca.py
import adivinhacao # nome do arquivo adivinhacao.py

print("****************************")
print("Escolha o seu jogo!")
print("****************************")

print("(1) Forca (2) Adivinhação")

jogos = int(input("Qual jogo?"))

if (jogos == 1):
    print("Jogando forca")
    forca.jogar() # chama a função dentro do arquivo
elif(jogos == 2):
    print("Jogando adivinhação")
    adivinhacao.jogar() # chama a função dentro do arquivo