peso = float(input('Digite o seu peso (kg)'))
altura = float(input('Digite a sua altura(m)'))
imc = peso / (altura * altura)
print('O imc dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print("Você esta ABAIXO do peso.")
elif 18.5 <= imc < 25:
    print('O seu peso esta IDEAL.')
elif 25 <= imc < 30:
    print('Voce esta no SOBREPESO')
elif 30 <= imc < 40:
    print('Você esta OBESO')
elif imc > 40:
    print('Você esta na categoria de OBESIDADE MORBIDA! Cuidado')

