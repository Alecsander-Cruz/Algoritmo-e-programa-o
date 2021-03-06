'''JOGO DA FORCA EM PYTHON
MATÉRIA: ALGORITMO E PROGRAMAÇÃO
prof.: CARLOS EDUARDO
GRUPO: GABRIEL DA SILVA COSTA VASCONCELOS DE ARAÚJO / 1610013277
ALECSANDER DANIEL CRUZ  / 1610014085
CAIO MARTINS LEMOS DE SOUZA / 1610014084

'''
import sys
import string # para manipular as palavras retiradas da lista
import random # para escolher a palavra

lista_facil = ['melhor', 'grande', 'claro', 'azul', 'vermelho', 'preto', 'branco', 'casa', 'tempo', 'felicidade', 'bondade', 'vida',
'caneta', 'cavalo', 'trem', 'golpe', 'cosmos']

lista_dificil = ['procrastinar', 'prolegômenos', 'vicissitudes', 'pernóstico', 'opróbrio', 'idiossincrasia', 'elucubrações',
'chistoso', 'acrimônia', 'combustível', 'concurso', 'protesto', 'governo', 'paquiderme', 'tamandaré']
F_= True
D_= False
dificuldade = True

sair = False

while (not sair):
    print ("---------------------------")
    print ("       JOGO DA FORCA       ")
    print ("---------------------------")
    print ("1- INICIAR PARTIDA         ")
    print ("2- CONFIGURAR DIFICULDADE  ")
    print ("3- SAIR")
    
    while True:
        opcao = input('OPÇÃO DESEJADA: ')
        print()

        if (opcao == '1') or (opcao == '2') or (opcao == '3'):
            break

            print('DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.')

    if opcao == '3':
        sair = True
#--------------MENU DE DIFICULDADE---------------------------------- #       
    if opcao == '2':
        voltar = False
        while (not voltar):
            
           #--------------Asterisco-----------#
            
            if F_ == True:
                FF = '*'
            else:
                FF = ''
            if D_ == True:
                DD = '*'
            else:
                DD = ' '
#------------------------------------------------------------------#
                
            print ('---------------------------')
            print ('       JOGO DA FORCA       ')
            print ('---------------------------')
            print ('F- FÁCIL',FF)
            print ('D- DIFICIL', DD)
            print ('')
            print ('V- VOLTAR')
            while True:
                dific = input('OPÇÃO DESEJADA: ')
                print()
                if (dific == 'F') or (dific == 'D') or (dific == 'V'):
                    break

                print ('DESCULPE, A OPÇÃO DIGITADA É INVÁLIDA.')

            if dific == 'V':
                voltar = True

            if dific == 'F':
                F_ = True
                D_ = False
                dificuldade = True #True é facil

            if dific == 'D':
                F_ = False
                D_ = True
                dificuldade = False #False é dificil
            
#-----------------------------Condições do jogo-----------------------------        
    if opcao == '1':
        if dificuldade == True:
            lista = lista_facil
            vidas = 5
        elif dificuldade == False:
            lista = lista_dificil
            vidas = 3
    
#--------------------------- Inicio do jogo---------------------------------
        joao = vidas
        jogo_completo = False
        letras_erradas = []
        letras_corretas = []
        letras_usadas = []
        palavra = lista[random.randint(0,len(lista)-1)]
        linhas = '_' * len(palavra)
        while jogo_completo == False:

            print('Letras já utilizadas:', end=' ') # print das letras utilizadas
            for i in range(0, len(letras_usadas)):
                print(letras_usadas[i], end=' ')
            print(end='\n\n')
 
            
            for i in range(len(palavra)): # print dos underlines e das letras corretas
                if palavra[i] in letras_corretas:
                    linhas = linhas[:i] + palavra[i] + linhas[i+1:]
            print('Palavra:', end=' ')
            for letra in linhas:
                print(letra, end=' ')
            print(end='\n\n')

            print ('Entre uma letra (0 para sair).', (joao-len(letras_erradas)), 'tentativas restantes.')
            palpite = input ('> ')
            print()
            
            while palpite in letras_usadas:
                print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
                print ('Entre uma letra (0 para sair).', (joao-len(letras_erradas)), 'tentativas restantes.')
                palpite = input ('> ')
                print()
              
            
              
            if palpite == '0':
                break

            if len(palpite)!= 1:
                print ('Oi? Isso não é só uma letra.', end='\n\n')
            elif palpite in letras_erradas:
                print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
            elif palpite not in 'abcdefghijklmnopqrstuvwxyzçôóõíé':
                print ('Oi? Isso não é uma letra.', end='\n\n')
            elif palpite in letras_usadas:
                print ("Letra '",palpite ,"' já utilizada. Tente Outra.", sep='', end='\n\n')
            else:
                letras_usadas.append(palpite)
                if palpite in palavra: # verificação das letras na palavra
                    print("Boa! A letra '", palpite, "' existe na palavra :)", sep='', end='\n\n')
                    letras_corretas.append(palpite)
                    
                    palavra_completa = True # Verificar se o jogador ganhou
                    for (i) in range (len(palavra)):
                        if palavra[i] not in letras_corretas:
                            palavra_completa = False
                            break
                    if palavra_completa:
                        print("Parabéns! Você ganhou. A Palavra era '", palavra, "'.", sep='')
                        print ("Pressione enter para continuar...", end='\n\n')
                        jogo_completo = True
                            
            if palpite not in letras_corretas: #Letras erradas para a contagem da derrota já q vidas por algum motivo é imutável para mim
                if palpite in 'abcdefghijklmnopqrstuvwxyzçôóõíé': 
                    if palpite not in letras_erradas:
                        print("Letra '", palpite,"' não existe na palavra :(", sep='', end='\n\n')
                        letras_erradas.append(palpite)
                        
            if len(letras_erradas) == joao :
                print ("Jogo encerrado. Você perdeu. A palavra era '", palavra,"'.", sep='')
                print ("Pressione enter para continuar...", end='\n\n')
                jogo_completo = True
                
            if jogo_completo:
                jogar_denovo = input ('')
                print()
                if jogar_denovo == (''):
                    jogo_completo = False
                    joao = vidas
                    letras_erradas = []
                    letras_corretas = []
                    letras_usadas = []
                    palavra = lista[random.randint(0,len(lista)-1)]
                    linhas = '_' * len(palavra)
                else:
                    break
