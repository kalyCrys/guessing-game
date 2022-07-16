def jogar():
    import random
    print("======================================")
    print("== Bem vindo ao jogo de adivinhação ==")
    print("======================================")

    # declaracao de variaveis
    tentativas = 0
    fim_jogo= False
    pontos = 100
    nivel_valido = False
    resultado = True
    
    def acertou():
        print("Parabéns! Você acertou o número secreto ")
        print("Pontuação: {}".format(pontos))
        fim_jogo = True
    
    def maior():
        print("Você errou, o meu número é maior que o seu")
        
    def menor():
        print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas)) 
        
    def jogo_perdido(resultado):
        print("========= GAME OVER =========")
        print("pontuação: {}".format(pontos))
        print("Meu número era {}".format(numero_secreto))
        resultado = fim_jogo
        
    # escolha do nivel
    def escolha_nivel():
        print("Qual é  nível de dificuldade: ")
        print("(1) Fácil  (2) Médio   (3) Difícil ")

    # chamando função
    escolha_nivel()
    # Se a escolha for invalida o programa ira pedir que o user digite novamente
    while(nivel_valido == False):
        nivel = input("Defina um nível: ")
        nivel = int(nivel)
        if(nivel == 1):
            numero_secreto = random.randrange(1,11)
            nivel_valido = True
            print("Modo fácil")
            tentativas = 5
        elif(nivel == 2):
            numero_secreto = random.randrange(1,51)
            nivel_valido = True
            print("Modo Médio")
            tentativas = 10
        elif(nivel == 3):
            numero_secreto = random.randrange(1,101)
            nivel_valido = True
            print("Modo Difícil")
            tentativas = 15
            
        else:
            nivel_valido = False
            print("Escolha invalida, tente novamente")
            escolha_nivel()
        
    if(nivel == 1):
        while(fim_jogo != True):
            tentativas= tentativas - 1
            numero = int(input("Digite um número entre 1 e 10: "))
            # numero = int(numero)
            if numero == numero_secreto:
                acertou()
            else:
                print("que pena, você errou")
                pontos = abs(pontos - numero)
                if numero_secreto > numero:
                    print("O meu número é maior que o seu, número de tentativas: {}".format(tentativas))    
                else:
                    print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas))     
                
            
            if tentativas == 0:
                fim_jogo = True
                jogo_perdido(fim_jogo)
                
    elif(nivel == 2):
        while((fim_jogo != True)):
            tentativas= tentativas - 1
            numero = int(input("Digite um número entre 1 e 50: "))
            if numero == numero_secreto:
                acertou()
            else:
                print("que pena, você errou")
                pontos = abs(pontos - numero)
                if numero_secreto > numero:
                    print("O meu número é maior que o seu, número de tentativas: {}".format(tentativas))    
                else:
                    print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas))     
                
            if tentativas == 0:
                fim_jogo = True
                jogo_perdido()
                
            # tentativas= tentativas - 1
            
    elif(nivel==3):
        while(fim_jogo != True):
            tentativas= tentativas - 1
            numero = int(input("Digite um número entre 1 e 100: "))
            if numero == numero_secreto:
                acertou()
            else:
                print("que pena, você errou")
                pontos = abs(pontos - numero)
                if numero_secreto > numero:
                    print("O meu número é maior que o seu, número de tentativas: {}".format(tentativas))    
                else:
                    print("O meu número é menor que o seu, número de tentativas: {}".format(tentativas))     
            if tentativas == 0:
                fim_jogo = True
                jogo_perdido()