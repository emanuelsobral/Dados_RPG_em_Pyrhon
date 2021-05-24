import random
from random import randint
from random import choice
import os

d4 = random.randint(0,4)
d6 = random.randint(0,6)
d8 = random.randint(0,8)
d10 = random.randint(0,10)
d12 = random.randint(0,12)
d20 = random.randint(0,20)
d100 = random.randint(0,100)
corpo = ['Braço esquerdo','Braço direito','Torso','Perna esquerda','Perna direita','Cabeça']
corpo_select = (choice(corpo))
dado = ''


while dado !=  '9' :

    print( '''
[ 1 ] D4
[ 2 ] D6
[ 3 ] D8
[ 4 ] D10
[ 5 ] D12
[ 6 ] D20
[ 7 ] d100
[ 8 ] Partes do corpo
[ 9 ] Sair

    ''')

    dado = input('Escolha uma opção: ')
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    if dado == '1':
        print(f'D4 = {d4}')
        d4 = random.randint(1,4)
    elif dado == '2':
        print(f'D6 = {d6}')
        d6 = random.randint(1,6)
    elif dado == '3':
        print(f'D8 = {d8}')
        d8 = random.randint(1,8)
    elif dado == '4':
        print(f'D10 = {d10}')
        d10 = random.randint(1,10)
    elif dado == '5':
        print(f'D12 = {d12}')
        d12 = random.randint(1,12)
    elif dado == '6':
        print(f'D20 = {d20}')
        d20 = random.randint(1,20)
    elif dado == '7':
        print(f'D100 = {d100}')
        d100 = random.randint(1,100)
    elif dado ==  '8':
        print(f'Parte do corpo = {corpo_select}')
        corpo_select = (choice(corpo))
    elif dado == '9':
        break
    else:
        os.system('cls')
        print('Alternariva não encontrada')
print('Aplicação finalizada')
