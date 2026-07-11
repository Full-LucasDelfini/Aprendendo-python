dados = list()
pessoa = dict()
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['Gênero'] = str(input('Gênero[M/F]: ')).strip().upper()[0]
    while pessoa['Gênero'] not in 'MF':
        print('Tente novamente, por favor! Digite apenas M ou F.')
        pessoa['Gênero'] = str(input('Gênero[M/F]: ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    dados.append(pessoa.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
totcadastro = len(dados)
print(f'Ao todo foram cadastrados {totcadastro} pessoas.')
soma = 0
for p in dados:
    soma += p['Idade']
media = soma / len(dados)
print(f'- A média de idades é: {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['Gênero'] == 'F':
        print(f'{p["Nome"]}', end='')
print()
print(f'- As pessoas com idade acima da média foram: ', end='')
for p in dados:
    if p['Idade'] > media:
        print(f'   nome = {p["Nome"]}; gênero = {p["Gênero"]}; idade = {p["Idade"]};', end=' ')
print()
print('<=> ENCERRANDO <=>')