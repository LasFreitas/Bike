# !/usr/bin/python
# -*- coding: UTF-8 -*-

# ─── IMPORTS ────────────────────────────────────────────────────────────────────
import enum
import os
import sys
import time
import traceback

from ast import Pass
from datetime import datetime
from PyQt5 import Qt, QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QApplication, QDialog, QMessageBox, QPushButton, QWidget)

# ─── IMPORTS LOCAIS ─────────────────────────────────────────────────────────────
import m_Err
import m_Form
import m_Image
import m_Text
import m_Var

# ─── VARIÁVEIS ──────────────────────────────────────────────────────────────────
intTime = 0
app = QApplication(sys.argv)      
                           

# ─── DICIONÁRIO DE MENSAGENS PADRÃO ─────────────────────────────────────────────
dictMessage = {
                # ''' SYSTEM '''
                '*ECA': 'ENTRE EM CONTATO COM O ADMINISTRADOR.',    

                # ''' PASSWORD '''
                '*DSS': 'DIGITE A SENHA DO USUÁRIO!',
                
                
                # ''' USUÁRIO '''
                '*UNC': 'USUÁRIO NÃO CADASTRADO',
                '*IDU': 'IDENTIFICANDO O USUÁRIO||AGUARDE . . .',

                
                # ''' FIELD '''
                '*CPO': 'CAMPO DE PREENCHIMENTO OBRIGATÓRIO!',
                '*JC': 'JÁ CADASTRADO(A)!',
                '*PNCD': 'PESQUISANDO NOVO CÓDIGO DISPONÍVEL:',
                '*CP': 'CARACTER(ES) PERMITIDO(S): ',
                
                
                # ''' DATABASE '''
                '*ODB': 'ABRINDO BANCO DE DADOS||AGUARDE . . .',
                '*ADB': 'ATUALIZANDO BANCO DE DADOS||AGUARDE . . .'
                
                }

# ─── BUTTON MESSAGEBOX ──────────────────────────────────────────────────────────
class Button_Message(enum.Enum):
   # Método de criação de MessageBox
   m_Yes = 0
   m_No = 1
   m_YesNo = 2
   m_Nobutton = 10
     
# ─── ICON MESSAGEBOX ────────────────────────────────────────────────────────────
class Icon_Message(enum.Enum):
   m_Critical = 0
   m_Warning = 1
   m_Information = 2
   m_Question = 3
   m_User = 4


class Ui_Message(QtWidgets.QDialog):
    
    def __init__(self):
        
        try:
            # ─── FORM ────────────────────────────────────────────────────────
            super(Ui_Message, self).__init__()
            self.ui = uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmMessage.ui', self)
            
            # Define cor de fundo do form  
            self.setStyleSheet("QDialog { background-color:" + m_Var.clrColorClear +" }");
            
            # Esconde a barra de título
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            
            # Desativa botão de help na barra de título do form
            self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)  
            
            # Desativa botão fechar na barra de título do form
            self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False) 
            
            # Configura o form      
            m_Form.Form_Config(self)   
                       
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())  
            
            
            
class Message(object):
    
    try:
       
        # ─── DEFINIÇÃO DE VARIÁVEIS ──────────────────────────────────────
        instance = None
        
        # ─── FUNÇÕES ─────────────────────────────────────────────────────
        def __new__(cls, *args, **kwargs):
            
            try:
               
                if cls.instance is None:
                    cls.instance = super().__new__(Message)
                    return cls.instance
                return cls.instance
            
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())
        
        def __init__(self): 
                                         
            try:
              
                self.boxMsg = Ui_Message()
            
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())
        
        def __exit__(self, ext_type, exc_value, traceback):
            
            try:
            
                self.close()
            
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())
        
       
        # ─── SHOW TIMER ──────────────────────────────────────────────────
        def Show_Timer(self, blnShowTimer, strMessage, objLabel, intTime):

            try:
                while intTime:
                    
                    if blnShowTimer == True:
                        
                        mins, secs = divmod(intTime, 60)
                        timer = self.Format_Message(strMessage) + ' [' '{:02d}:{:02d}'.format(mins, secs) + ']'

                        # Atualiza o título com a contagem de tempo regressivo  
                        objLabel.setText(self.Format_Message(strMessage) +  " \n\n [" + str(intTime) + "]" )
                        objLabel.update()
                        objLabel.repaint()
                        
                                        
                    time.sleep(1)
                    intTime -= 1  
                
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())  
                
        # ─── ICONE ───────────────────────────────────────────────────────
        def Select_Icon(self, objLabel, typeIcon):

            try:
                # Verifica qual o ícone a ser exibido
                if typeIcon.value == 0:
                    objLabel.setPixmap(QPixmap(m_Image.Load_Image('Critical.png'))) 
                elif typeIcon.value == 1:
                    objLabel.setPixmap(QPixmap(m_Image.Load_Image('Warming.png'))) 
                elif typeIcon.value == 2:
                    objLabel.setPixmap(QPixmap(m_Image.Load_Image('Information.png'))) 
                elif typeIcon.value == 3:
                    objLabel.setPixmap(QPixmap(m_Image.Load_Image('Question.png'))) 
                elif typeIcon.value == 4:
                    objLabel.setPixmap(QPixmap(m_Image.Load_Image('User.png'))) 
                    
                objLabel.update()
                objLabel.repaint()
                
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc()) 

        
        # ─── FORMATAR MENSAGEM ───────────────────────────────────────────
        def Format_Message(self, strMsg):

            try:
            
                # Verifica se é mensagem padrão ou mensagem definida pelo usuário
                if strMsg[0] == '*':
                    
                    # Verifica se existe a mensagem no dicionário
                    if strMsg in dictMessage:
                        # Existe no dicionário e atualiza a mensagem
                        strMsg = dictMessage[strMsg]    
                    else:
                        
                        
                        # Atualiza arquivo de erro com o erro ocorrido
                        m_Err.printErr("MENSAGEM NÃO CADASTRADA NO DICIONÁRIO" + "|" + self.Format_Message.__name__.upper() + "|" + strMsg.upper())
                                    
                        # Não existe a mensagem
                        #strMensagem = "MENSAGEM NÃO CADASTRADA NO DICIONÁRIO! \n\n ENTRE EN CONTATO COM O ADMINISTRADOR."
                        strMsg = "MENSAGEM NÃO CADASTRADA NO DICIONÁRIO!||ENTRE EM CONTATO COM O ADMINISTRADOR."
                        
                else:
                    # Atualiza mensagem com a mensagem enviada
                    strMsg = strMsg

                # Subistitui | por \n (quebra de linha)
                strMsg = strMsg.replace('|', '\n')
                
                return strMsg.upper()
        
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())
                
        # ─── MENSAGEM BOAS VINDAS ────────────────────────────────────────
        def Welcome(self):
        
            try:
                
                current_hour = int(datetime.now().strftime('%H'))
                if current_hour < 12:
                    return 'Bom Dia'
                elif 12 <= current_hour < 18:
                    return 'Boa Tarde'
                else:
                    return 'Boa Noite'
            
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())  
        
        # ─── ALTERAÇÃO TEXTO MENSAGEM ────────────────────────────────────
        def Update_Message(self, strMessage):

            try:
                
                QtWidgets.qApp.processEvents()
                
                               
                lbMessage = self.boxMsg.findChild(QtWidgets.QLabel, 'lbMensagem')
                lbMessage.setText((self.Format_Message(strMessage)))
                
                lbMessage.update()
                lbMessage.repaint() 
                                
                time.sleep(5)
               
                
               
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())  
            
         
        # ─── FECHAMENTO FORM ─────────────────────────────────────────────
        def Form_Close(self):     

            try:
                
                self.boxMsg.close()
                
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())
                
                
                
        # ─── SHOW MESSAGE BOX ────────────────────────────────────────────
        def Show_Message_Box(self, strMessage, typeIcon = Icon_Message, typeButton = Button_Message, blnTimer = False,  timeout=5, blnAutoClose = False):
            
            try:

                QtWidgets.qApp.processEvents()
                
                # Exibe form de mensagem
                self.boxMsg.show()
                             
                btYes = self.boxMsg.findChild(QtWidgets.QPushButton, 'btSim')
                btYes.setIcon(QtGui.QIcon(m_Image.Load_Image('Yes.png')))
                btYes.hide()
                
                btNo = self.boxMsg.findChild(QtWidgets.QPushButton, 'btNao')
                btNo.setIcon(QtGui.QIcon(m_Image.Load_Image('No.png')))
                btNo.hide()
                
                # Verifica qual(is) botão(ões) será(ão) exibido(s)
                
                if typeButton.value == 0:   # YES
                
                   btYes.show() 
                
                elif typeButton.value == 1: # NO
                
                    btNo.show()
                
                elif typeButton.value == 2: # YES NO
                
                    btYes.show()
                    btNo.show()
                
                elif typeButton.value == 10:    # NO BUTTON
                
                    btYes.hide()
                    btNo.hide()
                
                # Verifica qual o ícone a ser exibido
                lbIcon = self.boxMsg.findChild(QtWidgets.QLabel, 'lbIcone')
                self.Select_Icon(lbIcon, typeIcon)
                
                lbMessage = self.boxMsg.findChild(QtWidgets.QLabel, 'lbMensagem')
                lbMessage.setText((self.Format_Message(strMessage)))
                
                # Verifica se é para exibir tempo regressivo
                if blnTimer == True:
                    
                    QtWidgets.qApp.processEvents()
                    self.Show_Timer(True, strMessage, lbMessage, timeout)
                    blnTimer = False
                    
                else:
                    
                    QtWidgets.qApp.processEvents()
                    time.sleep(timeout)
                    
                # Verifica se é para fechar o form
                if blnAutoClose == True:
                         
                   self.Form_Close()

            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())              
   
    #TRY inicial           
    except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())  
                
               

