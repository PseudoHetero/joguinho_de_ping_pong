from random import randint
# Para repetição de um programa
num = tuple(randint(1,10) for a in range(5))
# Descobrir o maior e o menor
print('Numeros gerados aleatoriamente:',*num)
print(f'Maior Numero {max(num)}')
print(f'Menor Numero {min(num)}')


