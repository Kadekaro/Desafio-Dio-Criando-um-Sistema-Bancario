menu = '''
        ================================= MENU ===================================
        [Sacar]: Para sacar, aperte "s" no seu teclado.
        [Depositar]: Para depositar, aperte "d" no seu teclado.
        [Extrato]: Para ver o extrato, aperte "e" no seu teclado.
        Para voltar e fazer outra operação, aperte "v" no seu teclado.
        Para encerrar suas operações neste terminal, aperte "p" no seu teclado.
        ===========================================================================
'''
extrato = []
dinheiro = 0
n_saques = 0

print(menu)

escolher_Operacao = input().lower()

while escolher_Operacao != 'p':
    if escolher_Operacao == 's':
        sacar = float(input('Digite o quanto gostaria de sacar: R$ '))
        if sacar > dinheiro:
            print(f'Não é possível sacar, você está sem dinheiro, faça um depósito!')
            escolher_Operacao = input().lower()
        elif n_saques < 3 and sacar <= 500:
            n_saques += 1
            dinheiro -= sacar
            extrato.append(f'- {sacar:.2f} = {dinheiro:.2f} ')
        elif n_saques >= 3:
            print(f'Você atingiu o limite de saque diário!')
            for saldo in extrato:
                print(f'{saldo}')
            print(f'  Saldo total {dinheiro:.2f}')
            break
        elif sacar > 500:
            print('O limite de saque é de R$ 500,00.')
            continue

    elif escolher_Operacao == 'd':
        depositar = float(input('Digite o quanto gostaria de depositar: R$ '))
        if depositar >= 0:
            dinheiro += depositar
            extrato.append(f'+ {depositar:.2f} = {dinheiro:.2f}')
        else:
            print('Só aceitamos valores de depósitos positivos.')
            continue

    elif escolher_Operacao == 'v':
        print(menu)

    elif escolher_Operacao == 'e':
        if len(extrato) == 0:
            print('Não foram realizadas movimentações.')
            for saldo in extrato:
                print(f'{saldo}')
        print(f'Saldo total = {dinheiro:.2f}')

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')

    escolher_Operacao = input().lower()

print('Operações encerradas.')