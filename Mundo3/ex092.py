from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Nascimento'] = int(input('Ano de nascimento: '))
dados['CTPS'] = (int(input(f'Carteira de trabalho: (0 caso não tenha) ')))
dados['idade'] = datetime.now().year - dados['Nascimento']
if dados['CTPS'] != 0:
    dados['Contrato'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    idade_contrato = dados['Contrato'] - dados['Nascimento']
    dados['Aposentadoria'] = idade_contrato + 35
print('='*35)
for k, v in dados.items():
    print(f' - {k} tem o valor de: {v}')