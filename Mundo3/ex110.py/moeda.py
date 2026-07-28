def dobro(preço, formato=False):
    res = preço * 2
    return res if formato is False else (moeda(res))

def metade(preço,formato=False):
    res = preço / 2
    return res if formato is False else (moeda(res))

def aumentar(preço=0, porcentagem=0, formato=False):
    res = preço + (preço * porcentagem/100)
    return res if formato is False else (moeda(res))

def diminuir(preço=0, porcentagem=0, formato=False):
    res = preço - (preço * porcentagem / 100)
    return res if not formato else (moeda(res))

def moeda(preço=0, formate='R$'):
    return f'{formate}{preço:.2f}'.replace('.',',')

def resumo(preço=0, taxaau=10, taxare=5):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaau}% de aumento: \t{aumentar(preço, taxaau, True)}')
    print(f'{taxare}% de redução: \t{diminuir(preço, taxare, True)}')
