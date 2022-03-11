n = int(input('Digite o número que você deseja ver a tabuada:'))
t = 0
print('{:.^30}'.format('TABUADA DO {} '.format(n)))
while t <= 10:
    print('{} X {} = {}'.format(n, t, (n * t)))
    t = t + 1
