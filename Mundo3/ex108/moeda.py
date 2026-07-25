def dobro (preço):
    return preço * 2

def metade (preço):
    return preço / 2

def aumentar (preço=0, porcentagem=0):
    return preço + (preço * porcentagem/100)

def diminuir (preço=0, porcentagem=0):
    return preço - (preço * porcentagem/100)

def moeda (preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')