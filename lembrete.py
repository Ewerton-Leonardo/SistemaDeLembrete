class Lembrete:
    def __init__(self, descricao, tag, id):
        self.__descricao = descricao
        self.__tag = tag
        self.__id = id
        self.__arquivado = False

    def getDescricao(self):
        return self.__descricao

    def getTag(self):
        return self.__tag

    def getId(self):
        return self.__id

    def getArquivado(self):
        return self.__arquivado

    def setDescricao(self, novaDescricao):
        self.__descricao = novaDescricao

class LembreteSimples(Lembrete):
    def __init__(self, descricao, tag, id):
        Lembrete.__init__(self, descricao, tag, id)

class LembreteTarefa(Lembrete):
    def __init__(self, descricao, tag, deadline, id):
        Lembrete.__init__(self, descricao, tag, id)
        self.__deadline = deadline

    def getDeadline(self):
        return self.__deadline

    def setDeadline(self, novaDeadline):
        self.__deadline = novaDeadline


