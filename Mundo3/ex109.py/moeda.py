def dobro (preço, formato=False):
    res = preço * 2
    return res if formato is False else (moeda(res))

def metade (preço,formato=False):
    res = preço / 2
    return res if formato is False else (moeda(res))

def aumentar (preço=0, porcentagem=0, formato=False):
    res = preço + (preço * porcentagem/100)
    return res if formato is False else (moeda(res))

def diminuir (preço=0, porcentagem=0, formato=False):
    res = preço - (preço * porcentagem / 100)
    return res if not formato else (moeda(res))

def moeda (preço=0, formate='R$'):
    return f'{formate}{preço:.2f}'.replace('.',',')
