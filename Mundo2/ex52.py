numero = int(input('Digite um número para verificar se ele é primo: '))
total_divisores = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        total_divisores += 1

if total_divisores == 2:
    print(f'O número digitado "{numero}" é primo!')
else:
    print(f'O número digitado "{numero}" não é primo!')
