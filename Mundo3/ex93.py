jogador = dict()
jogador['Nome'] = str(input('Nome: ')).capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
jogador['TotGols'] = list()
for i in range(jogador['Partidas']):
    Gols = int(input(f'quantos gols na {i+1}° partida? '))
    jogador['TotGols'].append(Gols)
jogador['Soma'] = sum(jogador['TotGols'])
print('=-'*20)
print(jogador)
print('=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('=-'*20)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas:')
for i, v in enumerate(jogador['TotGols']):
    print(f'=> Na partida {i+1}, fez {v} gol(s)')
print(f'Foi um total de {jogador["Soma"]} gol(s)')