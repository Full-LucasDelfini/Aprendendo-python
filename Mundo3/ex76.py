listagem_materias = ('LÁPIS', 1.0, 'BORRACHA', 2, 'CADERNO', 15.90, 'ESTOJO', 25.00,'TRANSFERIDOR', 4.20,
                     'COMPASSO', 9.99, 'MOCHILA', 120.32, 'CANETAS', 22.30, 'LIVRO', 34.90)
print('='*40)
print(f"{'LISTAGEM DE PREÇOS.':^40}")
print('='*40)
for pos in range(0,len(listagem_materias)):
    if pos % 2 == 0:
        print(f'{listagem_materias[pos]:.<30}',end='')
    else:
        print(f'{listagem_materias[pos]:>8.2f}')