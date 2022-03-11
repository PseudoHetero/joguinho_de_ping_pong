n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) /2
if media < 5.0:
    print('\033[31mA media do aluno é {}'.format(media))
    print('\033[31mO aluno esta REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('\033[33mA media do aluno é {}'.format(media))
    print('\033[33mO aluno esta em RECUPERAÇÂO')
elif media > 7.0:
    print('\033[32mA media do aluno é {}'.format(media))
    print('\033[32mO aluno esta APROVADO')