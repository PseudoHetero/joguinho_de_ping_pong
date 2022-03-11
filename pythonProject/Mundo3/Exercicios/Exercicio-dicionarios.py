lista = {}
nome = (str(input('Digite o nome do aluno:')))
lista['aluno'] = nome
media = (float(input('Digite a média do aluno:')))
lista['nota'] = media
print('-='*15)
if lista['nota'] <= 5:
    print(f' - O aluno {lista["aluno"]}\n - Com media de {lista["nota"]}\n'f' - Esta REPROVADO')
elif lista['nota'] < 7:
    print(f' - O aluno {lista["aluno"]}\n - Com media de {lista["nota"]}\n'f' - Esta de RECUPERAÇÃO')
elif lista['nota'] >= 7:
    print(f' - O aluno {lista["aluno"]}\n - Com media de {lista["nota"]}\n'f' - Esta APROVADO\n - PARABENS')

# aluno = {'nome': str(input('Nome: '))}
# aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
# aluno['situação'] = 'aprovado' if aluno['média'] >= 7 else 'reprovado' if aluno['média'] <6 else 'recuperação'
# for key, value in aluno.items():
# 	print(f'{key}:', value)
