alt = float(input('Digite a altura da parede:'))
lar = float(input('Digite a largura da parede:'))
m2 = alt * lar

print('A aréa da parede é de {}, você vai precisar de {} litros de tinta'.format(m2, (m2 / 2)))
