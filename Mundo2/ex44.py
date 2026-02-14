from time import sleep
nome = str(input('Olá, como você se chama? ')).strip().capitalize()
valor = float(input(f'Qual o valor do produto, {nome}? R$: '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] - À vista (dinheiro, pix ou cheque)      
[ 2 ] - À vista no cartão
[ 3 ] - No cartão em 2x
[ 4 ] - No cartão em 3x ou mais''')
opcao = int(input('Teria interesse em qual opção? '))
print('PROCESSANDO...')
sleep(1.5)
if opcao == 1:
    print(f'Perfeito, {nome}! Pagamentos à vista em dinheiro, pix ou cheque temos 10% de desconto:R$ {valor*0.9:.2f}')
elif opcao == 2:
    print(f'Ótimo, {nome}! Para pagamentos à vista no cartão temos 5% de desconto: R$ {valor*0.95:2f}')
elif opcao == 3:
    print(f'Para parcelamentos em até 2x conseguimos prosseguir sem juros adicionais, {nome}! R$: 2X {valor/2:.2f}')
elif opcao == 4:
    print(f'Para parcelamentos em até 3x ou mais, cobramos 20% de juros,{nome}! ficará R$:{valor*1.2:2f}')
else:
    print(f'\033[1;31m ERRO! Temos apenas 4 opções de pagamento, {nome}!\033[m')