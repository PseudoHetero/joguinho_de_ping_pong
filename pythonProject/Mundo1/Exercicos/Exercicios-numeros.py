num = int(input('Digite um numeno de 0 à 9999:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}'.format(num))
print('{} Unidades'.format(u))
print('{} Dezenas'.format(d))
print('{} Centena'.format(c))
print('{} Milhar'.format(m))

