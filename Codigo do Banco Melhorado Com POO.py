class Menu:
    @staticmethod
    def mostrar():
        print('''    
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
            ''')


class Cliente:
    cadastros = []

    @classmethod
    def filtrar_cadastros(cls, cpf):
        return any(cpf == cadastro['Cpf'] for cadastro in cls.cadastros)

    @staticmethod
    def depositar(dinheiro, saldo, extrato):
        valor = float(input('Digite o quanto gostaria de depositar: R$ '))
        if valor > 0:
            dinheiro += valor
            saldo = dinheiro
            extrato.append(f'Depósito: R$ {valor:.2f} | Saldo: R$ {dinheiro:.2f}')
            print("\nDepósito realizado com sucesso.")
        else:
            print('\nSó aceitamos valores de depósitos positivos.')
        return dinheiro, saldo, extrato

    @staticmethod
    def ver_extrato(dinheiro, extrato):
        if not extrato:
            print('\n\tNão foram realizadas movimentações.\n')
        else:
            for valor in extrato:
                print(f'\t\t{valor}')
            print(f'\t\tSaldo total = R$ {dinheiro:.2f}')

    @classmethod
    def criar_conta(cls, contas):
        cpf = input('Digite o seu CPF: ')
        if cls.filtrar_cadastros(cpf):
            cadastro = cls.cadastros[-1]
            conta = {'cadastro': cadastro, 'AGENCIA': '0001'}
            contas.append(conta)
            print("\nConta criada com sucesso.")
        else:
            print(f'\nUsuário com CPF {cpf} não encontrado. Cadastre um usuário com esse CPF primeiro!')

    @classmethod
    def filtrar_contas(cls, cpf, contas):
        return any(cpf == conta['cadastro']['Cpf'] for conta in contas)

    # Outras funções mantidas iguais


class Main(Cliente):
    def __init__(self):
        super().__init__()
        self.contas = []
        self.extrato = []
        self.dinheiro = 0
        self.n_saques = 0
        self.saldo = 0
        self.cpf = None

    def executar(self):
        while True:
            Menu.mostrar()
            escolher_operacao = input("Escolha uma das opções do Menu acima: ").lower()
            if escolher_operacao in ['s', 'd', 'e']:
                self.cpf = input('Digite o seu CPF: ')
                if not self.filtrar_cadastros(self.cpf):
                    print('\nUsuário com CPF não encontrado.')
                    continue

                if self.filtrar_contas(self.cpf, self.contas):
                    if escolher_operacao == 's':
                        self.dinheiro, self.n_saques, self.extrato, self.saldo = self.sacar(
                            self.dinheiro, self.n_saques, self.extrato, self.saldo)
                    elif escolher_operacao == 'd':
                        self.dinheiro, self.saldo, self.extrato = self.depositar(
                            self.dinheiro, self.saldo, self.extrato)
                    elif escolher_operacao == 'e':
                        self.ver_extrato(self.dinheiro, self.extrato)
                else:
                    print('\nUsuário com conta não encontrada.')

            elif escolher_operacao == 'c':
                self.cadastrar()
            elif escolher_operacao == 'cc':
                self.criar_conta(self.contas)
            elif escolher_operacao == 'lc':
                self.listar_conta()
            elif escolher_operacao == 'p':
                break
            else:
                print(f'\nOpção inválida, preste atenção nas teclas pedidas no Menu!')

    def listar_conta(self):
        if not self.contas:
            print('\nNenhuma conta criada ainda.')
            return

        print('\nLista de Contas:')
        for i, conta in enumerate(self.contas, start=1):
            print(f"Conta {i}:")
            print(f"CPF do Titular: {conta['cadastro']['Cpf']}")
            print(f"AGÊNCIA: {conta['AGENCIA']}")
            print("-" * 30)

    @staticmethod
    def sacar(dinheiro, n_saques, extrato, saldo):
        if n_saques >= 3:
            print("\nLimite máximo de saques atingido (3 saques).")
            return dinheiro, n_saques, extrato, saldo

        while True:
            try:
                valor = float(input('Digite o valor que gostaria de sacar: R$ '))
                if valor <= 0:
                    raise ValueError
                if valor > saldo:
                    print("\nSaldo insuficiente.")
                    return dinheiro, n_saques, extrato, saldo
                if valor > 500:
                    print("\nLimite máximo de saque por vez é de R$500.")
                    return dinheiro, n_saques, extrato, saldo
                break
            except ValueError:
                print('\nPor favor, digite um valor válido (positivo).')

        dinheiro -= valor
        saldo -= valor
        n_saques += 1
        extrato.append(f'Saque: R$ {valor:.2f} | Saldo: R$ {dinheiro:.2f}')
        print("\nSaque realizado com sucesso.")
        return dinheiro, n_saques, extrato, saldo

    def cadastrar(self):
        cpf = input('Digite o CPF: ')
        if not self.filtrar_cadastros(cpf):
            cadastro = {
                'Cpf': cpf,
                'Nome': input('Nome: '),
                'Idade': input('Idade: '),
                'Endereço': input('Endereço: '),
                'DataNascimento': input('Data de Nascimento (dd/mm/aaaa): ')
            }
            self.cadastros.append(cadastro)
            print(f'\nUsuário cadastrado com sucesso!')
        else:
            print(f'\nJá existe um usuário cadastrado com esse CPF!')


if __name__ == "__main__":
    banco = Main()
    banco.executar()
