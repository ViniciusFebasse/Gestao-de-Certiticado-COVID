# Caminho padrão para achar o QtDesigner (procure também no venv):
## C:\Users\vinicius.serra\AppData\Local\Programs\Python\Python39\Lib\site-packages

# Instalação do aplicativo do Qt-Designer, caso não se encontre nas pastas
## https://build-system.fman.io/qt-designer-download

# Após a geração do arquivo.ui insira o mesmo na pasta do projeto
## O pyuic5 deve ser executado no PC e não no ambiente virtual
## Abra o terminal e digite "pyuic5 arquivo.ui -o arquivo.py"

import sys

from template import *
from PyQt5.QtWidgets import QMainWindow, QApplication

from banco_dados import BancoDados


class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi((self))
        self.database = BancoDados()

        # Botões
        self.criar_registro.clicked.connect(self.insere)
        self.apagar_registro.clicked.connect(self.apaga)
        self.atualizar_registro.clicked.connect(self.atualiza)

    def insere(self):
        nome = self.input_nome.text()
        telefone = self.input_telefone.text()

        self.database.cria(nome, telefone)

        self.text_resultado.setText(str(self.database.mostrar()))
        self.database.consulta()

    def apaga(self):
        nome = self.input_nome.text()

        self.database.apaga(nome)

        self.text_resultado.setText(str(self.database.mostrar()))
        self.database.consulta()

    def atualiza(self):
        nome = self.input_nome.text()
        telefone = self.input_telefone.text()

        self.database.atualiza(nome, telefone)

        self.text_resultado.setText(str(self.database.mostrar()))
        self.database.consulta()


if __name__ == "__main__":

    try:
        qt = QApplication(sys.argv)
        janela = Janela()
        janela.show()
        qt.exec()

    except Exception as e:
        print(e)
