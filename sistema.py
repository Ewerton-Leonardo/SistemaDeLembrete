import psycopg2
from lembrete import LembreteSimples, LembreteTarefa
from lembreteDAO import LembreteDAO

class Sistema:
    def __init__(self):
        conexao = psycopg2.connect(host="localhost", database="sistemadelembretes", user="postgres", password="suasenha")
        self.lembreteDAO = LembreteDAO(conexao)

    #Visualiza todos os post-its NAO arquivados
    def visualizarDashboard(self, usuario):
        pass

    def criarLembrete(self, descricao, tag):
        lembreteSimples = LembreteSimples(descricao, tag, id)
        self.lembreteDAO.inserirLembreteSimples(lembreteSimples)

    def criarLembreteTarefa(self, descricao, tag, deadline):
        lembreteTarefa = LembreteTarefa(descricao, tag, deadline, id)
        self.lembreteDAO.inserirLembreteTarefa(lembreteTarefa)

    def arquivarLembrete(self, id):


