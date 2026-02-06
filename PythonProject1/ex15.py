km = float(input('Quantos quilometros foram percorridos?'))
dia = int(input('Quantos dias o carro foi alugado?'))
soma = (km * 0.15) + (dia * 60)
print(f'O valor total à ser pago é de:R${soma:.2f}')