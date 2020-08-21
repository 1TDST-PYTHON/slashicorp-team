estaValido = False
estados = (
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ",
    "RN",
    "RS", "RO", "RR", "SC", "SE", "SP", "TO")


def validar(estado):
    global estaValido
    if len(estado) == 2:
        if estado in estados:
            estaValido = True
        else:
            print("\033[31mEste Estado não existe!\033[m")
    else:
        print("\033[31mDigite 2 caracteres para a sigla do Estado!\033[m")
