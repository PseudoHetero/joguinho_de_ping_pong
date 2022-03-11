# Somador
soma = 0
# Acumulador
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma dos valores é {}, o total de valores é {}'.format(soma, cont))
