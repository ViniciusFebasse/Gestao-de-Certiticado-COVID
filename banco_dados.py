import sqlite3
import random

class BancoDados:
    def __init__(self):

        # Criação e conexão futura com o banco de dados
        self.banco = sqlite3.connect('certificado-covid.db')
        self.cursor = self.banco.cursor()

    def cria(self, nome, telefone):
        self.cursor.execute(f'''INSERT INTO utentes (NOME, TELEMOVEL, NUS) VALUES('{nome}', '{telefone}', {random.randint(0, 999999)})''')
        self.banco.commit()

    def consulta(self):
        self.cursor.execute("SELECT * FROM utentes")
        print("<<<--->>>")
        for linha in self.cursor.fetchall():
            print(linha)
        print("<<<--->>>")

    def mostrar(self):
        self.cursor.execute("SELECT * FROM utentes")
        listagem = []
        for linha in self.cursor.fetchall():
            listagem.append(linha)
        return listagem

    def apaga(self, nome):
        self.cursor.execute(f"""DELETE FROM utentes WHERE NUS = '{nome}'""")
        self.banco.commit()

    def atualiza(self, nome, telefone):
        self.cursor.execute(f"""UPDATE utentes SET TELEMOVEL = '{telefone}' WHERE NOME = '{nome}'""")
        self.banco.commit()


if __name__ == '__main__':
    db = BancoDados()