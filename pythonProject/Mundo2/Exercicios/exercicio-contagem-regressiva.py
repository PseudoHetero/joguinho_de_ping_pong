import sys
from time import sleep
print('\033[34m*'*60)
print('{:^60}'.format('Contador do Ano Novo'))
print('*'*60)
new = input('\033[mEsta pronto para a contagem?').upper()
if new == 'SIM':
    sleep(1)
    print('VAMOS LÁ')
else:
    print('Ok, Talvez mais tarde')
    sys.exit()
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[34mFELIZ ANO NOVO!!!\033[m')
