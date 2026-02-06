nome = str(input('Digite o nome da sua cidade:')).strip()
santo = nome.capitalize().startswith('Santo')
#print(santo)
print(nome[:5].upper() == 'SANTO')
