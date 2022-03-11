print('Digite dois numeros')
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
elif n1 == n2:
    print('Os valores são iguais')