from PyQt5 import QtWidgets as qtw
import sys

class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.create_layout()
    def init_ui(self):
        self.setWindowTitle("Nested Layouts")
        self.setGeometry(300, 300, 300, 300)

    def create_layout(self):
        self.layout = qtw.QVBoxLayout()
        self.layout.addWidget(qtw.QLabel("Top"))
        self.formLayout = qtw.QFormLayout()


        # add email and password field to form layout
        self.emailLabel = qtw.QLabel("Email")
        self.emailForm = qtw.QLineEdit(placeholderText="Enter Email")

        self.passwordLabel = qtw.QLabel("Password")
        self.passwordForm = qtw.QLineEdit(placeholderText="Enter Password")

        self.formLayout.addRow(self.emailLabel,self.emailForm)
        self.formLayout.addRow(self.passwordLabel,self.passwordForm)


        # checkboxes with virticle box layout

        self.virticleLayout = qtw.QVBoxLayout()

        # create checkboxes 

        self.firstCheckBox = qtw.QCheckBox("first option")
        self.secondCheckBox = qtw.QCheckBox("second option")

        self.virticleLayout.addWidget(self.firstCheckBox)
        self.virticleLayout.addWidget(self.secondCheckBox)


        self.layout.addLayout(self.formLayout)


        self.layout.addLayout(self.virticleLayout)
        self.virticleLayout.addWidget(qtw.QLabel("Bottom"))

        self.layout.addWidget(qtw.QLabel("Bottom"))
        self.setLayout(self.layout)

app = qtw.QApplication(sys.argv)
window  = Window()
window.show()
sys.exit(app.exec_())
