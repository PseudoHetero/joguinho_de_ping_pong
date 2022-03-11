from random import randint
from time import sleep
print('-=-' * 24)
print('lets play!! Digite um numemero de 0 - 5 que voce acha que estou pensando')
print('-=-' * 24)
n = int(input('Digite o numero:'))
c = randint(0, 5)
print('Processando...')
sleep(2)
if n > 5:
    print('Eu disse de 0 - 5 tapado')
    exit()
if n == c:
    print('Droga voce ganhou ;--;')
else:
    print('HA, eu sou imbatível')
print('Eu pensei no numero {}'.format(c))
