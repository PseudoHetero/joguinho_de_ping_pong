listagem = ('Lápis' ,1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 15.00,
            'Tranferidor', 7.00,
            'Compasso', 9.99,
            'Mochila', 120.90,
            'Canetas',20.00,
            'Livors', 30.90)
print('.-'*30)
print(f'{"Listagem de Preços":^60}')
print('.-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<50}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
print('.-' * 30)