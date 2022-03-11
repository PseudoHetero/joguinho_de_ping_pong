from random import randint
count = 0
print('\033[31m-=-' * 24)
print('lets play!! Digite um numemero de 0 - 5 que voce acha que estou pensando')
print('-=-' * 24)
n = int(input('Digite o numero:'))
c = randint(0, 10)
while c != n:
    if n < c:
        print('Palpite muito baixo ')
    else:
        print('Palpite muito alto')
    n = int(input('Ha Você errou, tente de novo:'))
    count += 1
print('Depois de muito pensar, voce acertou com {} tentativas'.format(count))
