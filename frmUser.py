
# imports
import sys
import traceback

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog,
                             QListWidgetItem, QMainWindow, QTableWidgetItem,
                             QWidget)
 # imports locais
import m_Err
import m_Form
import m_Var


class Ui_User(QtWidgets.QDialog):
                
    def __init__(self):
        
        try:
            
            super(Ui_User,self).__init__() 
            self.ui = uic.loadUi(m_Var.strScreen + 'frmUser.ui', self)
                     
            ''' ENCERRAR '''
            # Atribue controle a variável
            butExit = self.ui.findChild(QtWidgets.QPushButton, 'pbExit')
                            
            # Atribue função fechar ao click do mouse
            butExit.clicked.connect(self.close)
            
         
            # Configura o form 
            m_Form.formConfigControl(self)
             
            # Exibe o form        
            self.show()


        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
            
    