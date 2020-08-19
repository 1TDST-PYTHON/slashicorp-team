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
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("Para realizar a inscrição informe os seguintes dados: ")
        nome = input("Digite o nome do aluno: ")
        cpf = input("Digite seu CPF: ")
        ValidaCpf.validar(cpf)
        estado = str(input("Escolha o estado que deseja fazer o curso: ")).upper()
        ValidaEstado.validar_estado(estado)
        curso = input("Escolha um dos cursos disponíveis: ")
        nome.append(nome)
        cpf.append(cpf)
        estado.append(estado)
        curso.append(curso)
        print(aluno)
    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo cpf\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
            cpf.index(alteraInscricaoCpf)

        elif opcao1 == 2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        print("nada")
    elif menu == 4:
        print('Saindo...')
        break
    else:
        print("Opção Inválida")