nome = input('Digite o seu nome completo: ')
minu = nome.lower()
mai = nome.upper()
num = nome.replace(" ","")
num2 = len(num)
con = nome.find(' ')
print('Analisando seu nome...')
print('O seu nome em maiusculo é {} \nO seu nome em minusculo é {}' .format(mai, minu))
print('O seu nome tem ao todo {} letras \nO seu primeiro nome tem {}'.format(num2, con))


