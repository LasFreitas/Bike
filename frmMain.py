# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sys
import traceback

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog,
                             QListWidgetItem, QMainWindow, QTableWidgetItem,
                             QWidget)

# imports locais
import frmBike
import frmConfig
import frmData
import frmMaint
import frmUser
import m_Application
import m_Directory
import m_Err
import m_Form
import m_Text
import m_Var



'''---------- FORM MAIN ----------'''
class Ui_Main(QtWidgets.QDialog):
        
    def __init__(self):

        try:
            # Carrega form principal
            super(Ui_Main, self).__init__()
            uic.loadUi(m_Var.strScreen + 'frmMain.ui', self)
            
           
            '''---------- BUTTON ----------'''
            
            ''' USUÁRIO '''
            butUser = self.findChild(QtWidgets.QPushButton, 'pbUser')
            butUser.clicked.connect(frmUser.Ui_User)
          
            
            ''' BICICLETA '''
            butBike = self.findChild(QtWidgets.QPushButton, 'pbBike')
            butBike.clicked.connect(frmBike.Ui_Bike)
            
            ''' DADOS '''
            butData = self.findChild(QtWidgets.QPushButton, 'pbData')
            butData.clicked.connect(frmData.Ui_Data)
            
            ''' MANUTENÇÃO '''
            butMaint = self.findChild(QtWidgets.QPushButton, 'pbMaint')
            butMaint.clicked.connect(frmMaint.Ui_Maint)
            
            ''' CONFIGURAÇÃO '''
            butConfig = self.findChild(QtWidgets.QPushButton, 'pbConfig')
            butConfig.clicked.connect(frmConfig.Ui_Config)
        
                        
            ''' ENCERRAR '''
            # Atribue controle a variável
            butEnd = self.findChild(QtWidgets.QPushButton, 'pbEnd')
            butEnd.clicked.connect(m_Application.endApplication)
            
            # Define titulo do form principal
            self.setWindowTitle(m_Var.strSystem.upper())
                                    
            # Configura o form      
            m_Form.formConfigControl(self)   
                        
            # Exibe form
            self.show()
            
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())


def main():
    try:
        
        # Verifica se existe os diretórios necessários para funcionamento do sistema 
        # Caso NÃO exista, cria os diretórios conforme lista       
        m_Directory.checkSystemDirectory(m_Var.getVar('lstDirectory'))
                
        # Atualiza arquivo de log com a data e hora da inicialização do sistema
        m_Text.write_texto("LOG", "INICIALIZAÇÃO DO SISTEMA", "TXT", True)
        
        app = QtWidgets.QApplication(sys.argv)
        ex = Ui_Main()
        sys.exit(app.exec_())  
    
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
            
        
'''---------- EXECUÇÃO DO SISTEMA ----------'''
if __name__ == '__main__':
   main()
   
           
        

