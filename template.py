# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 501, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_4 = QtWidgets.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(60, 50, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_5.setObjectName("label_5")
        self.input_nome_login = QtWidgets.QLineEdit(self.tab_6)
        self.input_nome_login.setGeometry(QtCore.QRect(110, 100, 71, 20))
        self.input_nome_login.setObjectName("input_nome_login")
        self.input_nus_login = QtWidgets.QLineEdit(self.tab_6)
        self.input_nus_login.setGeometry(QtCore.QRect(110, 150, 61, 20))
        self.input_nus_login.setObjectName("input_nus_login")
        self.btn_login = QtWidgets.QPushButton(self.tab_6)
        self.btn_login.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.btn_login.setObjectName("btn_login")
        self.btn_novo_cadastro = QtWidgets.QPushButton(self.tab_6)
        self.btn_novo_cadastro.setGeometry(QtCore.QRect(190, 230, 101, 23))
        self.btn_novo_cadastro.setObjectName("btn_novo_cadastro")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 90, 47, 13))
        self.label.setObjectName("label")
        self.criar_registro = QtWidgets.QPushButton(self.tab)
        self.criar_registro.setGeometry(QtCore.QRect(10, 230, 101, 23))
        self.criar_registro.setObjectName("criar_registro")
        self.input_cadastro_telemovel = QtWidgets.QLineEdit(self.tab)
        self.input_cadastro_telemovel.setGeometry(QtCore.QRect(100, 130, 61, 20))
        self.input_cadastro_telemovel.setObjectName("input_cadastro_telemovel")
        self.apagar_registro = QtWidgets.QPushButton(self.tab)
        self.apagar_registro.setGeometry(QtCore.QRect(170, 230, 111, 23))
        self.apagar_registro.setObjectName("apagar_registro")
        self.input_cadastro_nome = QtWidgets.QLineEdit(self.tab)
        self.input_cadastro_nome.setGeometry(QtCore.QRect(100, 80, 71, 20))
        self.input_cadastro_nome.setObjectName("input_cadastro_nome")
        self.atualizar_registro = QtWidgets.QPushButton(self.tab)
        self.atualizar_registro.setGeometry(QtCore.QRect(350, 230, 101, 23))
        self.atualizar_registro.setObjectName("atualizar_registro")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_7.setObjectName("label_7")
        self.input_cadastro_nus = QtWidgets.QLineEdit(self.tab)
        self.input_cadastro_nus.setGeometry(QtCore.QRect(100, 40, 71, 20))
        self.input_cadastro_nus.setObjectName("input_cadastro_nus")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 61, 20))
        self.label_3.setObjectName("label_3")
        self.input_cadastro_morada = QtWidgets.QLineEdit(self.tab)
        self.input_cadastro_morada.setGeometry(QtCore.QRect(100, 170, 381, 20))
        self.input_cadastro_morada.setObjectName("input_cadastro_morada")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(250, 40, 111, 20))
        self.label_8.setObjectName("label_8")
        self.input_cadastro_data_nascimento = QtWidgets.QDateEdit(self.tab)
        self.input_cadastro_data_nascimento.setGeometry(QtCore.QRect(370, 40, 110, 22))
        self.input_cadastro_data_nascimento.setObjectName("input_cadastro_data_nascimento")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(250, 80, 111, 20))
        self.label_9.setObjectName("label_9")
        self.radio_data_sim = QtWidgets.QRadioButton(self.tab)
        self.radio_data_sim.setGeometry(QtCore.QRect(310, 80, 41, 17))
        self.radio_data_sim.setObjectName("radio_data_sim")
        self.radio_data_nao = QtWidgets.QRadioButton(self.tab)
        self.radio_data_nao.setGeometry(QtCore.QRect(370, 80, 41, 17))
        self.radio_data_nao.setObjectName("radio_data_nao")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(240, 90, 61, 16))
        self.label_14.setObjectName("label_14")
        self.input_vacina_dosagem = QtWidgets.QLineEdit(self.tab_2)
        self.input_vacina_dosagem.setGeometry(QtCore.QRect(320, 90, 71, 20))
        self.input_vacina_dosagem.setObjectName("input_vacina_dosagem")
        self.input_data_vacina = QtWidgets.QDateEdit(self.tab_2)
        self.input_data_vacina.setGeometry(QtCore.QRect(90, 90, 110, 22))
        self.input_data_vacina.setObjectName("input_data_vacina")
        self.atualizar_registro_vacina = QtWidgets.QPushButton(self.tab_2)
        self.atualizar_registro_vacina.setGeometry(QtCore.QRect(360, 180, 101, 23))
        self.atualizar_registro_vacina.setObjectName("atualizar_registro_vacina")
        self.criar_registro_vacina = QtWidgets.QPushButton(self.tab_2)
        self.criar_registro_vacina.setGeometry(QtCore.QRect(30, 180, 101, 23))
        self.criar_registro_vacina.setObjectName("criar_registro_vacina")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(230, 50, 81, 16))
        self.label_16.setObjectName("label_16")
        self.apagar_registro_vacina = QtWidgets.QPushButton(self.tab_2)
        self.apagar_registro_vacina.setGeometry(QtCore.QRect(180, 180, 111, 23))
        self.apagar_registro_vacina.setObjectName("apagar_registro_vacina")
        self.input_vacina_nus = QtWidgets.QLineEdit(self.tab_2)
        self.input_vacina_nus.setGeometry(QtCore.QRect(90, 50, 71, 20))
        self.input_vacina_nus.setObjectName("input_vacina_nus")
        self.input_vacina_tipo = QtWidgets.QLineEdit(self.tab_2)
        self.input_vacina_tipo.setGeometry(QtCore.QRect(330, 50, 71, 20))
        self.input_vacina_tipo.setObjectName("input_vacina_tipo")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 100, 47, 13))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(30, 130, 61, 16))
        self.label_18.setObjectName("label_18")
        self.input_vacina_toma = QtWidgets.QLineEdit(self.tab_2)
        self.input_vacina_toma.setGeometry(QtCore.QRect(90, 130, 71, 20))
        self.input_vacina_toma.setObjectName("input_vacina_toma")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_10.setObjectName("label_10")
        self.input_teste_nus = QtWidgets.QLineEdit(self.tab_3)
        self.input_teste_nus.setGeometry(QtCore.QRect(80, 60, 71, 20))
        self.input_teste_nus.setObjectName("input_teste_nus")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.label_11.setObjectName("label_11")
        self.input_data_teste = QtWidgets.QDateEdit(self.tab_3)
        self.input_data_teste.setGeometry(QtCore.QRect(80, 110, 110, 22))
        self.input_data_teste.setObjectName("input_data_teste")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(230, 110, 61, 16))
        self.label_12.setObjectName("label_12")
        self.input_teste_resultado = QtWidgets.QLineEdit(self.tab_3)
        self.input_teste_resultado.setGeometry(QtCore.QRect(310, 110, 71, 20))
        self.input_teste_resultado.setObjectName("input_teste_resultado")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(220, 60, 81, 16))
        self.label_13.setObjectName("label_13")
        self.input_teste_tipo = QtWidgets.QLineEdit(self.tab_3)
        self.input_teste_tipo.setGeometry(QtCore.QRect(320, 60, 71, 20))
        self.input_teste_tipo.setObjectName("input_teste_tipo")
        self.criar_registro_teste = QtWidgets.QPushButton(self.tab_3)
        self.criar_registro_teste.setGeometry(QtCore.QRect(20, 190, 101, 23))
        self.criar_registro_teste.setObjectName("criar_registro_teste")
        self.apagar_registro_teste = QtWidgets.QPushButton(self.tab_3)
        self.apagar_registro_teste.setGeometry(QtCore.QRect(170, 190, 111, 23))
        self.apagar_registro_teste.setObjectName("apagar_registro_teste")
        self.atualizar_registro_teste = QtWidgets.QPushButton(self.tab_3)
        self.atualizar_registro_teste.setGeometry(QtCore.QRect(350, 190, 101, 23))
        self.atualizar_registro_teste.setObjectName("atualizar_registro_teste")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(50, 30, 47, 13))
        self.label_19.setObjectName("label_19")
        self.input_certificado_nus = QtWidgets.QLineEdit(self.tab_4)
        self.input_certificado_nus.setGeometry(QtCore.QRect(150, 30, 71, 20))
        self.input_certificado_nus.setObjectName("input_certificado_nus")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(50, 140, 131, 16))
        self.label_20.setObjectName("label_20")
        self.valida_certificado = QtWidgets.QLabel(self.tab_4)
        self.valida_certificado.setGeometry(QtCore.QRect(210, 130, 141, 41))
        self.valida_certificado.setObjectName("valida_certificado")
        self.btn_valida_certificado = QtWidgets.QPushButton(self.tab_4)
        self.btn_valida_certificado.setGeometry(QtCore.QRect(280, 60, 101, 23))
        self.btn_valida_certificado.setObjectName("btn_valida_certificado")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(50, 80, 81, 16))
        self.label_21.setObjectName("label_21")
        self.input_certificado_nus_2 = QtWidgets.QLineEdit(self.tab_4)
        self.input_certificado_nus_2.setGeometry(QtCore.QRect(150, 80, 71, 20))
        self.input_certificado_nus_2.setObjectName("input_certificado_nus_2")
        self.table_ultimas_alteracoes = QtWidgets.QTableView(self.tab_4)
        self.table_ultimas_alteracoes.setGeometry(QtCore.QRect(70, 250, 351, 71))
        self.table_ultimas_alteracoes.setObjectName("table_ultimas_alteracoes")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(70, 220, 131, 16))
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableView = QtWidgets.QTableView(self.tab_5)
        self.tableView.setGeometry(QtCore.QRect(20, 60, 461, 261))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "LOGIN"))
        self.label_6.setText(_translate("MainWindow", "NUS:"))
        self.label_5.setText(_translate("MainWindow", "Nome:"))
        self.btn_login.setText(_translate("MainWindow", "Login"))
        self.btn_novo_cadastro.setText(_translate("MainWindow", "Novo Cadastro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.criar_registro.setText(_translate("MainWindow", "Criar Registro"))
        self.apagar_registro.setText(_translate("MainWindow", "Apagar Registro"))
        self.atualizar_registro.setText(_translate("MainWindow", "Atualizar Registro"))
        self.label_2.setText(_translate("MainWindow", "Telemovel:"))
        self.label_7.setText(_translate("MainWindow", "NUS:"))
        self.label_3.setText(_translate("MainWindow", "Morada:"))
        self.label_8.setText(_translate("MainWindow", "Data de Nascimento:"))
        self.label_9.setText(_translate("MainWindow", "Doença:"))
        self.radio_data_sim.setText(_translate("MainWindow", "Sim"))
        self.radio_data_nao.setText(_translate("MainWindow", "Não"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Cadastro de Utentes"))
        self.label_14.setText(_translate("MainWindow", "Dosagem:"))
        self.atualizar_registro_vacina.setText(_translate("MainWindow", "Atualizar Registro"))
        self.criar_registro_vacina.setText(_translate("MainWindow", "Criar Registro"))
        self.label_15.setText(_translate("MainWindow", "NUS:"))
        self.label_16.setText(_translate("MainWindow", "Tipo de Vacina:"))
        self.apagar_registro_vacina.setText(_translate("MainWindow", "Apagar Registro"))
        self.label_17.setText(_translate("MainWindow", "Data:"))
        self.label_18.setText(_translate("MainWindow", "Toma:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vacinação"))
        self.label_10.setText(_translate("MainWindow", "NUS:"))
        self.label_11.setText(_translate("MainWindow", "Data:"))
        self.label_12.setText(_translate("MainWindow", "Resultado:"))
        self.label_13.setText(_translate("MainWindow", "Tipo de Teste:"))
        self.criar_registro_teste.setText(_translate("MainWindow", "Criar Registro"))
        self.apagar_registro_teste.setText(_translate("MainWindow", "Apagar Registro"))
        self.atualizar_registro_teste.setText(_translate("MainWindow", "Atualizar Registro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Testes"))
        self.label_19.setText(_translate("MainWindow", "NUS:"))
        self.label_20.setText(_translate("MainWindow", "Validação do Certificado:"))
        self.valida_certificado.setText(_translate("MainWindow", "Resultado"))
        self.btn_valida_certificado.setText(_translate("MainWindow", "Validar Certificado"))
        self.label_21.setText(_translate("MainWindow", "Nº Certificado:"))
        self.label_22.setText(_translate("MainWindow", "Últimas alterações:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Certificados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Log"))
