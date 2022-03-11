num = int(input('Digite um numero:'))
par = num % 2
if par == 1:
    print('_-_' * 15)
    print('O número {} é IMPAR'.format(num))
    print('_-_' * 15)
else:
    print('_-_' * 15)
    print('O número {} é PAR'.format(num))
    print('_-_' * 15)