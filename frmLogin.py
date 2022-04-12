
# imports
import sys
import traceback



from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets
#from PyQt5 import QtCore, QtWidgets, uic, Qt
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog,
                             QListWidgetItem, QMainWindow, QTableWidgetItem,
                             QWidget)
 # imports locais
import m_Err
import m_Form
import m_Var
import m_Hash


class Ui_Login(QtWidgets.QDialog):
                
    def __init__(self):
        
        try:
            
            super(Ui_Login,self).__init__() 
            self.ui = uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmLogin.ui', self)
            
            
            '''---------- FORM ----------'''
            # Define cor de fundo do form  
            self.setStyleSheet("QDialog { background-color:" + m_Var.clrColorDark +" }");
           
            # Esconde a barra de título
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            
            # Desativa botão de help na barra de título do form
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  
            
            # Desativa botão fechar na barra de título do form
            self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint,False)      
                     
            
            '''---------- BUTTON ----------'''
           
            ''' ENCERRAR '''
            # Atribue controle a variável
            # butExit = self.ui.findChild(QtWidgets.QPushButton, 'pbExit')
                            
            # Atribue função fechar ao click do mouse
            # butExit.clicked.connect(self.close)
            
                     
            
            
            '''---------- LABEL -----------'''
            
            # Atribue controle a variável
            self.lbPassword = self.ui.findChild(QtWidgets.QLineEdit, 'lnUser')
            
            # Muda para caracteres password
            self.lbPassword.setEchoMode(QtWidgets.QLineEdit.Password)
            
            # Limita campo em 15 caracteres
            self.lbPassword.setMaxLength(15)
            
            # Habilita QLineEdit
            self.lbPassword.setEnabled(True)
            
            # Atribue função ao pressionar tecla ENTER/RETURN
            self.lbPassword.returnPressed.connect(self.Key_Return)
            
            
            # Configura o form      
            m_Form.Form_Config(self)   
           
           
          

        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())


    def Key_Return(self):
        
        print(m_Hash.CreateHash(self.lbPassword.text()))  
              
                  
def main():
    
    try:
           
    
        app = QtWidgets.QApplication(sys.argv) 
        window = Ui_Login()
        window.show()
        
        app.exec_()
        
        
    
    except Exception as e:
         # Atualiza arquivo de erro com o erro ocorrido
         m_Err.printErr(traceback.format_exc())


if __name__ == '__main__':
    main()  