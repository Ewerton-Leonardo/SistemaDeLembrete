from usuario import Usuario
from lembrete import Lembrete, LembreteTarefa

class Sistema:
    def __init__(self):
        pass

    def visualizarDashboard(self, usuario):
        pass

    def criarLembrete(self, descricao, tag, emailUser):
        lembrete = Lembrete(descricao, tag, emailUser, id)
        return lembrete

    def criarLembreteTarefa(self, descricao, tag, emailUser, deadline):
        lembreteTarefa = LembreteTarefa(descricao, tag, emailUser, deadline)
        return lembreteTarefa

    def arquivarLembrete(self, id):
