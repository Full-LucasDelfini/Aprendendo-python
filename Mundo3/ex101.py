from datetime import datetime
def voto (ano):
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    if (idade >= 16 and idade < 18) or (idade >= 70):
        return f'Com {idade} anos: VOTO OPCIONAL!'
    if idade >= 18 and idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATORIO!'

anonasc = int(input('Digite o ano de nascimento: '))
print(voto(anonasc))