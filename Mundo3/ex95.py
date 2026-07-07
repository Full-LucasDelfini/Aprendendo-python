time = list()
jogadores = dict()
while True:
    jogadores.clear()
    jogadores['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    jogadores['partidas'] = int(input(f'Quantas partidas {jogadores["Nome"]} jogou: '))
    gols_partida = list()
    for g in range(jogadores["partidas"]):
        gol = int(input(f'  -> Quantos gols na {g + 1}° partida: '))
        gols_partida.append(gol)
    jogadores['Gols'] = gols_partida[:]
    jogadores['totgols'] = sum(gols_partida)
    time.append(jogadores.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 45)
    if resp == 'N':
        break
print('-=' * 25)
print(f'{"cod":<5} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 45)
for i, v in enumerate(time):
    gols_str = str(v["Gols"])
    print(f'{i:<5} {v["Nome"]:<15} {gols_str:<15} {v["totgols"]:<5}')
print('-' * 45)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, gols in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i + 1} fez {gols} gols.')
    print('-' * 45)
print('<< VOLTE SEMPRE >>')