import time
from Imagensdojogo import imagem


def inicio(palavra_secreta, letras_descobertas, letras_erradas):

    '''
    Está função imprimirá a imagem da forca de uma lista, determinando sempre o index da lista
    de acordo com o valor de length obitido na variavel letras_erradas, a função imprimirá tambem
    a quantidade de letras da palavra secreta em '_' baseado no length da variavel  palavra_secreta,
    a cada letra que for acertada um '_' será substituido pela mesma.
    '''

    imagem.forca_erros(letras_erradas) #Imprime a imagem da forca através da função forca_erros no pacote imagem
    print("Letras Erradas:", end=' ') #Imprime a frasa Letras erradas: determinando no final (end) um espço vazio
    print (letras_erradas)       #Imprime as leras erradas

    vazio = '_' * len(palavra_secreta)  #Imprime '_' de acordo com length (cumprimento) da palavra secreta
    for i in range(len(palavra_secreta)):   #Percorre a palavra secreta armazenada na variavel palavra_secreta
        if palavra_secreta[i] in letras_descobertas:  #Analisa se a letra digitada está na palavra secreta
            vazio = vazio[:i] + palavra_secreta[i] + vazio[i + 1:]  #Substitui o '_' pela letra certa na posição certa
    print(vazio)  #Imprime o valor da variavel vazio



def tentativas(tentativ_realizada):
    '''
    Está função verificará se a letra digitada corresponde ao requisitos necesarios são eles:
    verifica se foi digitado mais de uma letra, verifica se a letra ja foi digitada
    '''

    while True:
        letra = input("Digite uma letra: ").upper()
        if len(letra) != 1:  # verifica se apalavra escrita em palpite tem uma letra so.
            print('Coloque uma unica letra')
            time.sleep(2)
        elif letra in tentativ_realizada:  # se palpite esta dentro de palpites feitos
            print('Voce ja digitou essa letra, digite de novo!')
            time.sleep(2)
        elif not 'A' <= letra <= 'Z':  # verifica se palpite e menor ou igual a A ou se e menor ou igual a Z
            print('Escolha Somente uma letra!')
            time.sleep(2)
        return letra


def verifica_letras(palavra_secreta, letras_descobertas):
    '''
    Está função verifica se todas as letras foram acertadas
    '''
    vitoria = True
    for x in palavra_secreta:  #Percorre a palavra secreta
        if x not in letras_descobertas: #Verifica se todas as letras da palavras secreta estão em letras descobertas
            vitoria = False  #Muda o valor da variavel para False
            break  #Para o laço For
    return vitoria #Retorna o valo =r da variavel



def solicita_nome():
    '''
    EStá função solicita o nome do jogador
    '''

    return  input("DIGITE O NOME DO JOGADOR: ").upper()  #Solicita o nome do jogador


def dados_do_jogador(Nome, letras_erradas, qtd_vitoria, qtd_derrota, qtd_partidas):
    '''
    Está função imprime os dados do jogador e do jogo, quantidade de vitória, derrotas e partidas
    '''

    print('JOGADOR: ',  Nome)  #Imprime o nome do jogador
    print("TEMA: ANIMAIS")
    tentativas = 6 - len(letras_erradas)  #A cada palavra errada decrementa o numero 6
    print('TENTATIVAS: ', tentativas)    #Mostra a quinatidade de tentativas restantes
    print ('VITORIAS: ',qtd_vitoria)     #imprime a quantidade de vitórias
    print('DERROTAS: ', qtd_derrota)     #Imprime a quantidade de derrotas
    print('PARTIDAS: ', qtd_partidas)  # Imprime a quantidade de derrotas


def linhas():
    '''
    imprime linhas para acabamentos
    '''
    print('=============================================================') #imprime linhas para acabamentos


