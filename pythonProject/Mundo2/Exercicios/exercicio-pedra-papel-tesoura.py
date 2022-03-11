from random import randint
# Cores
vermelho = '\033[31m'
verde = '\033[32m'
ciano = '\033[36m'
print('\033[36m-.' * 30)
print('{:^60}'.format('Pedra, Papel e Tesoura'))
print('\033[36m-.' * 30)
print('Olá vamos jogar um jogo?')
print('''Escolha entre:
1 - Pedra
2 - Papel 
3 - Tesoura''')
cpu = randint(1, 3)
user = int(input('Digite o número:'))
if user == 1 and cpu == 2:
    print('{}Ha Papel cobre Pedra'.format(vermelho))
    print('VOCE PERDEU!!')
elif user == 1 and cpu == 3:
    print('{}Droga, Pedra quebra Tesoura'.format(verde))
    print('VOCE GANHOU')
elif user == 1 and cpu == 1:
    print('Parece que empatou, melhor de 3?')
elif user == 2 and cpu == 3:
    print('{}Ha Tesoura corta Papel'.format(vermelho))
    print('VOCE PERDEU!!')
elif user == 2 and cpu == 1:
    print('{}Droga, Papel cobre Pedra'.format(verde))
    print('VOCE GANHOU')
elif user == 2 and cpu == 2:
    print('Parece que empatou, melhor de 3?')
elif user == 3 and cpu == 1:
    print('{}Ha Pedra quebra Tesoura'.format(vermelho))
    print('VOCE PERDEU!!')
elif user == 3 and cpu == 2:
    print('{}Droga, Tesoura corta Papel'.format(verde))
    print('VOCE GANHOU')
elif user == 3 and cpu == 3:
    print('Parece que empatou, melhor de 3?')
