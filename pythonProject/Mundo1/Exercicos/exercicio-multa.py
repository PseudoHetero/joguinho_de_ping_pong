print('_-_' * 15)
print('Bem-vindo ao site do Detran')
print('_-_' * 15)
km = float(input('Digite a quilometragem:'))
multa = (km - 80.00) * 7
if km >= 80.00:
    print('Voce excedeu o limite permitido e foi multado')
    print('Sua multa é de R${}'.format(multa))
    print('Aprende a dirigir animal')
else:
    print('Voce está dentro da lei')
    print('Não faz mais que a obrigação')

