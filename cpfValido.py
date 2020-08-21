estaValido = False


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


def validar(cpf):
    global estaValido
    vercpf = verificar_cpf(cpf, 11)
    if (vercpf == False):
        print("\033[31mCPF inválido\033[m")

    elif cpf[9] == vercpf[0] and cpf[10] == vercpf[1]:
        print("\033[32mCPF válido!\033[m")
        estaValido = True
    else:
        print("\033[31mCPF inválido!\033[m")
