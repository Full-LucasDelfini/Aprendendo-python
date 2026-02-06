nome = str(input(f'Digite seu nome completo:')).strip()
print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(f' O total de letras é: {len(nome) - nome.count(' ')} letras')
print(f'O primeiro nome tem: {nome.find(' ')} letras')


