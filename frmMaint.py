import sys
import m_FormConfig
import m_Var

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QTableWidgetItem, QDialog, QDesktopWidget, QWidget

      
class Ui_Maint(QtWidgets.QDialog):
                
    def __init__(self):
        
        super(Ui_Maint,self).__init__() 
        self.ui = uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmMaint.ui', self)
                    
        ''' ENCERRAR '''
        # Atribue controle a variável
        butExit = self.ui.findChild(QtWidgets.QPushButton, 'pbExit')
        # Atribue função fechar ao click do mouse
        butExit.clicked.connect(self.close)
        
            
        
        
         # Centraliza o form
        self.move(m_FormConfig.centerForm(self))    
        
        self.show()
