from datetime import datetime
trampo = {'nome': (str(input('Digite o seu nome:'))),
          'ano': (int(input('Digite o ano em que voce ''nasceu:'))),
          'ct': (int(input('Digite o Número da sua carteira de trabalho (0 se não possuir:')))}
idade = datetime.now().year - trampo['ano']
if trampo['ct'] == 0:
    print('*-' * 30)
    print(f'- Nome {trampo["nome"]}\n- Idade {idade}\n')
else:
    trampo['ac'] = int(input('Digite o seu ano de contratação:'))
    trampo['sal'] = float(input('Digite o seu sálario:'))
    trampo['apos'] = (trampo['ac'] - trampo['ano']) + 35

    print('*-' * 30)
    print(f'- Nome {trampo["nome"]}\n- Idade {idade}\n- Carteira de Trabalho {trampo["ct"]}\n'
          f'- Ano de Contratação: {trampo["ac"]}\n- Sálario R${trampo["sal"]}\n'
          f'- VAi se aposentar com {trampo["apos"]} anos')
