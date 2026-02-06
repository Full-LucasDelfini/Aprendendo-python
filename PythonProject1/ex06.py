n1 = float(input('Digite uma nota:'))
n2 = float(input('Digite outra nota:'))
print(f'O valor das notas somadas é: {n1+n2} e sua média:{(n1+n2)/2:.1f}')
media = (n1+n2)/2
if media >= 6:
    print('Parabéns, você foi aprovado!')
else:
    print('Infelizmente você foi reprovado!')



