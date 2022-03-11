from math import factorial
soma = 0
n = int(input('Digite um valor para calcular o fatorial:'))
f = factorial(n)
c = n

while c > 0:
    print('{}'.format(c,), end='')
    print('x' if c > 1 else '=', end='')
    c -= 1

print('{}'.format(f))


