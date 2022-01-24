from PyQt5 import QtWidgets as qtw
import sys

class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350, 150, 350, 350)
        self.init_ui()

    def init_ui(self):
        self.layout = qtw.QFormLayout()
        # email fields
        self.emailLabel = qtw.QLabel("Email: ")
        self.emailLineEdit = qtw.QLineEdit(placeholderText="Enter your email")
        self.layout.addRow(self.emailLabel, self.emailLineEdit)

        # password fields
        self.passwordLabel = qtw.QLabel("Password: ")
        self.passwordLineEdit = qtw.QLineEdit(placeholderText="Enter your password")
        self.passwordLineEdit.setEchoMode(qtw.QLineEdit.Password)
        self.passwordLineEdit.setMaxLength(50)
        self.passwordLineEdit.setStyleSheet("background-color: blue;\n"
                                            "color: white;\n"
                                            "margin: 5px;\n"
                                            "font-size: 10pt;")

        self.layout.addRow(self.passwordLabel, self.passwordLineEdit)

        # submit button
        self.submitButton = qtw.QPushButton("Submit")
        self.layout.addRow(self.submitButton)

        self.setLayout(self.layout)


app = qtw.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
