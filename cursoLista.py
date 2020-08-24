curso_permi = {
    "A01": ("PR", "RS", "SC", "MG", "RJ",
            "SP", "ES", "MT", "MS", "GO", "MA",
            "PI", "CE", "RN", "PE", "PB",
            "SE", "AL", "BA", "AM", "RR", "AP",
            "PA", "TO", "RO", "AC"),
    "A02": ("MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"),
    "A03": ("MT", "MS", "GO", "DF"),
    "A04": ("AM", "RR", "AP", "PA", "TO", "RO", "AC", "MG", "RJ", "SP", "ES", "PR", "RS", "SC"),
    "A05": ("MG", "SP", "ES")
}
cursos = {
    "A01": "AI e Machine Learing",
    "A02": "Business Inteligence",
    "A03": "Governança em TI",
    "A04": "Programação Python",
    "A05": "Programação Java"
}


def cursos_por_estado(estado: str) -> str:
    """
    Função que recebe uma a sigla de um estado, imprime na tela os cursos disponiveis naquele estado
    pede ao usuario selecionar o curso que deseja(efetua a validação desse input) e retorna uma string com o codigo do curso selecionado
    :param estado: uma string contendo a sigla do estado a ser avaliado
    :return: string contendo o codigo do curso selecionado
    """

    def select_curso(sg_estado: str) -> str:
        curso = input("Escolha um dos cursos disponíveis: ").upper()
        while True:
            if curso_permi.get(curso):
                if estado in curso_permi[curso]:
                    break
                print("\033[31mO código selecionado deve estar entre os mostrados na tabela acima.\033[m")
            else:
                print("\033[31mO valor digitado não correponde ao código de um curso\033[m")
            curso = input("Escolha um dos cursos disponíveis: ").upper()
        return curso

    estado = estado.upper()

    print(34 * '-')
    print(f" CODIGO{'CURSO'.rjust(20)}")
    print(34 * '-')

    for codigo, curso in cursos.items():
        if codigo == "A01":
            if estado in curso_permi["A01"]:
                print(f"  {codigo.ljust(12)}{curso}")
        elif codigo == "A02":
            if estado in curso_permi["A02"]:
                print(f"  {codigo.ljust(12)}{curso}")
        elif codigo == "A03":
            if estado in curso_permi["A03"]:
                print(f"  {codigo.ljust(12)}{curso}")
        elif codigo == "A04":
            if estado in curso_permi["A04"]:
                print(f"  {codigo.ljust(12)}{curso}")
        elif codigo == "A05":
            if estado in curso_permi["A05"]:
                print(f"  {codigo.ljust(12)}{curso}")
    print(34 * '-')

    return select_curso(estado)
