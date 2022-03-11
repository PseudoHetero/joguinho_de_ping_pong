from datetime import date
birth = int(input('Informe o ano em que voce nasceu:'))
today = date.today().year
anos = today - birth
if anos <= 9:
    print('O atleta tem {} anos\nÉ classificado como Mirim'.format(anos))
elif anos <= 14:
    print('O atleta tem {} anos\n É classificado como INFANTIL'.format(anos))
elif anos <= 19:
    print('O atleta tem {} anos\n É classificado como JUNIOR'.format(anos))
elif anos <= 25:
    print('O atleta tem {} anos\n É classificado como SÊNIOR'.format(anos))
elif anos > 25:
    print('O atleta tem {} anos\n É classificado como MASTER'.format(anos))
