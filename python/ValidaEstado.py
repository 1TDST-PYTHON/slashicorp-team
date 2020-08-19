estados = ("AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS",
            "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SE", "SP", "TO")

def validar_estado(estado):
    if len(estado) == 2:
        if estado in estados:
            return True
        else:
            print("Este Estado não existe!")
    else:
        print("Digite 2 caracteres para a sigla do Estado!")

