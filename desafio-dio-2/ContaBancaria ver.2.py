import textwrap


def menu():
    menu = '''
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nc] Nova conta
        [lc] Listar contas
        [nu] Novo usuário
        [q] Sair
        => '''
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'\tDepósito: R$ {valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite.')
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'\tSaque: R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print('\n====================== EXTRATO ======================')
    print('\tNão foram realizadas movimentações.' if not extrato else extrato)
    print(f'\n\tSaldo: R$ {saldo:.2f}')
    print('======================')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Existe usuário com este CPF!')

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereco (logradouro, nro = bairro - cidade/sigla estado): ')
    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereco})
    print('====> usuário criado com sucesso!')


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n====> Conta Criada com sucesso!')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    print('\nUsuárionão encontrado --- Fluxo de criação de conta encerrado!')


def listar_contas(contas):
    for conta in contas:
        linha = f"""
                AGENCIA:\t{conta['agencia']}
                C/C:\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
        """
        print('='*100)
        peint(textwrap.dedent(linha))


def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor de depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor de saque: '))
            saldo, extrato = sacar(saldo, valor, extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
        else:
            print('Operação falhou! O valor informado é inválido!')
