def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        else:
            return num
def leiafloat(msg):
    while True:
        texto = input(msg).strip()
        texto = texto.replace(',','.')
        try:
            n = float(texto)
        except(ValueError, TypeError):
            print('ERRO! Digite um número real válido.')
            continue
        else:
            return n
num = leiaint('Digite um número inteiro: ')
n = leiafloat('Digite um número real: ')
print(f'Os valores digitados foram inteiro={num}, real={n}')