import sys
import platform
import paramiko
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient, QWindow)
from PySide2.QtWidgets import *

from CPUStress_Window import Ui_MainWindow

from cryptography.fernet import Fernet
from datetime import date

class MainScreen(QMainWindow):
    def __init__(self):
        
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ConnectBtn.clicked.connect(self.connect_server)

        self.ui.ExecuteBtn.clicked.connect(self.execute_stress)
        self.expiry_verification()
        

    def connect_server(self):
        server_user = self.ui.UserInp.text()
        server_name = self.ui.ServerInp.text()
        server_pwd = self.ui.PwdInp.text()

        self.conn = paramiko.SSHClient()
        self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.conn.connect(hostname=server_name, port=22, username=server_user, password=server_pwd)
        except Exception as e:
            self.ui.ConnStatusTxt.setText('Connection Refused')
            print(e)
            
        self.ui.ConnStatusTxt.setStyleSheet('color : green')
        self.ui.ConnStatusTxt.setText('Connected')

        stdin, stdout, stderr = self.conn.exec_command('hostname -i')

        #print(''.join(stdin.readlines()))
        print('connected to ', ''.join(stdout.readlines()))
        print(''.join(stderr.readlines()))
    
    def execute_stress(self):
        self.ui.ExecStatusTxt.setStyleSheet('color : blue')
        self.ui.ExecStatusTxt.setText('Executing...')
        self.ui.ExecStatusTxt.repaint()
        self.selected_CPUper = self.ui.CPUper_RBGrp.checkedButton().text()
        self.CPU_cores = None
        if(self.selected_CPUper == "100%"):
            self.CPU_cores = 4
        elif(self.selected_CPUper == "75%"):
            self.CPU_cores = 3
        elif(self.selected_CPUper == "50%"):
            self.CPU_cores = 2
        elif(self.selected_CPUper == "25%"):
            self.CPU_cores = 1
        
        self.CPU_duration = self.ui.DurationInp.text()
        
        stdin, stdout, stderr = self.conn.exec_command('seq {cores} | xargs -P0 -n1 timeout {duration} md5sum /dev/zero'.format(cores = self.CPU_cores, duration = self.CPU_duration))
        
        #print('---',''.join(stderr.readlines()),'---')

        #print(len(''.join(stderr.readlines())))

        if(len(''.join(stderr.readlines())) > 0):
            self.ui.ExecStatusTxt.setStyleSheet('color : red')
            self.ui.ExecStatusTxt.setText('Not Executed')
        else:
            self.ui.ExecStatusTxt.setStyleSheet('color : green')
            self.ui.ExecStatusTxt.setText('Executed')

    def expiry_verification(self):
        self.app_key = b'z4WgegchrnsyRaKJXWg4sN9iaqEvaVjWjfZSI2gH5jE='
        self.crypto_fer = Fernet(self.app_key)

        with open('Licence.key', 'rb') as f:
            self.enc_code = f.read()
        
        #print(self.enc_code)
        self.dec_code = str(self.crypto_fer.decrypt(self.enc_code))
        #print(self.dec_code)
        self.dec_code = self.dec_code[2:-1].split('-')
        #print(self.dec_code)
        self.exp_date = date(year=int(self.dec_code[0]), month=int(self.dec_code[1]), day=int(self.dec_code[2]))
        self.curr_date = date.today()

        if(self.curr_date > self.exp_date):
            self.exp_msg = QMessageBox()
            self.exp_msg.setIcon(QMessageBox.Critical)
            self.exp_msg.setText('Your Licence has been Expired')
            self.exp_msg.setWindowTitle('Application Expiration')
            self.exp_msg.setStandardButtons(QMessageBox.Ok)
            self.exp_msg.buttonClicked.connect(lambda: sys.exit())
            self.exp_msg.show()
            print('Exiting....')
        else:
            self.show()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainScreen()
    sys.exit(app.exec_())