gender = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while gender not in 'MmFf':
   gender = str(input('Dados invalidos. Por favor, infome o seu sexo [M/F]:')).strip().upper()[0]
print('Sexo {} Registrado com sucesso'.format(gender))