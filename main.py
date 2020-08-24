import cursoLista
import cpfValido
import estadoValido

codigo = []
nome = []
cpf = []
estado = []
curso = []
alunos = []
sair = 0
# a variável i é utilizada como iteração para gerar o código de inscrição automático
i = 1000

while (sair != 4):
    print('\nMenu')
    menu = int(input("\t1. Fazer Inscrição\t\n2. Alterar Inscrição\t\n3. Listar Inscrições\t\n4. Sair\n=> "))
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
        # recebe o retorno do curso da função cursos_por_estado
        curso = cursoLista.cursos_por_estado(_estado)
        # incrementa para gerar o código da nova inscrição
        i += 1
        # adiciona inscrição a lista alunos
        alunos.append([i, _nome, _cpf, _estado, curso])
        cpfValido.estaValido = False
        estadoValido.estaValido = False
    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo CPF\n2. Alterar inscrição pelo código de inscrição\n=> "))
        if opcao1 == 1:
            cpf_alteracao = int(input("Informe seu CPF: "))
            # o loop abaixo irá verificar aluno por aluno na lista alunos
            for aluno in alunos:
                # verifica quando chega no cpf digitado
                if aluno[2] == cpf_alteracao:
                    novo_estado = input("Digite o novo estado: ")
                    estadoValido.validar(novo_estado)
                    # troca o estado 
                    aluno[3] = novo_estado
        elif opcao1 == 2:
            codigo_alteracao = int(input("Informe o código de inscrição: "))
            # o loop abaixo irá verificar aluno por aluno na lista alunos
            for aluno in alunos:
                # verifica quando chega no codigo digitado
                if aluno[0] == codigo_alteracao:
                    novo_estado = input("Digite o novo estado: ")
                    estadoValido.validar(novo_estado)
                    # troca o estado
                    aluno[3] = novo_estado

        else:
            print("Opção Inválida")
    elif menu == 3:
        for codigoimport, cursoimport in cursoLista.cursos.items():
            # a variável a baixo irá contabilizar a quantidade de alunos por curso
            qtd = 0
            # head da visualização
            print(34 * '-')
            print(f" {codigoimport.ljust(0)} - {cursoimport}")
            # o for irá exibir aluno por aluno de acordo com o curso
            for aluno in alunos:
                if codigoimport == aluno[4]:
                    print(34 * '-')
                    print(str(aluno[0]) + ' - ' + str(aluno[1]) + ' - ' + str(aluno[3]))
                    print(34 * '-')
                    qtd += 1
            # exibe apenas se a qtd total de inscritos for maior que 0                
            if qtd > 0:
                print('Total de inscritos: ', qtd, '\n')
    elif menu == 4:
        break
    else:
        print("Opção Inválida")