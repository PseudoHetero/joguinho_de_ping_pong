from datetime import date
print('Bem-vindo ao inferno!!')
birth = int(input('Informe o ano em que voce nasceu:'))
today = date.today().year
anos = today - birth
until = 18 - anos
until2 = until + today
when = anos - 18
when2 = today - when
if anos == 18:
    print('Você possui {} anos.\nEstá apto para cadastro'.format(anos))
elif anos < 18:
    print('Voce possui {} anos'.format(anos))
    print('Você ainda não esta na idade correta para se cadastrar')
    print('Você deve se cadastrar em {}'.format(until2))
elif anos > 18:
    print('Voce possui {} anos'.format(anos))
    print('Você ja se cadastrou no Serviço militar no ano de {}'.format(when2))