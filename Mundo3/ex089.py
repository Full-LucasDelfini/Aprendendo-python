alunos = []
maior = soma = 0
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' *30)
for i, a in enumerate(alunos):
    print(f'{i:<4} {a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opcao = int(input('Quer mostrar a nota de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')