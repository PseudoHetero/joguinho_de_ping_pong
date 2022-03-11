from random import randint
import time
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogadores.items():
    time.sleep(1)
    print(f'O {k} tirou o Numero {v}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=-'*30)
for i,v in enumerate(ranking):
    print(f'Em {i+1} lugar: {v[0]} com {v[1]}')
    time.sleep(1)