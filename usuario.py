class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def setNome(self, novoNome):
        self.__nome = novoNome

    def setSenha(self, novaSenha):
        self.__senha = novaSenha
