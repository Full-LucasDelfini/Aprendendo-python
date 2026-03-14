from time import sleep
maior = 0
menor = 0
posicaomaior = 0
posicaomenor = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}° pessoa em Kg: '))
    if c == 1:
       maior = peso
       menor = peso
       posicaomaior = c
       posicaomenor = c
    else:
        if peso > maior:
            maior = peso
            posicaomaior = c
        if peso < menor:
            menor = peso
            posicaomenor = c
sleep(0.5)
print('-='*65)
print('CARREGANDO...')
sleep(2.0)
if posicaomaior == posicaomenor:
    print('ERRO! não existe peso maior ou menor, pois os pesos digitados são iguais!')
else:
    print(f'O maior peso digitado foi o da {posicaomaior:.0f}° pessoa, que corresponde a {maior}Kg!')
    print(f'O menor peso digitado foi o da {posicaomenor:.0f}° pessoa, que corresponde a {menor}Kg!')
