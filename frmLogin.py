
# ─── IMPORTS ────────────────────────────────────────────────────────────────────
import datetime
import sys
import traceback

from PyQt5 import Qt, QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog, QListWidgetItem, QMainWindow, QTableWidgetItem, QWidget)

# ─── IMPORTS LOCAIS ─────────────────────────────────────────────────────────────
import c_Database
import c_Message
import m_Database
import m_Err
import m_Form
import m_Hash
import m_Message
import m_Text
import m_Var



dbLogin = c_Database.Database()

_Message = c_Message.Message()



class Ui_Login(QtWidgets.QDialog):
                
    def __init__(self):
        
        try:
            
            # ─── FORM ────────────────────────────────────────────────────────
            super(Ui_Login,self).__init__() 
            self.ui = uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmLogin.ui', self)
            
            # Define cor de fundo do form  
            self.setStyleSheet("QDialog { background-color:" + m_Var.clrColorDark +" }");
           
            # Esconde a barra de título
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            
            # Desativa botão de help na barra de título do form
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)  
            
            # Desativa botão fechar na barra de título do form
            self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint,False)      
                     
            
            # ─── BUTTON ──────────────────────────────────────────────────────
            ''' ENCERRAR '''
            # Atribue controle a variável
            # butExit = self.ui.findChild(QtWidgets.QPushButton, 'pbExit')
                            
            # Atribue função fechar ao click do mouse
            # butExit.clicked.connect(self.close)
            
            # ─── LABEL ───────────────────────────────────────────────────────
            ''' PASSWORD '''
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
   
    # ─── TECLADO ────────────────────────────────────────────────────────────────────
    # ─── ENTER / RETURN ──────────────────────────────────────────────────────────────────────
    def Key_Return(self):
        
        try:

            # Verifica se foi digitado algum texto
            if self.lbPassword.text() > "":
                                
                # Verifica se BD está disponível
                if m_Var.blnDatabase == True:
                         
                    # Exibe aviso ao usuário
                    _Message.Show_Message_Box('*IDU', m_Message.Icon_Message.m_User, m_Message.Button_Message.m_Nobutton, False, 5, False)         
                    
                    # Pesquisa no BD se existe o usuário
                    tpUser = dbLogin.Search_Row('cadsysuser', 'userpassword' , m_Hash.CreateHash(self.lbPassword.text()))
                    
                    # Verifica se o usuário está cadastrado 
                    if tpUser is not None: #len(tpUser)> 0:
                               
                        # TODO VERIFICAR COMO RETORNAR 'DICIONARIO' DA PESQUISA
                        # TODO PARA MUDAR DE TPUSER[1] PARA TPUSER[USERNICKNAME]
                                                                    
                        # Atualiza variável com o nome do usuário
                        m_Var.strUser = tpUser[1].upper()
                        
                        # Atualiza variáveis para atualizar o banco de dados
                        intAccessNumber  = tpUser[2] + 1
                        datLastAccess = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        
                        # Exibe mensagem de boas vindas
                        _Message.Update_Message(m_Message.Welcome() + ', ' + tpUser[1].upper() + '|| Último acesso em: ' + tpUser[3][0:10] + ' às ' + tpUser[3][11:16] + '|| Acesso Nr.: ' + '{:n}'.format(tpUser[2],0))
                        
                        '''
                        0 - USERID
                        1 - USERNICKNAME
                        2 - USERACCESSNUMBER
                        3 - USERLASTACCESS
                        4 - USERPASSWORD
                        
                        '''                   
                       
                        # Verifica se database está online
                        if m_Var.blnDatabase == True:
                            
                            # Atualiza database com os dados do novo acesso
                            if dbLogin.Crud_Record('cadSysUser', (tpUser[0], tpUser[1], intAccessNumber, datLastAccess, tpUser[4], tpUser[4]), 'UserPassword = ?', c_Database.Type_Operation.m_Update) == True:
                                
                                # Fecha janela de login
                                self.close()
                                
                                # Exibe mensagem atualização do banco de dados
                                _Message.Update_Message('*ADB') #, m_Message.Icon_Message.m_Information, m_Message.Button_Message.m_Nobutton, False, 5, False)
                                                           
                                # Atualiza arquivo de log com a data e hora da inicialização do sistema
                                m_Text.write_texto("LOG", "LOGIN NO SISTEMA|ACESSO NR.: " '{:n}'.format(tpUser[2],0) + '|' + datLastAccess , "LOG", True)
                                
                                # Fecha form Message
                                _Message.Form_Close()

                        else:
                            
                            # NÃO PODE ATUALIZAR O BD
                            # Atualiza arquivo de log com a data e hora da inicialização do sistema
                            m_Text.write_texto("LOG", "LOGIN NO SISTEMA|ACESSO NR.: " '{:n}'.format(tpUser[2],0) + '|' + datLastAccess + '|NÃO FOI POSSÍVEL A ATUALIZAÇÃO DO BANCO DE DADOS|BLNDATABASE = ' + str(m_Var.blnDatabase) , "LOG", True)
                           
                    else:
                        
                        # NÃO EXISTE O USUÁRIO
                        _Message.Show_Message_Box('*UNC', m_Message.Icon_Message.m_Critical, m_Message.Button_Message.m_Nobutton, False, 5, True)         
           
            else:
               
               # Exibe mensagem de erro - Senha Obrigatória
               _Message.Show_Message_Box('*DSS', m_Message.Icon_Message.m_Critical, m_Message.Button_Message.m_Nobutton, True, 5, True)         
                             
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    

    # ─── ALT F10 ────────────────────────────────────────────────────────────────────
 
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
 

# ─── MAIN ───────────────────────────────────────────────────────────────────────

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
