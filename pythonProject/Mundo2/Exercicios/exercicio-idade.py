from datetime import date
maior = 0
menor = 0
today = date.today().year
for c in range(1,8):
    age = int(input('Digite o ano que voce nasceu:'))
    maiores = today - age
    if age >= 18:
            maior += 1
    else:
            menor += 1
print('Temos {} maiores de idade, e {} menores de idade'.format(maior,menor))

# Mesmo codigo resumido
#from datetime import date
#menores = 0
#for c in range(1, 8):
#    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
#    if date.today().year - pessoa < 21:
#        menores += 1
#print('\n{} são Maiores e {}são menores.'.format(7 - menores, menores))
