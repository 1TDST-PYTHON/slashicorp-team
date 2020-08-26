estadosCapitais = [("AC", "Rio Branco"), ("AL","Maceió"), ("AP","Macapá"), ("AM","Manaus"), ("BA","Salvador"), ("CE","Fortaleza"), ("DF","Brasília"), ("ES","Vitória"), ("GO","Goiânia"), ("MA","São Luís"), ("MT","Cuiabá"), ("MS","Campo Grande"), ("MG","Belo Horizonte"), ("PA","Belém"), ("PB","João Pessoa"), ("PR","Curitiba"), ("PE","Recife"), ("PI","Teresina"), ("RJ","Rio de Janeiro"), ("RN","Natal"), ("RS","Porto Alegre"), ("RO","Porto Velho"), ("RR","Boa Vista"), ("SC","Florianópolis"), ("SP","São Paulo"), ("SE","Aracaju"), ("TO","Palmas")]
estaValido = False

def validar(estado):
    global estaValido
    estado = estado.upper()
    while len(estado) != 2:
        estado = input("\033[31mDigite 2 caracteres para a sigla do Estado!\n\033[m").upper()
    for index, estadoTemp in enumerate(estadosCapitais):
        if estado == estadoTemp[0]:
            estaValido = True
            break
    else:
        estado = input("\033[31mEste Estado não existe! Digite outro estado:\n\033[m").upper()
        validar(estado)

def encontraCapital(estado):
    for index, estadoTemp in enumerate(estadosCapitais):
        if estado == estadoTemp[0]:
            return estadosCapitais[index][1]
