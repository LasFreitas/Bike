# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sys
import enum
import traceback

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog

# imports Locais
import m_Var
import m_Err



''' VARIÁVEIS '''
blnTmr = False
strMensagem = ""
strTitulo = ""


''' DICIONÁRIO DE MENSAGEM PADRÃO '''

dictMessage = {
                # ''' SYSTEM '''
    
    
                # ''' PASSWORD '''
                '*DSS': 'DIGITE A SENHA DO USUÁRIO!',
                
                
                # ''' USUÁRIO '''
                '*UNC': 'USUÁRIO NÃO CADASTRADO',

                
                # ''' FIELD '''
                '*CPO': 'CAMPO DE PREENCHIMENTO OBRIGATÓRIO!',
                '*JC': 'JÁ CADASTRADO(A)!',
                '*PNCD': 'PESQUISANDO NOVO CÓDIGO DISPONÍVEL:',
                '*CP': 'CARACTER(ES) PERMITIDO(S): '
                
                }





''' MESSAGEBOX '''
class Button_Message(enum.Enum):
   # Método de criação de MessageBox
   m_OK = 0
   m_OkCancel = 1
   m_Yes = 2
   m_YesNo = 3
   m_Open = 4
   m_Save = 5
   m_NoButton = 10
      
class Icon_Message(enum.Enum):
   m_Critical = 0
   m_Warning = 1
   m_Information = 2
   m_Question = 3


class Message_Box(QMessageBox):
    
    try:

        '''---------- PARÂMETROS ----------'''
        '''
            strTittle - Título do QMessageBox
            strMessage - Mensagem do QMessageBox
            typeIcon - Tipo de Icon
            typeButton - Tipo dos botões
            blnTimer = Boolean para apresentação de contagem regressiva
        
        '''

        try:
        
            def __init__(self, strTittle, strMessage, typeIcon = Icon_Message, typeButton = Button_Message, blnTimer = False,  timeout=5, parent=None):
            
                super(Message_Box, self).__init__(parent)
            
            
                global strTitulo
                strTitulo = strTittle
                
                # Atualiza título do QMessageBox
                self.setWindowTitle(strTittle)
                
                # Atualiza tempo de espera
                self.time_to_wait = timeout
                    
                # Verifica qual o ícone a ser exibido
                if typeIcon.value == 0:
                    self.setIcon(QMessageBox.Critical)
                elif typeIcon.value == 1:
                    self.setIcon(QMessageBox.Warning)
                elif typeIcon.value == 2:
                    self.setIcon(QMessageBox.Information)
                elif typeIcon.value == 3:
                    self.setIcon(QMessageBox.Question)
                        
                # Verifica qual(is) botão(ões) será(ão) exibido(s)
                if typeButton.value == 0:
                    self.setStandardButtons(QMessageBox.Ok)
                elif typeButton.value == 1:
                    self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
                elif typeButton.value == 2:
                    self.setStandardButtons(QMessageBox.Yes)     
                elif typeButton.value == 3:
                    self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     
                elif typeButton.value == 4:
                    self.setStandardButtons(QMessageBox.Open)  
                elif typeButton.value == 5:
                    self.setStandardButtons(QMessageBox.Save)  
                elif typeButton.value == 10:
                    self.setStandardButtons(QMessageBox.NoButton) 
            
                    self.timer = QtCore.QTimer(self)
                    self.timer.setInterval(1000)
                    self.timer.timeout.connect(self.changeContent)
                    self.timer.start()
                
            
                # Atualiza texto da mensagem a ser exibida
                global strMensagem
                
                # Verifica se é mensagem padrão ou mensagem definida pelo usuário
                if strMessage[0] == '*':
                    
                    # Verifica se existe a mensagem no dicionário
                    if strMessage in dictMessage:
                        # Existe no dicionário e atualiza a mensagem
                        strMensagem = dictMessage[strMessage]    
                    else:
                        # Não existe a mensagem
                        strMensagem = "MENSAGEM NÃO CADASTRADA NO DICIONÁRIO! \n\n ENTRE EN CONTATO COM O ADMINISTRADOR."
                else:
                    # Atualiza mensagem com a mensagem enviada
                    strMensagem = strMessage
                           
                
                
            
                # Atualiza a variável com o novo valor
                global blnTmr
                blnTmr = blnTimer
                        
                # Atualiza mensagem a ser exibida
                self.setText(strMensagem.upper())
                
        except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())  
        
            
        def changeContent(self):
            try:
                
                # Verifica se é para mostrar contagem regressiva
                if blnTmr == True:
                    
                    # Atualiza o título com a contagem de tempo regressivo               
                    self.setWindowTitle(strTitulo +  " [" + str(self.time_to_wait) + "]" )
                    
                    # Atualiza a mensagem com a contagem de tempo regressivo
                    #self.setText(strMensagem.upper() + " (" + str(self.time_to_wait) + ")")
                    
                else:
                    
                    # Atualiza a mensagem
                    self.setText(strMensagem.upper())
            
                # Diminui o tempo de exibição
                self.time_to_wait -= 1
        
                # Verifica se já encerrou o tempo
                if self.time_to_wait < 0:
                    
                    # Fecha o form
                    self.close()
            
            except Exception as e:
                    # Atualiza arquivo de erro com o erro ocorrido
                    m_Err.printErr(traceback.format_exc()) 
        
        
        def closeEvent(self, event):
            try:
        
                self.timer.stop()
                event.accept()
        
            except Exception as e:
                    # Atualiza arquivo de erro com o erro ocorrido
                    m_Err.printErr(traceback.format_exc()) 

    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc()) 
            


            
def Message_Label(objLabel, strMessage, typeIcon = Icon_Message, blnClear = False, blnTimer = False,  timeout=5 ):
    try:
        # TODO IMPLEMENTAR MESSAGE_LABEL
        pass    
    
        # Verifica qual o ícone a ser exibido
        if typeIcon.value == 0:
            objLabel.setPixmap(QPixmap(QMessageBox.Critical))
        elif typeIcon.value == 1:
            objLabel.setIcon(QMessageBox.Warning)
        elif typeIcon.value == 2:
            objLabel.setIcon(QMessageBox.Information)
        elif typeIcon.value == 3:
            objLabel.setIcon(QMessageBox.Question)
    
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc()) 
            