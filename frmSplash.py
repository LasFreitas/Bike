# encoding: utf-8
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
import time

import sys
import os
import time
import threading
import m_Var
import m_Text
import m_Form
#import m_Image
import m_Backup
import frmMain


class Ui_Splash(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(m_Var.strScreen + 'FrmSplash.ui', self)

        self.setStyleSheet("QDialog { background-color:" + m_Var.clrColorClear + " }");
       

        # Instância label título e modifica texto
        lbTittle = self.findChild(QtWidgets.QLabel, 'lbTittle')
        lbTittle.setText(m_Var.strSystem)

        lbMessage = self.findChild(QtWidgets.QLabel, 'lbMessage')
        lbMessage.setText('')

        # Instância e carrega imagem
        # lbImage = self.findChild(QtWidgets.QLabel, 'lbImage')
        # lbImage.setText('')

        lbMessage.setText('AGUARDE... VERIFICANDO O SISTEMA')


        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        
         # Esconde Barra de Titulo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Configura o form 
        # m_Form.formConfigControl(self)

        #self.show()

        #def execBackup():
        #    m_Backup.delDB(lbMessage)


def main():
    # Atualiza arquivo de log com a data e hora da inicialização do sistema
    m_Text.write_texto("LOG", "INICIALIZAÇÃO DO SISTEMA", "TXT", True)
   

    app = QtWidgets.QApplication(sys.argv) 
    window = Ui_Splash()
    window.show()
   
     
    
    m_Backup.delDB(window.lbMessage)
   
    #frmMain.Ui_Main()
      
   
    QTimer.singleShot(5000, app.quit)
      
    
    sys.exit(app.exec_())
      
        


if __name__ == '__main__':
    main()
