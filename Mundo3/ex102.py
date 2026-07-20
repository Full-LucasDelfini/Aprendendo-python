def fatorial(num):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :return: O valor do fatorial de um número num
    """
    fat = 1
    for n in range(num, 0, -1):
        if n > 1:
            print(f'{n} x ', end='')
        else:
            print(f'{n} = ', end='')
        fat *= n
    return fat
valor = (int(input('Digite o número para descobrir o seu fatorial: ')))
print(fatorial(valor))
help(fatorial)