import CursosPorEstado
import ValidaEstado
import ValidaCpf
 
nome = []
cpf = []
estado = []
curso = []
aluno = [nome, cpf, estado, curso]
sair = 0
while (sair != 4):
    print('Menu')
    menu = int(input("\n1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("\nInformações para a inscrição: ")
        _nome = input("Nome do aluno: ")
        ValidaCpf.validar()
        ValidaEstado.validar_estado()
        CursosPorEstado.cursos_por_estado(ValidaEstado.estado)
        _curso = input("Escolha um dos cursos disponíveis: ")
        nome.append(_nome)
        cpf.append(str(ValidaCpf.cpf))
        estado.append(str(ValidaEstado.estado))
        curso.append(_curso)
        print(aluno)
    elif menu == 2:
        opcao1 = int(input("[1] Alterar inscrição pelo CPF\n[2] Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
            cpf.index(alteraInscricaoCpf)

        elif opcao1 == 2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        print('Em andamento...')
    elif menu == 4:
        print('Saindo...')
        break
    else:
        print("Opção Inválida")
        
