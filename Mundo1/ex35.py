r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
azul = '\033[1;34;107m'
vermelho ='\033[1;31;107m'
verde = '\033[1;32;107m'
limpa = '\033[m'
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {azul} {r1:.1f} {limpa},{vermelho} {r2:.1f} {limpa} e {verde} {r3:.1f} {limpa} formam um tríangulo!')
else:
    print(f'As retas {azul} {r1:.1f} {limpa},{vermelho} {r2:.1f} {limpa} e {verde} {r3:.1f} {limpa} não formam um tríangulo!')