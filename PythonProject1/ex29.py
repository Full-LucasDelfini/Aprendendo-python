velo = float(input('Digite uma velocidade em km/h: '))
if velo > 80:
    multa = (velo - 80) * 7
    print(f'Você foi multado e pagará R$ {multa:.2f} pela velocidade de {velo}km/h')
else:
    print('Dessa vez você escapou! Sua velocidade foi abaixo de 80km/h!')