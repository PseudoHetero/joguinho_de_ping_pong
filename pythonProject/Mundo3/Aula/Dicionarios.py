# Estrutura dos dicionários
filmes = {'titulo': 'star wars', 'ano': 1977, 'Diretor': 'George Lucas'}

# Para deletar algum item do dicionario
#del filmes['titulo]

print(f'O filme {filmes["titulo"]} foi lancado em {filmes["ano"]}')
# Para referenciar um elemento é necessario usar cochetes

print(filmes.keys())
print(filmes.items())
print(filmes.values())

for k in filmes.keys():
    print(k)

for k, v in filmes.items():
    print(f'{k} = {v}')