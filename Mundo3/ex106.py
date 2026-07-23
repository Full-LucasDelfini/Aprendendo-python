from time import sleep
c = ('\033[m',       # sem cores/limpa (0)
    '\033[0;107;41m', # vermelho (1)
    '\033[0;107;42m', # verde (2)
    '\033[0;107;43m', # amarelo (3)
    '\033[0;107;44m', # azul (4)
    '\033[0;107;45m', # roxo (5)
    '\033[0;107;30m' # branco (6)
     )

def ajuda (com):
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)

def titulo (msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1.5)

while True:
    comando = str(input('Função ou biblioteca: ')).strip()
    if comando.upper() == 'FIM':
        break
    titulo(f'Acessando o manual do comando "{comando}"...',5 )
    sleep(1.5)
    ajuda(comando)
titulo('Até mais!',1)