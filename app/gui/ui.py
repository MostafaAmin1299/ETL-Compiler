from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SQLCompiler(object):
    def setupUi(self, SQLCompiler):
        SQLCompiler.setObjectName("SQLCompiler")
        SQLCompiler.resize(800, 609)
        SQLCompiler.setMinimumSize(QtCore.QSize(800, 609))
        SQLCompiler.setMaximumSize(QtCore.QSize(800, 609))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ICON.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SQLCompiler.setWindowIcon(icon)
        SQLCompiler.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(SQLCompiler)
        self.centralwidget.setObjectName("centralwidget")
        self.inputbox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(40, 50, 721, 81))
        self.inputbox.setStyleSheet(
                "width: 100%;\n"
                "color: black;\n"
                "padding: 14px 14px ;\n"
                "margin: 8px 0;\n"
                "border: 2px solid;\n"
                "border-radius: 4px;\n"
                "border-color: rgb(76, 175, 80);\n"
                "font: 11pt Tahoma, Verdana, sans-serif;\n"
        )
        self.inputbox.setText("")
        self.inputbox.setObjectName("inputbox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 91, 31))
        self.label.setStyleSheet("font: 12pt Tahoma, Verdana, sans-serif;")
        self.label.setObjectName("label")
        self.outputbox = QtWidgets.QTextEdit(self.centralwidget)
        self.outputbox.setGeometry(QtCore.QRect(40, 170, 721, 151))
        self.outputbox.setStyleSheet(
                "color: black;\n"
                "padding: 14px 14px ;\n"
                "margin: 8px 0;\n"
                "border: 2px solid;\n"
                "border-radius: 4px;\n"
                "border-color: rgb(76, 175, 80);\n"
                "font: 11pt Tahoma, Verdana, sans-serif;\n"
        )
        self.outputbox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.outputbox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.outputbox.setReadOnly(True)
        self.outputbox.setObjectName("outputbox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 91, 31))
        self.label_2.setStyleSheet("font: 12pt Tahoma, Verdana, sans-serif;")
        self.label_2.setObjectName("label_2")
        self.combilebtn = QtWidgets.QPushButton(self.centralwidget)
        self.combilebtn.setGeometry(QtCore.QRect(40, 320, 341, 61))
        self.combilebtn.setStyleSheet(
                "width: 100%;\n"
                "background-color: #4CAF50;\n"
                "color: white;\n"
                "padding: 14px 20px;\n"
                "margin: 8px 0;\n"
                "border: none;\n"
                "border-radius: 4px;\n"
                "font: 12pt Tahoma, Verdana, sans-serif;"
        )
        self.combilebtn.setCursor(QtGui.QCursor())
        self.combilebtn.setObjectName("combilebtn")
        self.excutebtn = QtWidgets.QPushButton(self.centralwidget)
        self.excutebtn.setGeometry(QtCore.QRect(420, 320, 341, 61))
        self.excutebtn.setStyleSheet(
                "width: 100%;\n"
                "background-color: #4CAF50;\n"
                "color: white;\n"
                "padding: 14px 20px;\n"
                "margin: 8px 0;\n"
                "border: none;\n"
                "border-radius: 4px;\n"
                "font: 12pt Tahoma, Verdana, sans-serif;"
        )
        self.excutebtn.setObjectName("excutebtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 390, 91, 31))
        self.label_3.setStyleSheet("font: 12pt Tahoma, Verdana, sans-serif;")
        self.label_3.setObjectName("label_3")
        self.results = QtWidgets.QTextEdit(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(40, 420, 721, 181))
        self.results.setStyleSheet(
                "color: black;\n"
                "padding: 14px 14px ;\n"
                "margin: 8px 0;\n"
                "border: 2px solid;\n"
                "border-radius: 4px;\n"
                "border-color: rgb(76, 175, 80);\n"
                "font: 11pt Tahoma, Verdana, sans-serif;"
        )
        self.results.setObjectName("results")
        SQLCompiler.setCentralWidget(self.centralwidget)

        self.retranslateUi(SQLCompiler)
        QtCore.QMetaObject.connectSlotsByName(SQLCompiler)

    def retranslateUi(self, SQLCompiler):
        _translate = QtCore.QCoreApplication.translate
        SQLCompiler.setWindowTitle(_translate("SQLCompiler", "SQL Compiler"))
        self.label.setText(_translate("SQLCompiler", "INPUT"))
        self.label_2.setText(_translate("SQLCompiler", "OUTPUT"))
        self.combilebtn.setText(_translate("SQLCompiler", "COMPILE"))
        self.excutebtn.setText(_translate("SQLCompiler", "EXECUTE"))
        self.label_3.setText(_translate("SQLCompiler", "RESULTS"))

import app.gui.resource_rc

