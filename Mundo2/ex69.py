maiores = homemtot = fmenores = 0
while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        entrada = str(input('Sexo [M/F]: ')).strip().upper()
        if entrada:
            sexo = entrada[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homemtot += 1
    if sexo == 'F' and idade < 20:
        fmenores += 1
    cont = ' '
    while cont not in 'SN':
        entrada_cont = str(input('Quer continuar? [S/N] ')).strip().upper()
        if entrada_cont:
            cont = entrada_cont[0]
    if cont == 'N':
        break
print('-' * 30)
print(f'O total de pessoas maiores de idade é {maiores}')
print(f'O total de homens cadastrados foi {homemtot}.')
print(f'O total de mulheres menores de 20 anos é {fmenores}')