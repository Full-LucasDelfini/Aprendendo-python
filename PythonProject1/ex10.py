lg = float(input('Qual é a largura em metros?'))
al = float(input('Qual é a altura em metros?'))
area = lg * al
pin = area / 2
print(f'Sua área total é {area:.2f}m²',end= ' ')
print(f'e será necessário {pin:.2f}l de tinta para pintar')