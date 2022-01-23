import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QStackedWidget, QLineEdit
import sqlite3


class WelcomeDialog(QDialog):
    def __init__(self, parent=None):
        super(WelcomeDialog, self).__init__(parent)
        loadUi('welcome.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.getLoginScreen)
        self.createAccountButton.clicked.connect(self.getSignUpScreen)

    def getLoginScreen(self):
        login = LoginDialog()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("getlogin clicked")

    def getSignUpScreen(self):
        signup = SignUpDialog()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("getsignup clicked")


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        loadUi('login.ui', self)
        self.passwordField.setEchoMode(QLineEdit.Password)
        self.loginButton.clicked.connect(self.loginFunction)
        self.backButton.clicked.connect(self.backFunction)
        print(dir(self.error))

    def backFunction(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        print("back clicked")

    def loginFunction(self):
        self.email = self.emailField.text()
        self.password = self.passwordField.text()
        
        if len(self.email) == 0 or len(self.password) == 0:
            self.error.setText("Please enter your email and password")
            print("invalid length")
        else: 
            database = sqlite3.connect('database.db')
            cursor = database.cursor()
            cursor.execute("SELECT * FROM users WHERE name = ? AND password = ?", (self.email, self.password))
            if cursor.fetchone() is None:
                self.error.setText("Invalid email or password")
                print("invalid email or password")
            else:
                self.error.setText("Login Successful")
                print("login successful")


class SignUpDialog(QDialog):
    def __init__(self, parent=None):
        super(SignUpDialog, self).__init__(parent)
        loadUi("signup.ui",self)
        self.passwordField.setEchoMode(QLineEdit.Password)
        self.signUpButton.clicked.connect(self.signUpFunction)
        self.backButton.clicked.connect(self.backFunction)
    def backFunction(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        print("back clicked")

    def signUpFunction(self):
        self.email = self.emailField.text()
        self.password = self.passwordField.text()

        if len(self.email)==0 or len(self.password) ==0:
            self.error.setText("Please enter your email and password")
            print("invalid length")
        else: 
            database = sqlite3.connect('database.db')
            cursor = database.cursor()
            cursor.execute("INSERT INTO users (name,password) VALUES (?,?)", (self.email, self.password))
            database.commit()
            self.error.setText("Sign Up Successful")
            database.close()
            print("sign up successful")



app = QApplication([])
window = WelcomeDialog()
widget = QStackedWidget()
widget.addWidget(window)
widget.setFixedWidth(1000)
widget.setFixedHeight(800)
widget.show()
try: 
    sys.exit(app.exec_())

except Exception as e:
    print("Exception: ",e)
