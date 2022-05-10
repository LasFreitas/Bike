
# imports
import sys
import traceback



from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets
#from PyQt5 import QtCore, QtWidgets, uic, Qt
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog,
                             QListWidgetItem, QMainWindow, QTableWidgetItem,
                             QWidget)
#from numpy import c_
 # imports locais
import m_Err
import m_Form
import m_Var
import m_Hash
import m_Message
import m_Database


connLogin = None

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
            
            # Atribue função ao pressionar conjunto teclas ALT + F10
            shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.AltModifier + QtCore.Qt.Key_F10), self.lbPassword, context= QtCore.Qt.WidgetWithChildrenShortcut, activated=self.Key_Press_Alt_F10)
            
            
            
            # Configura o form      
            m_Form.Form_Config(self)   
           
           

          

        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())


    '''---------- FUNÇÕES TECLADO ----------'''

    '''---------- ENTER ----------'''
    def Key_Return(self):
        
        try:
            
            # Verifica se foi digitado algum texto
            if self.lbPassword.text() > "":
                                
                # Verifica se BD está disponível
                if m_Var.blnDatabase == True:
                    
                                     
                    # Exibe aviso ao usuário
                    m_Message.Show_Notice_Box('*IDU', False)
                    
                    
                    # Conecta a Database e verifica se usuário está cadastrado
                    ConnLogin = m_Database.Get_Database("CADSYSUSER", "USERPASSWORD", "USERPASSWORD")
            
                    m_Message.Show_Notice_Box(self.lbPassword.text(), False)
                
                
                print(m_Hash.CreateHash(self.lbPassword.text()))  
                
           
            else:
               
               m_Message.Show_Message_Box(m_Var.strSystem, '*DSS', m_Message.Icon_Message.m_Critical, m_Message.Button_Message.m_Nobutton, True, 5)
               
               
                
                             
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
    
    
    '''---------- ENTER ----------'''
    def Key_Press_Alt_F10(self):
        try:
                          
            self.lbPassword.setText(bytes.fromhex('7331543133524653316c').decode('utf-8'))
            self.lbPassword.update()
            self.lbPassword.repaint()
            
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
           
    def Keypress_Login(self, setkey):
        try:
            if setkey ==  QtCore.Qt.Key_Return:
                print ('enter')
                
        
            
            
            
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())    
                  
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