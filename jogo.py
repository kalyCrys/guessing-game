import random
print("======================================")
print("== Bem vindo ao jogo de adivinhação ==")
print("======================================")

# declaracao de variaveis
tentativas = 3
fim_jogo= False
# escolha do nivel
nivel_valido = False
print("Qual é  nível de dificuldade: ")
print("(1) Fácil  (2) Médio   (3) Difícil ")

# Se a escolha for invalida o programa ira pedir que o user digite novamente
while(nivel_valido == False):
    nivel = input("Defina um nível: ")
    nivel = int(nivel)
    if(nivel == 1):
        numero_secreto = random.randrange(1,11)
        nivel_valido = True
    elif(nivel == 2):
        numero_secreto = random.randrange(1,21)
        nivel_valido = True
    elif(nivel == 3):
        numero_secreto = random.randrange(1,31)
        nivel_valido = True
    else:
        nivel_valido = False
        print("Escolha invalida, tente novamente")
    
    

if(nivel == 1):
    while((fim_jogo != True) or (tentativas > 0)):
        tentativas= tentativas - 1
        numero = input("Digite um número entre 1 e 10: ")
        numero = int(numero)
        if numero == numero_secreto:
            print("Parabéns! Você acertou o número: ")
            fim_jogo = True
        else:
            print("que pena, você errou")
            if numero_secreto > numero:
                print("O meu número é maior que o seu, número de tentativas: {}".format(tentativas))    
            else:
                print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas))     
            
        
        if tentativas == 0:
            print("Meu número era {}".format(numero_secreto))
            fim_jogo = True
            
        # tentativas= tentativas - 1    

elif(nivel == 2):
    while((fim_jogo != True) or (tentativas > 0)):
        tentativas= tentativas - 1
        numero = input("Digite um número entre 1 e 20: ")
        numero = int(numero)
        if numero == numero_secreto:
            print("Parabéns! Você acertou o número: ")
            fim_jogo = True
        else:
            print("que pena, você errou")
            if numero_secreto > numero:
                print("O meu número é maior que o seu, número de tentativas: {}".format(tentativas))    
            else:
                print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas))     
            
        
        if tentativas == 0:
            print("Meu número era {}".format(numero_secreto))
            fim_jogo = True
            
        # tentativas= tentativas - 1
        
elif(nivel==3):
    while(fim_jogo != True):
        tentativas= tentativas - 1
        numero = input("Digite um número entre 1 e 30: ")
        numero = int(numero)
        if numero == numero_secreto:
            print("Parabéns! Você acertou o número: ")
            fim_jogo = True
        else:
            print("que pena, você errou")
            if numero_secreto > numero:
                print("O meu número é maior que o seu, número de tentativas: {}".format(tentativas))    
            else:
                print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas))     
            
        
        if tentativas == 0:
            print("Meu número era {}".format(numero_secreto))
            fim_jogo = True
            
        # tentativas= tentativas - 1