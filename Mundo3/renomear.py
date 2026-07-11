import os
import re

PASTA = '.'
DIGITOS = 3

padrao = re.compile(r'^ex(\d+)\.py$')

for nome_arquivo in os.listdir(PASTA):
    match = padrao.match(nome_arquivo)
    if match:
        numero = int(match.group(1))
        novo_nome = f'ex{numero:0{DIGITOS}d}.py'
        if novo_nome != nome_arquivo:
            os.rename(nome_arquivo, novo_nome)
            print(f'{nome_arquivo} -> {novo_nome}')

print('Concluído!')