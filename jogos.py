# importando arquivos
import forca
import adivinhacao
inicio = False
while(inicio != True):
    print("======================================")
    print("           Escolha seu jogo              ")
    print("======================================")
    print("(1) Forca   (2) Adivinhação   (3) Sair  ")
    escolha_jogo = int(input("Digite o número correspondente a sua escolha: "))

    if(escolha_jogo == 1):
        print("Jogando forca")
        forca.jogar()

    if(escolha_jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

    if(escolha_jogo == 3):
        print("Saindo...")
        inicio = True