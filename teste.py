class Aluno(object):
    def __init__(self, nome, cpf, estado, curso):
        self.__nome = nome
        self.__cpf = cpf
        self.__estado = estado
        self.__curso = curso

    def __repr__(self):
        return "nome:%s cpf:%s estado:%s curso:%s" % (self.__nome, self.__cpf, self.__estado, self.__curso)

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_estado(self):
        return self.__estado

    def get_curso(self):
        return self.__curso
