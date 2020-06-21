
"Lista com imagens que serão exibidas durante o jogo"
FORCAIMG = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def forca_erros(letras_erradas):
    '''
    Esta Função imprime a imagen da lista usando o length (cumprimento) da variavel para determinar o index da imagem
    será exibido
    '''

    print(FORCAIMG[len(letras_erradas)] + '\n') #Imprime a imagem da lista usado valor de cumprimento como index





