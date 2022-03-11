print('\033[34m-.'*15)
print('{:^30}'.format('10 Termos de um PA'))
print('-.'*15)
termo = int(input('Digite o Termo:'))
razao = int(input("Digite a Razão:"))
dec = termo + (10 - 1) * razao
for c in range(termo, dec + razao, razao):
    print('{}'. format(c), end= ' -> ')
print('END')
