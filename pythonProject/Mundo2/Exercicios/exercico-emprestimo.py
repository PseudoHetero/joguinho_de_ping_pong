from time import sleep
print('\033[34m Bom dia, O que você deseja fazer?')
v1 = int(input('\033[34mDigite: \n1 Para emprestimo\n2 Para pagamento \n3 Para falar com um representante:'))
if v1 == 2:
    print('\033[31mNossas linhas estão congestionadas favor ir em uma agencia pra realizar o pagamento')
elif v1 == 3:
    print('Estamos te direcionando...')
    sleep(4)
    print('\033[31mNão conseguimos achar nenhuma linha disponivel ')
elif v1 == 1:
    home = float(input('Qual o valor da casa que deseja comprar?'))
    job = float(input('Qual o seu salário?'))
    ano = int(input('Em quantos anos deseja pagar a mensalidade?'))
    mes = home * ano / 12
    percen = 30 / 100 * job
    if percen <= mes:
       print('\033[31mMe desculpa mas o emprestimo nao pode ser liberado.')
    else:
        print('\033[32mParabens o emprestimo sera depositado na sua conta')
        print('A mensalidade do emprestimo é de R${:.2f} por mês'.format(mes))
