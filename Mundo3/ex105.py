def notas(*val, sit=False):
        dados = dict()
        dados['total'] = len(val)
        dados['maior'] = max(val)
        dados['menor'] = min(val)
        soma = 0
        for n in val:
            soma += n
        media = (soma / len(val))
        dados['media'] = media
        if sit:
            if media > 5:
                dados['situacao'] ='BOA'
            elif media == 5:
                dados['situacao'] ='RAZOÁVEL'
            else:
                dados['situacao'] ='RUIM'
        return dados

resultado = notas(5, 10, 9, 5, 8, sit=True)
print(resultado)