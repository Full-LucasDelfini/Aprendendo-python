from time import sleep
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
azul = '\033[1;34m'
roxo = '\033[1;35m'
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'{azul} Os {vermelho} fogos {verde} de {amarelo} artifício {roxo} estouraram!!!')


