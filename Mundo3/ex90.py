aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
aluno['media'] = float(input('Digite a media do aluno: '))
if aluno['media'] >= 6:
    aluno['situacao'] = 'APROVADO!'
else:
    aluno['situacao'] = 'REPROVADO!'
print(f'O nome é igual a: {aluno["nome"]}')
print(f'A média é igual a: {aluno["media"]:g}')
print(f'A situação é igual a: {aluno["situacao"]}')