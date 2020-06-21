import random  #Importa a função random

def sorteio(): #Função que seleionará a palavra secreta de forma eleátória
    '''
    Está função selecionará de forma automatica uma palavra do arquivo palavrassecretas.txt
    e armazenará seu valor na rariavel palv.
    '''

    palav = random.choice(open('.\palavrassecretas.txt', 'r').readlines())  #Armazena na variavel a palavra secreta aleatória
    palav = palav.rstrip('\n')  #Retira a próxima linha que almenta o length da palavra
    return palav #Retorna o valor da variavel