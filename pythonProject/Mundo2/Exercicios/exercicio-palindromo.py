nome = input('Digite uma palavra:').upper().strip().replace(' ','')
inv = nome[::-1]
if inv == nome:
    print('O nome {} de trás pra frente é {}, sendo assim ele É um PALINDROMO'.format(nome, inv))
else:
    print('A palavra {} de trás pra frente é {}, sendo assim NÃO é um PALINDROMO'.format(nome, inv))
