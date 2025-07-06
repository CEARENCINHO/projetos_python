'''
    Gerador de senha:
    peguntar o quantos de caracter deve ter a senha
    se quer incluir letras maiusculas e menusculas, sibolos e numeros
'''

from random import*

a = ['letra maiuslas', 'letras menusculas', 'sibolos', 'numeros']

logico = []

simbolos = [
    '!', '@', '#', '$', '%', '&',
    '_', '?','/'
]

letra = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]

def gerador(qtd):
    senha_gerada = []
    caracter = []

    if logico[0] == True: # letras maiusculas
        for i in letra:
            caracter.append(i.upper())

    if logico[1] == True: # letras menusculas
        for i in letra:
            caracter.append(i)

    if logico[2] == True:
        for i in simbolos: # simbolos 
            caracter.append(i)

    if logico[3] == True:
        for i in range(10): # numeros
            caracter.append(i)


    num = len(caracter) - 1
    for i in range(qtd):
        indice = randint(0, num)
        senha_gerada.append(caracter[indice])

    senha = ''.join(str(item) for item in senha_gerada)
    #senha = ''.join(senha_gerada)

    return (f'\nSenha: {senha}')


def selecao():
    for i in a:
        while True:
            try:
                informacao = input(f'Incluir {i}? (S/N)')
                break
            except ValueError:
                print('Digite apenas "S" ou "N"!')
        if informacao == 'S' or informacao == 's':
            logico.append(True)
        else:
            logico.append(False)
            

print(' '*5,'!GERADOR DE SENHA!')
while True:
    try:
        quant_caracter = int(input('Qual deve ser o tamanho da senha? '))
        break
    except ValueError:
        print('Digite apenas valor "NUMERICO!"')

selecao()
print(gerador(quant_caracter))