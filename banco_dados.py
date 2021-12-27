import sqlite3

class BancoDados:
    def __init__(self):

        # Criação e conexão futura com o banco de dados
        self.banco = sqlite3.connect('certificado-covid.db')
        self.cursor = self.banco.cursor()

    def cria(self, nome, telefone):
        self.cursor.execute(f'''INSERT INTO pessoas (nome, telefone) VALUES('{nome}', '{telefone}')''')
        self.banco.commit()

    def consulta(self):
        self.cursor.execute("SELECT * FROM pessoas")
        print("<<<--->>>")
        for linha in self.cursor.fetchall():
            print(linha)
        print("<<<--->>>")

    def mostrar(self):
        self.cursor.execute("SELECT * FROM pessoas")
        listagem = []
        for linha in self.cursor.fetchall():
            listagem.append(linha)
        return listagem

    def apaga(self, nome):
        self.cursor.execute(f"""DELETE FROM pessoas WHERE nome = '{nome}'""")
        self.banco.commit()

    def atualiza(self, nome, telefone):
        self.cursor.execute(f"""UPDATE pessoas SET telefone = '{telefone}' WHERE nome = '{nome}'""")
        self.banco.commit()


if __name__ == '__main__':
    db = BancoDados()