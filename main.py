import cursoLista
import cpfValido
import estadoValido

codigo = []
nome = []
cpf = []
estado = []
curso = []
alunos = []
aluno_novo = []
sair = 0
i = 1000

dicionario = {
    "codigo": (codigo),
    "nome": (nome),
    "curso": (curso),
    "cpf": (cpf),
    "estado": (estado)
}

while (sair != 4):
    print('\nMenu')
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("\nInformações para a inscrição:")
        _nome = input("Nome do aluno: ")

        while not cpfValido.estaValido:
            _cpf = input("CPF: ")
            if _cpf in cpf:
                print("CPF já cadastrado.")
            else:
                cpfValido.validar(_cpf)

        _estado = ''
        while not estadoValido.estaValido:
            _estado = input("Estado que deseja fazer o curso: ").upper()
            estadoValido.validar(_estado)
        curso = cursoLista.cursos_por_estado(_estado)
        i += 1
        alunos.append([i, _nome, _cpf, _estado, curso])
        cpfValido.estaValido = False
        estadoValido.estaValido = False
    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo CPF\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
        elif opcao1 == 2:
            codigo_alteracao = int(input("Informe o código de inscrição: "))
            for aluno in alunos:
                if aluno[0] == codigo_alteracao:
                    novo_estado = input("Digite o novo estado: ")
                    estadoValido.validar(novo_estado)
                    aluno[3] = novo_estado

        else:
            print("Opção Inválida")
    elif menu == 3:
        for codigoimport, cursoimport in cursoLista.cursos.items():
            count = 0
            print(34 * '-')
            print(f" {codigoimport.ljust(0)} - {cursoimport}")
            for aluno in alunos:
                if codigoimport == aluno[4]:
                    print(34 * '-')
                    print(str(aluno[0]) + ' - ' + str(aluno[1]) + ' - ' + str(aluno[3]))
                    print(34 * '-')
                    count += 1
            if count > 0:
                print('Total de alunos: ', count, '\n')
            print(34 * '-')
            print(str(aluno) + ' - ' + str(nome) + ' - ' + str(estado))
            print(34 * '-')
            print('Total de alunos: ', len(codigo), '\n')
    # elif menu == 3:
    #     for codigo, nome in dicionario.items():
    #         print(34 * '-')
    #         print(f" {str(codigo).ljust(12)}{str(nome).ljust(12)}")
    #     print(34 * '-')
    #     print('Total de alunos: ', len(codigo), '\n')
    elif menu == 4:
        break
    else:
        print("Opção Inválida")
