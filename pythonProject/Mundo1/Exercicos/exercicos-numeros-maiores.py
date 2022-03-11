salario = float(input('Digite o salário do funcionário:'))
if salario <= 1250:
    aumento1 = salario + (salario * 15 / 100)
    print('O seu novo sálario é R${:.2f}'.format(aumento1))
else:
    aumento2 = salario + (salario * 10 / 100)
    print('O seu novo sálario é R${:.2f}'.format(aumento2))
