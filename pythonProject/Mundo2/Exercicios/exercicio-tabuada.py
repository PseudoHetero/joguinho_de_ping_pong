
while True:
    n = int(input('Digite o número para ver a tabuada:'))
    if n > 0:
        for c in range(1,11):
            print(f'{n} X {c} = {n * c}')
    else:
        break