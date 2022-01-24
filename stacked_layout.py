from PyQt5 import QtWidgets as qtw
import sys

class StackedWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stacked Layout')
        self.setGeometry(300, 300, 300, 200)
        self.layout = qtw.QVBoxLayout()
        self.setLayout(self.layout)

        self.pageCombo = qtw.QComboBox()
        self.pageCombo.addItems(['Page 1', 'Page 2'])
        self.pageCombo.activated.connect(self.switchPage)

        self.stackedLayout = qtw.QStackedLayout()

        self.page1 = qtw.QWidget()
        self.pag1Layout = qtw.QFormLayout()
        self.pag1Layout.addRow("Name:", qtw.QLineEdit())
        self.pag1Layout.addRow("Address:", qtw.QLineEdit())
        self.page1.setLayout(self.pag1Layout)

        self.stackedLayout.addWidget(self.page1)

        self.page2 = qtw.QWidget()
        self.page2Layout = qtw.QFormLayout()
        self.page2Layout.addRow("Job:", qtw.QLineEdit())
        self.page2Layout.addRow("Deparatment:", qtw.QLineEdit())
        self.page2.setLayout(self.page2Layout)

        self.stackedLayout.addWidget(self.page2)

        self.layout.addWidget(self.pageCombo)
        self.layout.addLayout(self.stackedLayout)

    def switchPage(self):
        print("Current Index: ",self.pageCombo.currentIndex())
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

app = qtw.QApplication(sys.argv)
window = StackedWindow()
window.show()
sys.exit(app.exec_())
