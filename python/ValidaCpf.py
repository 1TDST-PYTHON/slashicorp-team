def verificar_cpf(cpf, digitos):
    if len(cpf) != digitos:
        return False
    else:
        j = ((10 * int(cpf[0])) + (9 * int(cpf[1])) + (8 * int(cpf[2])) + (7 * int(cpf[3])) + (6 * int(cpf[4])) \
             + (5 * int(cpf[5])) + (4 * int(cpf[6])) + (3 * int(cpf[7])) + (2 * int(cpf[8]))) % 11
        if j < 2:
            digitoj = 0
        else:
            digitoj = 11 - j
        k = ((11 * int(cpf[0])) + (10 * int(cpf[1])) + (9 * int(cpf[2])) + (8 * int(cpf[3])) + (7 * int(cpf[4])) \
             + (6 * int(cpf[5])) + (5 * int(cpf[6])) + (4 * int(cpf[7])) + (3 * int(cpf[8])) + (2 * digitoj)) % 11
        if k < 2:
            digitok = 0
        else:
            digitok = 11 - k
    return str(digitoj) + str(digitok)

# Nova versão do IF para validação do CPF.
'''
def validar(cpf):
    vercpf = verificar_cpf(cpf, 11)
    if (cpf[9] == vercpf[0] and cpf[10] == vercpf[1]):
        print("CPF válido!")
        validate = True
    else:
        print("CPF inválido!")
        return vercpf
        validate = False'''

# Versão antiga do IF para validação do CPF.

def validar(cpf):
    validate = False
    while (validate == False):
        cpf = input("Digite um CPF do aluno: ")
        vercpf = verificar_cpf(cpf, 11)
        if (vercpf == False):
            print("CPF inválido")
            validate = False
        elif cpf[9] == vercpf[0] and cpf[10] == vercpf[1]:
            print("CPF válido!")
            validate = True
        else:
            print("CPF inválido!")
            validate = False



'''---------------------'''

'''def validar():
    print("Digite o número do CPF com os dígitos verificadores. Somente os números.")
    cpf = input("CPF:")
    vercpf = verificar_cpf(cpf, 11)
    if (vercpf == False):
        print("CPF inválido")
    elif cpf[9] == vercpf[0] and cpf[10] == vercpf[1]:
        print("CPF válido!")
    else:
        print("CPF inválido!")
validar()'''