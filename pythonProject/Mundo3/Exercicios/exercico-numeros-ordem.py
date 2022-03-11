lista = []
for c in range(0, 5):
    lista.append(input(f'Digite um número para a posiçao {c}:'))
mai = max(lista)
mini = min(lista)
posmai = lista.index(mai)
posmin = lista.index(mini)
print(f'Voce digitou os Numueros:{lista}')
print(f'O maior valor é {mai} e esta na posição {posmai}')
print(f'E o menor valor é {mini} e esta na posição {posmin}')
