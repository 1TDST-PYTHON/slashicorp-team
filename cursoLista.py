def cursos_por_estado(estado: str) -> None:
    """
    Função que recebe uma a sigla de um estado e imprime na tela os cursos disponiveis naquele estado
    :param estado: uma string contendo a sigla do estado a ser avaliado
    :return: None
    """
    estado = estado.upper()
    curso_permi = {
        "A02": ["MA", "PI", "CE", "RN", "PE", "PB", "SE", "AL", "BA"],
        "A03": ["MT", "MS", "GO", "DF"],
        "A04": ["AM", "RR", "AP", "PA", "TO", "RO", "AC", "MG", "RJ", "SP", "ES", "PR", "RS", "SC"],
        "A05": ["MG", "SP", "ES"]
    }
    cursos = {
        "A01": "AI e Machine Learing",
        "A02": "Business Inteligence",
        "A03": "Governança em TI",
        "A04": "Programação Python",
        "A05": "Programação Java"
    }
    
    print(34 * '-')
    print(f" CODIGO{'CURSO'.rjust(20)}")
    print(34 * '-')

    for codigo, curso in cursos.items():
        if codigo == "A01":
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
