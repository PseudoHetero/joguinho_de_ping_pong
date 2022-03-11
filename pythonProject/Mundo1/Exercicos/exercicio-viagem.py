via = float(input('Qual a distancia da sua viagem?'))
promo = via * 0.50
norm = via * 0.45
if via <= 200.00:
    print('Sua viagem é de {} Km.'.format(via))
    print('A sua viagem ficou no preço de R${}.'.format(promo))
else:
    print('Sua viagem é de {} Km.'.format(via))
    print('A sua viagem ficou no preço de R${}.'.format(norm))
