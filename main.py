import cpfValido
import estadoValido
import cursoLista

codigo = []
nome = []
cpf = []
estado = []
curso = []
aluno = [[codigo], [nome], [cpf], [estado], [curso]]
# aluno = {'codigo': [codigo], 'nome': [nome], 'cpf': [cpf], 'estado': [estado], 'curso': [curso]}
sair = 0
i = 0

while (sair != 4):
    print('\nMenu')
    menu = int(input("1. Fazer Inscrição\n2. Alterar Inscrição\n3. Listar Inscrições\n4. Sair\n:"))
    if menu == 1:
        print("\nInformações para a inscrição:")
        _nome = input("Nome do aluno: ")
        _cpf = 0
        while not cpfValido.estaValido:
            _cpf = input("CPF: ")
            cpfValido.validar(_cpf)
        _estado = ''
        while not estadoValido.estaValido:
            _estado = input("Estado que deseja fazer o curso: ").upper()
            estadoValido.validar(_estado)
        cursoLista.cursos_por_estado(_estado)
        i = i + 1
        codigo.append(i)
        nome.append(_nome)
        cpf.append(_cpf)
        estado.append(_estado)
        cpfValido.estaValido= False
        estadoValido.estaValido = False
        
    elif menu == 2:
        opcao1 = int(input("1. Alterar inscrição pelo CPF\n2. Alterar inscrição pelo código de inscrição\n:"))
        if opcao1 == 1:
            alteraInscricaoCpf = int(input("Informe seu CPF: "))
        elif opcao1 == 2:
            alteraInscricaoCD = int(input("Informe o código de inscrição: "))
        else:
            print("Opção Inválida")
    elif menu == 3:
        for codigoimport, cursoimport in cursoLista.cursos.items():
            print(34 * '-')
            print(f" {codigoimport.ljust(0)} - {cursoimport}")
            print(34 * '-')
            # print( """id + ' - ' + """ , _nome + ' - ' + _estado)
            print(34 * '-')
            print('Total de alunos: ', len(aluno[0]), '\n')

    elif menu == 4:
        break
    else:
        print("Opção Inválida")
