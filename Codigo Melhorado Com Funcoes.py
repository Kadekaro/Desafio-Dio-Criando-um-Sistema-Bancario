def Menu():
    menu = '''    
    Seja bem vindo(a) ao menu do Banco:
        |======== MENU ========|
        |    [S] = Sacar       |
        |    [D] = Depositar   |
        |    [E] = Extrato     |
        |    [C] = Cadastrar   |
        |   [CC] = Criar Conta |
        |   [LC] = Listar Conta|
        |    [P] = Sair        |
        |======================|
        '''
    print(menu)


def main():
    contas = []
    cadastros = []
    extrato = []
    dinheiro = 0
    n_saques = 0
    saldo = 0

    while True:
        Menu()
        escolher_operacao = input("Escolha uma das opções do Menu acima: ").lower()
        if escolher_operacao == 's':
            # Essa parte atualiza a variável extrato e dinheiro, fora do escopo das funções sacar e depositar
            dinheiro, n_saques, extrato, saldo = sacar(dinheiro=dinheiro,
                                                       n_saques=n_saques,
                                                       extrato=extrato,
                                                       saldo=saldo)
        elif escolher_operacao == 'd':
            # Essa parte atualiza a variável extrato e dinheiro, fora do escopo das funções sacar e depositar
            dinheiro, saldo, extrato = depositar(dinheiro, saldo, extrato)
        elif escolher_operacao == 'e':
            ver_extrato(dinheiro, extrato=extrato)
        elif escolher_operacao == 'c':
            cadastros = cadastrar(cadastros)
        elif escolher_operacao == 'cc':
            cadastros, contas = criar_conta(cadastros, contas)
        elif escolher_operacao == 'lc':
            cpf, cadastros = listar_conta(cadastros)
            if cpf is not None:
                for cadastro in cadastros:
                    if cadastro['Cpf'] == cpf:
                        print(cadastro)
        elif escolher_operacao == 'p':
            break
        else:
            print(f'\nOpção inválida, preste atenção nas teclas pedidas no Menu!')


def sacar(*, dinheiro, n_saques, extrato, saldo):
    while True:
        try:
            valor = float(input('Digite o quanto gostaria de sacar: R$ '))
            if valor <= 0:
                raise ValueError
            break
        except ValueError:
            print('\nPor favor, digite um valor válido (positivo).')

    if valor > dinheiro:
        print(f'\nVocê não possui dinheiro suficiente em conta!')
    elif valor > dinheiro and n_saques >= 3:
        print('\nVocê não possui dinheiro suficiente em conta eo limite de saque é de R$ 500,00.')
    elif n_saques >= 3:
        print(f'\nVocê atingiu o limite de saque diário!')
        print(f'\tO seu saldo é de: R$ {dinheiro:.2f}')
    elif valor > 500:
        print('\nO limite de saque é de R$ 500,00.')
    elif n_saques < 3 and valor <= 500:
        n_saques += 1
        dinheiro -= valor
        extrato.append(f'R$ {saldo:.2f} - R$ {valor:.2f} = R$ {dinheiro:.2f} ')
        if dinheiro >= 0:
            saldo = dinheiro
        print()
        ver_extrato(dinheiro, extrato=extrato)

    return dinheiro, n_saques, extrato, saldo


def depositar(dinheiro, saldo, extrato, /):
    while True:
        try:
            valor = float(input('Digite o quanto gostaria de depositar: R$ '))
            if valor <= 0:
                raise ValueError
            break
        except ValueError:
            print('\nPor favor, digite um valor válido (positivo).')

    if valor > 0:
        dinheiro += valor
        extrato.append(f'R$ {saldo} + R$ {valor:.2f} = R$ {dinheiro:.2f}')
        saldo = dinheiro
        print()
        ver_extrato(dinheiro, extrato=extrato)
    else:
        print('\nSó aceitamos valores de depósitos positivos.')
    return dinheiro, saldo, extrato


def ver_extrato(dinheiro, /, *, extrato):
    if len(extrato) == 0:
        print('\n\tNão foram realizadas movimentações.\n')
    for valores in extrato:
        print(f'\t\t{valores}')
    print(f'\t\tSaldo total = R$ {dinheiro:.2f}')


def cadastrar(cadastros):
    cpf = input('Digite o seu CPF: ')
    if filtrar_cadastros(cpf, cadastros):
        print(f'\nJá existe um usuário cadastrado com esse CPF!')
        return cadastros

    cadastro = {
        'Cpf': cpf,
        'Nome': input('Nome: '),
        'Idade': input('Idade: '),
        'Endereço': input('Endereço: '),
        'DataNascimento': input('Data de Nascimento(dd/mm/aaaa): ')
    }
    cadastros.append(cadastro)
    print(f'\n === Usuário cadastrado com sucesso! === ')
    return cadastros


def criar_conta(cadastros, contas):
    while True:
        cpf = input('Digite o seu CPF: ')
        if not cadastros:
            print('\n== Cadastre um usuário antes de criar uma conta! ==')
        elif filtrar_contas(cpf, contas):
            print(f'\nJá existe um usuário cadastrado com uma conta nesse CPF!')
        elif filtrar_cadastros(cpf, cadastros):
            cadastro = cadastros[-1]
            conta = {
                'cadastro': cadastro,
                'AGENCIA': '0001',
            }
            contas.append(conta)
            print(contas)
            print(f"\n == Conta criada com sucesso == ")
        else:
            print(f'\nUsuário com CPF {cpf} não encontrado. Cadastre um usuário com esse CPF primeiro!')
        return cadastros, contas


def filtrar_cadastros(cpf, cadastros):
    for cadastro in cadastros:
        if cpf == cadastro['Cpf']:
            return True
    return False


def filtrar_contas(cpf, contas):
    for conta in contas:
        if cpf == conta['cadastro']['Cpf']:
            return True
    return False


def listar_conta(cadastros):
    cpf = input('Digite o seu CPF: ')
    for i, cadastro in enumerate(cadastros):
        if cadastro['Cpf'] == cpf:
            return cpf, cadastros
    print('CPF não encontrado. Tente novamente.')
    return None, cadastros


main()
