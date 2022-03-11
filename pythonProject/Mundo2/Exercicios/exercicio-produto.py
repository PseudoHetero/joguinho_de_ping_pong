# cores
cor1 = '\033[35m'
cor2 = '\033[36m'
print('{}-.'.format(cor1) * 25)
# comando para centralizar
print('{:^50}'.format('Bem-vindo à Lojinha ForaBolsonaro'))
# ..........
print('-.' * 25)
valor = float(input('Digite o valor do produto que deseja comprar:'))
print("-.-.-.-.Selecione as opçoes-.-.-.-.-")
print("""1 - à vista {}dinheiro/cheque{}(10% de desconto)
2 - à vista no {}cartão{}(5% de desconto)
3 - em até {}2x no cartão{}(Preço normal)
4 - {}3x ou mais no cartão{}(20% de juros)""".format(cor2, cor1, cor2, cor1, cor2, cor1, cor2, cor1))
print('-.' * 20)
num = int(input('Selecione a opção:'))
if num == 1:
    print('A sua compra é de {}R${:.2f}{}, pagando com dinheiro/cheque o preço fica {}R${:.2f}{}'
          .format(cor2, valor, cor1, cor2, (valor - (10 / 100 * valor)), cor1))
elif num == 2:
    print('A sua compra é de {}R${:.2f}{}, pagando a vista no cartão o preço fica {}R${:.2f}{}'
          .format(cor2, valor, cor1, cor2, (valor - (5/100 * valor)), cor1))
elif num == 3:
    print('A sua compra é de {}R${:.2f}{}, em ate 2x no cartao opreço fica {}R${:.2f}{}'
          .format(cor2, valor, cor1, cor2, valor, cor1))
    parc = int(input('Digite em quantas vezes deseja parcelar em até {}2{} vezes:'.format(cor2, cor1)))
    if parc > 2:
        print('A compra nessa opção so pode ser de 2 vezes')
        exit()
    print('A sua compra foi parcelada em {}{}{} vezes e ficou {}R${:.2f}{} por mês'
          .format(cor2, parc, cor1, cor2, (valor // parc), cor1))
elif num == 4:
    print('A sua compra é de {}R${:.2f}{}, parcelando em mais de 3x tera um acrescimo de {}20%{}'
          .format(cor2, valor, cor1, cor2, cor1))
    parc2 = int(input('Digite em quantas vezes deseja parcelar:'))
    print('A sua compra foi parcelada em {}{}{} vezes e ficou {}R${:.2f}{}, por mês'
          .format(cor2, parc2, cor1, cor2, ((valor + (20/100) * valor) / parc2), cor1))
else:
    print('Favor digitar um numero de 1 à 4.')
print('-.' * 40)
