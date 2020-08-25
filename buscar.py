def buscar(pessoas):
    identificador_desejado = input('Id? ')
    for pessoa in pessoas:
        identificador, nome, cpf, estado, curso = pessoa
        if identificador == identificador_desejado:
            print(f'Nome: {nome}, CPF: {cpf}, ID: {identificador}, Estado: {estado}, Curso: {curso} ')
            break
            
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')
