class Lembrete:
    def __init__(self, descricao, tag, emailUser, id):
        self.__descricao = descricao
        self.__tag = tag
        self.__emailUser = emailUser
        self.__id = id

    def getDescricao(self):
        return self.__descricao

    def getTag(self):
        return self.__tag

    def getEmailUser(self):
        return self.__emailUser

    def setDescricao(self, novaDescricao):
        self.__descricao = novaDescricao

class LembreteTarefa(Lembrete):
    def __init__(self, descricao, tag, emailUser, deadline):
        Lembrete.__init__(self, descricao, tag, emailUser, id)
        self.__deadline = deadline

    def getDeadline(self):
        return self.__deadline

    def setDeadline(self, novaDeadline):
        self.__deadline = novaDeadline


