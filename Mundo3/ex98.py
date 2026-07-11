from time import sleep
def contador (inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = -passo
    print('-='*30)
    print(f'Contagem de inicio em {inicio} até {fim} de {passo} em {passo}.')
    sleep(1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ',end=' ')
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end=' ')
            sleep(0.5)
            cont -= passo
        print('FIM!')
contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 30)
print('Agora é sua vez de personalizar a contagem!')
comeco = int(input('Inicio: '))
final = int(input('Fim: '))
sequencia = int(input('Passo: '))
contador(comeco, final, sequencia)