from lembrete import LembreteSimples, LembreteTarefa

class Sistema:
    def __init__(self):
        pass

    #Visualiza todos os post-its NAO arquivados
    def visualizarDashboard(self, usuario):
        pass

    def criarLembrete(self, descricao, tag):
        lembreteSimples = LembreteSimples(descricao, tag, id)
        return lembreteSimples

    def criarLembreteTarefa(self, descricao, tag, deadline):
        lembreteTarefa = LembreteTarefa(descricao, tag, deadline, id)
        return lembreteTarefa

    def arquivarLembrete(self, id):
        pass

