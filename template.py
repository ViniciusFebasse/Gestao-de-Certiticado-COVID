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
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 501, 361))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label.setObjectName("label")
        self.criar_registro = QtWidgets.QPushButton(self.tab)
        self.criar_registro.setGeometry(QtCore.QRect(60, 140, 101, 23))
        self.criar_registro.setObjectName("criar_registro")
        self.input_telefone = QtWidgets.QLineEdit(self.tab)
        self.input_telefone.setGeometry(QtCore.QRect(100, 90, 61, 20))
        self.input_telefone.setObjectName("input_telefone")
        self.apagar_registro = QtWidgets.QPushButton(self.tab)
        self.apagar_registro.setGeometry(QtCore.QRect(180, 140, 111, 23))
        self.apagar_registro.setObjectName("apagar_registro")
        self.input_nome = QtWidgets.QLineEdit(self.tab)
        self.input_nome.setGeometry(QtCore.QRect(100, 50, 71, 20))
        self.input_nome.setObjectName("input_nome")
        self.atualizar_registro = QtWidgets.QPushButton(self.tab)
        self.atualizar_registro.setGeometry(QtCore.QRect(330, 140, 101, 23))
        self.atualizar_registro.setObjectName("atualizar_registro")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.text_resultado = QtWidgets.QTextEdit(self.tab)
        self.text_resultado.setGeometry(QtCore.QRect(200, 240, 171, 71))
        self.text_resultado.setObjectName("text_resultado")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "UTENTES"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.criar_registro.setText(_translate("MainWindow", "Criar Registro"))
        self.apagar_registro.setText(_translate("MainWindow", "Apagar Registro"))
        self.atualizar_registro.setText(_translate("MainWindow", "Atualizar Registro"))
        self.label_2.setText(_translate("MainWindow", "Telefone:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Utentes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Vacinação"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Testes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Certificados"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Log"))
