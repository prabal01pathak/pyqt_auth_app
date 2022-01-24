from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
import sys
import os

class ShowAllWindow(qtw.QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textEditor = Notepad()
        self.textEditor.show()


class Notepad(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.text = qtw.QTextEdit(self)
        self.text.setGeometry(0, 0, 800, 600)
        self.text.setFontPointSize(12)
        self.text.setFontFamily("Consolas")
        self.text.setStyleSheet("background-color: #f0f0f0")
        self.text.setStyleSheet("color: #000000")
        self.text.setStyleSheet("selection-color: #ffffff")
        self.text.setStyleSheet("selection-background-color: #000000")
        self.text.setStyleSheet("border: 1px solid #000000")
        self.text.setStyleSheet("border-radius: 5px")
        self.text.setStyleSheet("padding: 5px")
        self.text.setStyleSheet("margin: 5px")
        self.text.setStyleSheet("font-size: 12px")
        self.text.setStyleSheet("font-family: Consolas")
        self.text.setStyleSheet("font-weight: normal")
        self.text.setStyleSheet("font-style: normal")
        self.text.setStyleSheet("text-decoration: none")
        self.text.setStyleSheet("text-align: left")
        self.text.setStyleSheet("line-height: 1.5")
        self.text.setStyleSheet("letter-spacing: 0px")
        self.text.setStyleSheet("word-spacing: 0px")
        self.text.setStyleSheet("text-indent: 0px")
        self.text.setStyleSheet("text-transform: none")

        self.addToolBar(qtw.QToolBar(self))
        self.toolbar = self.addToolBar("File")
        self.toolbar.setIconSize(qtc.QSize(16, 16))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.setMovable(False)
        self.toolbar.setFloatable(False)
        self.toolbar.setAllowedAreas(Qt.TopToolBarArea)
        self.toolbar.setStyleSheet("background-color: #f0f0f0")
        self.setCentralWidget(self.text)




if __name__ == "__main__":
    app = ShowAllWindow(sys.argv)
    sys.exit(app.exec_())
