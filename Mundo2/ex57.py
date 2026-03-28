gene = str(input("Digite seu sexo (M/F): ")).strip().upper()
while gene not in 'FM':
    gene = str(input('O gênero digitado não existe, digite um gênero entre (M/F): ')).strip().upper()
print(f'Sexo {gene} registrado com sucesso!')
