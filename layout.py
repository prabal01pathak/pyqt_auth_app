from PyQt5.QtWidgets import ( 
                QApplication,
                QMainWindow,
                QWidget,
                QHBoxLayout,
                QVBoxLayout,
                QGridLayout,
                QFormLayout,
                QPushButton
            )
import sys

class WidgetWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("Widget Lyout")
        self.resize(120,750)
        # set layout to the widget 
        layout = QHBoxLayout()
        pushButton1 = QPushButton("Hello")
        pushButton2 = QPushButton("World!")
        pushButton3 = QPushButton("Prabal!")
        pushButton4 = QPushButton("Prabal!")

        #set widgets to the layout
        layout.addWidget(pushButton1)
        layout.addWidget(pushButton2,1)
        layout.addWidget(pushButton3,2)
        layout.addWidget(pushButton4,6)
        self.setLayout(layout)
        self.show()


app = QApplication([])
window = WidgetWindow()
sys.exit(app.exec_())

