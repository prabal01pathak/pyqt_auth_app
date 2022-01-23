from PyQt5.QtWidgets import QFileDialog,QMainWindow,QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys

class FileBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('fileBrowser.ui', self)
        self.browseButton.clicked.connect(self.openFile)


    def openFile(self):
        filename, some = QFileDialog.getOpenFileName(self, 'Open File', '.')
        self.fileName.setText(filename)
        print(filename)
        print("some: ",some)

app = QApplication([])
window = FileBrowser()
window.show()
sys.exit(app.exec_())

