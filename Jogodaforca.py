import os  #Importa o módulo os para uso do cls
from Imagensdojogo import load   #Importa o módulo load do pacote Imagensdojogo
from Modulos_do_jogo import modulo  #Importa o módulo modulo do pacote Modulos_do_jogo
from Palavras_secretas_do_jogo import palavrasorteada  #Importa o módulo palavrasorteada do pacote Palavras_secretas_do_jogo


def main(): #Função principal do programa
    '''Está função executara deiversas funções em modulos de pacotes como o objetivo de criar
       criar o jogo da forca, os modulos estão sendo usados para facilitar a manutenção e diminuir
       a quantidade de codigos na função principal
    '''
    palavra_secreta = palavrasorteada.sorteio().upper()  #Variavel que recebe a palavra secreta de forma aleatória atravé do módulo palavrasorteada
    letras_descobertas = ''  #Variavel vazia que receberá as letras acertadas
    letras_erradas = ''   #Variavel vazia que receberá as letras erradas
    Jogo = True        #enquando o valor de jogo for True o jogo estará sendo executado
    Nome = modulo.solicita_nome()   #Solicita o nome do jogador através da função solicita_nome no pacote Modulos_do jogo
    qtd_vitoria = 0           #Conta a quantidade de vitórias
    qtd_derrota = 0           #Conta a quantidade de derrotas
    qtd_partidas = 0
    carregar = load.load()    #Execulta uma sequancia de prints simulando o carregamento do jogo

    while Jogo:       #enquando o valor de jogo for True o jogo estará sendo executado

        print(carregar)     #Exibe a simulação de um carregamento do jogo, imprime a variavel carregar
        os.system('cls')    #Limpa a tela a cada jogada a fins de manter a tela sempre limpa, funciona apenas se executado no DOS
        modulo.linhas()     #imprime linhas na tela
        modulo.dados_do_jogador(Nome, letras_erradas, qtd_vitoria, qtd_derrota, qtd_partidas) # imprime na tela nome, numero de derrotas e vitórias
        modulo.linhas()     #imprime linhas na tela
        modulo.inicio(palavra_secreta, letras_descobertas, letras_erradas) #Inicia o jogo através da função inicio

        letra = modulo.tentativas(letras_erradas + letras_descobertas) #variavel letra recebe o valor da tentativa realizada
        if letra in palavra_secreta: #Se a letra estiver em palavra_secreta
            letras_descobertas += letra #a letra é adicionada a variavel letras_descobertas
            if modulo.verifica_letras(palavra_secreta, letras_descobertas):  #verifica se todas as letras estão corretas
                print('Parabens! A palavra secreta e ' + palavra_secreta + '! Voce ganhou!!') #exibe a palavra secreta
                Jogo = False #Muda para o jogo mudando True para falso

            if not Jogo: #Se o valor não for True

                while True:
                    jogardenovo = str(input('Deseja jogar novamente? [S/N]  ')).upper() [0] #Pergunta se deseja continuar
                    if jogardenovo in 'SN': #Garante que os valores sejam S ou N
                        break #Para o loop
                    print('ERRO! Responda apenas S ou N.') #Imprime mensagem de erro

                if jogardenovo == 'S': #Se o vaor for igua a S
                    palavra_secreta = palavrasorteada.sorteio().upper()   #Gera uma palavra secreta nova
                    letras_descobertas = ''  #Zera os valores da variavel de letras_descobertas
                    letras_erradas = ''     #Zera os valores da variavel de letras_erradas
                    qtd_vitoria += 1      #Soma uma vitória a variavel qtn_vitoria
                    qtd_partidas += 1    #Soma uma partidas a variavel qtn_partidas
                    Jogo = True      #Muda o valor de False para True iniciando o jogo novamente
                else: # Se o valor fo N
                    qtd_vitoria += 1  # Soma uma vitória a variavel qtn_vitoria
                    qtd_partidas += 1 #Soma uma partidas a variavel qtn_partidas
                    modulo.dados_do_jogador(Nome, letras_erradas, qtd_vitoria, qtd_derrota, qtd_partidas) # imprime na tela nome, numero de derrotas e vitórias


        else:
            letras_erradas += letra     #Se a letra não estiver em palavra_secreta ela é adicionada a letras_erradas
            if len(letras_erradas) ==  6:    #determina o valor maximo de tentativas até 6
                modulo.inicio(palavra_secreta, letras_descobertas, letras_erradas)  #Incia o jogo novamente mantendo os valores até que o limite seja alcançãdo
                print("Voce exagerou o seu limite de tentativas!")
                print("Depois de " + str(len(letras_erradas)) + ' letras erradas e' + str(len(letras_descobertas)), end=' ') #exibe de erros e acertos
                print('Tentativas incorretos, a palavra era ' + palavra_secreta + '.') #Revela a palavra secreta
                Jogo = False #Muda para o jogo mudando True para falso

            if not Jogo: #Se o valor não for True
                while True:
                    jogardenovo = str(input('Deseja jogar novamente? [S/N]  ')).upper() [0] #Pergunta se deseja continuar
                    if jogardenovo in 'SN':  #Garante que os valores sejam S ou N
                        break  #Para o loop
                    print('ERRO! Responda apenas S ou N.') #Imprime mensagem de erro

                if jogardenovo == 'S': #Se o vaor for igua a S
                    palavra_secreta = palavrasorteada.sorteio().upper()   #Gera uma palavra secreta nova
                    letras_descobertas = ''  #Zera os valores da variavel de letras_descobertas
                    letras_erradas = ''     #Zera os valores da variavel de letras_erradas
                    qtd_vitoria += 1      #Soma uma vitória a variavel qtn_vitoria
                    qtd_partidas += 1    #Soma uma partidas a variavel qtn_partidas
                    Jogo = True      #Muda o valor de False para True iniciando o jogo novamente
                else:
                    qtd_derrota += 1  # Soma uma vitória a variavel qtn_derrotas
                    qtd_partidas += 1 #Soma uma partidas a variavel qtn_partidas
                    modulo.dados_do_jogador(Nome, letras_erradas, qtd_vitoria, qtd_derrota, qtd_partidas) # imprime na tela nome, numero de derrotas e vitórias

main()
