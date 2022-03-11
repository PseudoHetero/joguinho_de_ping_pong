pessoas = list()
pessoas.append(str(input('Digite o nome da pessoa:')))
v = input('Deseja continuar?')
while v == 's':
    pessoas.append(str(input('Digite um nome:')))
    v = input('Deseja continuar?')
    if v == 'n':
        break
print(pessoas)