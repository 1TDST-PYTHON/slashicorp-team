import cursoLista
import cpfValido
import estadoValido

cpf = []
curso = []
alunos = []
sair = 0
i = 1000

while (sair != 4):
    print('\nMenu')
    menu = int(input("\t1. Fazer Inscrição\n\t2. Alterar Inscrição\n\t3. Listar Inscrições\n\t4. Sair\n=> "))
    if menu == 1:
        voltar = 0
        while (voltar != 2):
           print("1. Continuar   2. Voltar")
           menu =int(input("=> "))
           if menu == 1:
               print("\nInformações para a inscrição:")
               _nome = input("Nome do aluno: ")
               while not cpfValido.estaValido:
                   _cpf = input("CPF: ")
                   if _cpf in cpf:
                       print("\033[31mCPF já cadastrado.\033[m")
                   else:
                       cpfValido.validar(_cpf)
               _estado = ''
               while not estadoValido.estaValido:
                   _estado = input("Estado que deseja fazer o curso: ").upper()
                   estadoValido.validar(_estado)
               curso = cursoLista.cursos_por_estado(_estado)
               i += 1
               alunos.append([i, _nome, _cpf, _estado, curso])
               cpf.append(_cpf)
               cpfValido.estaValido = False
               estadoValido.estaValido = False
               print("\nCódigo da inscrição: ", i, "\nInscrição finalizada!")
           else:
               break

    elif menu == 2:
        voltar = 0
        while (voltar != 2):
            print("1. Continuar   2. Voltar")
            menu = int(input("=> "))
            if menu == 1:
                opcao1 = int(
                    input("\t1. Alterar inscrição pelo CPF\n\t2. Alterar inscrição pelo código de inscrição\n=> "))
                if opcao1 == 1:
                    cpf_alteracao = input("Informe seu CPF: ")
                    for aluno in alunos:
                        if aluno[2] == cpf_alteracao:
                            novo_estado = input("Digite o novo estado: ").upper()
                            estadoValido.validar(novo_estado)
                            novo_curso = cursoLista.cursos_por_estado(novo_estado)
                            aluno[3] = novo_estado
                            aluno[4] = novo_curso
                            print("\n\033[32mAlteração finalizada com sucesso!\033[m")
                elif opcao1 == 2:
                    codigo_alteracao = int(input("Informe o código de inscrição: "))
                    for aluno in alunos:
                        if aluno[0] == codigo_alteracao:
                            novo_estado = input("Digite o novo estado: ").upper()
                            estadoValido.validar(novo_estado)
                            novo_curso = cursoLista.cursos_por_estado(novo_estado)
                            aluno[3] = novo_estado
                            aluno[4] = novo_curso
                            print("\nAlteração finalizada!")
                else:
                    print("\033[31mOpção Inválida\033[m")
            else:
                break

    elif menu == 3:
        for codigoimport, cursoimport in cursoLista.cursos.items():
            qtd = 0
            print(34 * '-')
            print(f" {codigoimport.ljust(0)} - {cursoimport}")
            for aluno in alunos:
                if codigoimport == aluno[4]:
                    print(34 * '-')
                    print(str(aluno[0]) + ' - ' + str(aluno[1]) + ' - ' + estadoValido.encontraCapital(aluno[3]))
                    print(34 * '-')
                    qtd += 1
            print('\nTotal de inscritos: ', qtd, '\n')

    elif menu == 4:
        break
    else:
        print("\033[31mOpção Inválida\033[m")
