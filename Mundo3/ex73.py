times = ('Palmeiras', 'Flamengo', 'São paulo', 'Fluminense', 'Bahia',
         'Atletico-PR', 'Coritiba', 'Atletico-MG', 'Bragantino', 'Vitoria',
         'Botafogo', 'Gremio', 'Vasco', 'Internacional', 'Santos',
         'Corinthians', 'Cruzeiro', 'Remo', 'Chapecoense' ,'Mirassol')
print(f'os primeiros colocados são {times[0:5]}')
print('*~*~'*30)
print(f'Os quatro últimos colocados são {times[-4:]}')
print('*~*~'*30)
print(f'Em ordem alfabêtica {sorted(times)}')
print(f'O Corinthians (melhor time do brasil) está em {times.index("Corinthians")+1}°')