import psycopg2
import psycopg2.extras
from lembrete import LembreteSimples, LembreteTarefa

class LembreteDAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def inserirLembreteSimples(self, lembrete: LembreteSimples):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Lembrete(descricao, tag) VALUES(%s, %s)", (lembrete.getDescricao(), lembrete.getTag(), lembrete.getId()))
        cursor.commit()
        cursor.close()

    def inserirLembreteTarefa(self, lembrete: LembreteTarefa):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO Lembrete(descricao, tag, deadline) VALUES(%s, %s)", (lembrete.getDescricao(), lembrete.getTag(), lembrete.getDeadline(), lembrete.getId()))
        cursor.commit()
        cursor.close()

    def listarLembretes(self):
        cursor = self.conexao.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM Lembrete")
        lembretes = [[],[]] #lembretes[0] são os Simples e lembretes[1] os Tarefa
        for tupla in cursor.fetchall():
            if tupla['deadline'] == None:
                lembretes[0].append(["Tag:" + str(tupla['tag']),  'Descrição: ' + str(tupla['descricao']), 'ID: ' + str(tupla['id'])])
            else:
                lembretes[1].append(["Tag:" + str(tupla['tag']),  'Descrição: ' + str(tupla['descricao']), "Deadline: " + str(tupla['deadline']), 'ID: ' + str(tupla['id'])])
        cursor.close()
        return lembretes
