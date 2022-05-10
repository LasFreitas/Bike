# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
from configparser import InterpolationMissingOptionError
import sys
import enum
import traceback
import time
import os

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


# imports Locais
import m_Var
import m_Err
import m_Form
import m_Image
import m_Text



''' VARIÁVEIS '''
#blnTmr = False
#strMensagem = ""
#strTitulo = ""
intTime = 0

''' DICIONÁRIO DE MENSAGEM PADRÃO '''

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
                '*DBO': 'ABRINDO BANCO DE DADOS||AGUARDE . . .'
                
                }





''' MESSAGEBOX '''
class Button_Message(enum.Enum):
   # Método de criação de MessageBox
   m_Yes = 0
   m_No = 1
   m_YesNo = 2
   m_Nobutton = 10
      
   '''
        m_OK = 0
        m_OkCancel = 1
        m_Yes = 2
        m_YesNo = 3
        m_Open = 4
        m_Save = 5
        m_NoButton = 10
   '''   
class Icon_Message(enum.Enum):
   m_Critical = 0
   m_Warning = 1
   m_Information = 2
   m_Question = 3
   
   
class Notice_Form(enum.Enum):
    m_Load = 0
    m_Refresh = 1
    m_Close = 2



class Ui_Message(QtWidgets.QDialog):
    
    def __init__(self):
        
        try:
            
            super(Ui_Message, self).__init__()
            self.ui = uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmMessage.ui', self)
            
            
            '''---------- FORM ----------'''
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
       
  
class Ui_Notice(QtWidgets.QDialog):
    
    def __init__(self):
        
        try:
            
            super(Ui_Notice, self).__init__()
            self.ui = uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmNotice.ui', self)
            
            
            '''---------- FORM ----------'''
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
      
  
''' ---------- FUNÇÕES ---------- '''

def Show_Timer(blnShowTimer, strMessage, objLabel, intTime):
    try:
        while intTime:
            
            if blnShowTimer == True:
                
                mins, secs = divmod(intTime, 60)
                timer = Format_Message(strMessage) + ' [' '{:02d}:{:02d}'.format(mins, secs) + ']'

                # Atualiza o título com a contagem de tempo regressivo  
                objLabel.setText(Format_Message(strMessage) +  " \n\n [" + str(intTime) + "]" )
                objLabel.update()
                objLabel.repaint()
           
            time.sleep(1)
            intTime -= 1  
        
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())  

''' MESSAGE BOX '''   
def Show_Message_Box(strTittle, strMessage, typeIcon = Icon_Message, typeButton = Button_Message, blnTimer = False,  timeout=5, parent=None):
    
    try:
        
        '''---------- PARÂMETROS ----------'''
        '''
            strTittle - Título do QMessageBox
            strMessage - Mensagem do QMessageBox
            typeIcon - Tipo de Icon
            typeButton - Tipo dos botões
            blnTimer = Boolean para apresentação de contagem regressiva
        
        '''
               
        blnTimer = False

        # Exibe form de mensagem
        boxMsg = Ui_Message()
        boxMsg.show()
                   
        # Define o Título 
        lbTittle = boxMsg.findChild(QtWidgets.QLabel, 'lbTitulo')
        lbTittle.setText(strTittle.upper())
        
        btYes = boxMsg.findChild(QtWidgets.QPushButton, 'btSim')
        btYes.setIcon(QtGui.QIcon(m_Image.Load_Image('Yes.png')))
        #btYes.clicked.connect(m_Application.System_End)
        btYes.hide()
        
        btNo = boxMsg.findChild(QtWidgets.QPushButton, 'btNao')
        btNo.setIcon(QtGui.QIcon(m_Image.Load_Image('No.png')))
        #btNo.clicked.connect(m_Application.System_End)
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
            blnTimer = True   
           
        
        # Define icon
        lbIcon = boxMsg.findChild(QtWidgets.QLabel, 'lbIcone')
                
        # Verifica qual o ícone a ser exibido
        if typeIcon.value == 0:
             lbIcon.setPixmap(QPixmap(m_Image.Load_Image('Critical.png'))) 
        elif typeIcon.value == 1:
             lbIcon.setPixmap(QPixmap(m_Image.Load_Image('Warming.png'))) 
        elif typeIcon.value == 2:
             lbIcon.setPixmap(QPixmap(m_Image.Load_Image('Information.png'))) 
        elif typeIcon.value == 3:
             lbIcon.setPixmap(QPixmap(m_Image.Load_Image('Question.png'))) 
                    
       
        lbMessage = boxMsg.findChild(QtWidgets.QLabel, 'lbMensagem')
        lbMessage.setText((Format_Message(strMessage)))
        
        
        
    
        '''---------- FORM ----------'''
        
        if blnTimer == True:
            
            QtWidgets.qApp.processEvents()
            Show_Timer(True, strMessage, lbMessage, timeout)
            #Show_Timer(timeout)    
            blnTimer = False
            
            boxMsg.close()
                                

                
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())  


''' AVISO '''
def Show_Notice_Box(strMessage = "AGUARDE . . .",  blnShowTimer = False , timeout = 3):
    try:
        
        strMensagem = ""
        
        # Exibe form de mensagem
        boxNotice = Ui_Notice()
    
    
        lbIcon = boxNotice.findChild(QtWidgets.QLabel, 'lbIcone')
        lbIcon.setPixmap(QPixmap(m_Image.Load_Image('information.png'))) 
        
        lbMessage = boxNotice.findChild(QtWidgets.QLabel, 'lbMensagem')
        lbMessage.setText(Format_Message(strMessage))
        
        boxNotice.show()
        
         
        
        QtWidgets.qApp.processEvents()
             
        Show_Timer(False, strMessage, lbMessage, timeout)
        
        boxNotice.close()
                  
        
        
        
                
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())  



def Format_Message(strMsg):
    try:
        
        # Verifica se é mensagem padrão ou mensagem definida pelo usuário
        if strMsg[0] == '*':
            
            # Verifica se existe a mensagem no dicionário
            if strMsg in dictMessage:
                # Existe no dicionário e atualiza a mensagem
                strMsg = dictMessage[strMsg]    
            else:
                
                
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr("MENSAGEM NÃO CADASTRADA NO DICIONÁRIO" + "|" + Format_Message.__name__.upper() + "|" + strMsg.upper())
                              
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
