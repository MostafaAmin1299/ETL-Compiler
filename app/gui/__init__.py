from PyQt5 import QtWidgets
from app.gui.ui import Ui_SQLCompiler
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_SQLCompiler()
ui.setupUi(MainWindow)

# Connections
from app.gui.controllers import compile, execute, change_tool
ui.combilebtn.clicked.connect(compile)
ui.excutebtn.clicked.connect(execute)
ui.listButton.currentIndexChanged.connect(change_tool)

