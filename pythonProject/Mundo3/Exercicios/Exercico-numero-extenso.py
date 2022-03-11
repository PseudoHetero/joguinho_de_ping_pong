numero = {0:'zero', 1:'um', 2:'dois', 3:'três', 4:'quatro', 5:'cinco', 6:'seis', 7:'sete', 8:'oito',
          9:'nove',10:'dez',11:'onze', 12:'doze', 13:'treze', 14:'quatorze', 15:'quinze',
          16:'dezesseis',17:'dezessete',18:'dezoito', 19:'dezenove', 20:'vinte'}
ext = int(input('Digite um numero de 0-20:'))
while ext > 20:
    ext = int(input('Digite um numero de 0-20:'))
print(f'Você digitou o número {numero.get(ext)}')
