# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import os
import sys
import time
import traceback
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets
#from PyQt5 import QtCore, QtWidgets, uic, Qt
from PyQt5.QtWidgets import (QApplication, QDesktopWidget, QDialog,
                             QListWidgetItem, QMainWindow, QTableWidgetItem,
                             QWidget)
from datetime import datetime
#from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui
#from PyQt5.QtGui import QIcon, QPixmap
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 



# imports locais
import frmBike
import frmConfig
import frmData
import frmLogin
import frmMaint
import frmUser
import m_Application
import m_Directory
import m_Err
import m_Form
import m_Image
import m_Text
import m_Var


'''---------- FORM MAIN ----------'''
class Ui_Main(QtWidgets.QDialog):
        
    def __init__(self):

        try:
            
            '''---------- FORM ----------'''
            
            # Carrega form principal
            super(Ui_Main, self).__init__()
            uic.loadUi(m_Var.strDirSystem + '\\Screen\\frmMain.ui', self)
                        
             # Esconde a barra de título
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
           
           
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
            butEnd.clicked.connect(m_Application.System_End)
                        
            
            '''---------- LABEL ----------'''
            
            # Instância label título e modifica texto
            lbTittle = self.findChild(QtWidgets.QLabel, 'lbTittle')
            lbTittle.setText(m_Var.strSystem)
                       
            # Hora Atual
            self.lbHourMinute = self.findChild(QtWidgets.QLabel, 'lbTime')
            
            # Data Atual
            self.lbDateNow = self.findChild(QtWidgets.QLabel, 'lbDate')
            
            # Imagem Brasil
            lbSystemBrasil = self.findChild(QtWidgets.QLabel, 'lbBrasil')
            lbSystemBrasil.setPixmap(QPixmap(m_Image.Load_Image('Brasil.png')))           
                       
            # Imagem Minimize
            lbSystemMinimize = self.findChild(QtWidgets.QLabel, 'lbMinimize')
            lbSystemMinimize.setPixmap(QPixmap(m_Image.Load_Image('Minimize.png')))
            
            # TODO Criar rotina para minimizar o form
            #lbSystemMinimize.mousePressEvent = print("sdafasdaf") #m_Application.Form_Minimized(self)
            #self.setWindowFlags(QtCore.Qt.WindowMinimized)
            
             # Imagem CLOSE
            lbSystemClose = self.findChild(QtWidgets.QLabel, 'lbClose')
            lbSystemClose.setPixmap(QPixmap(m_Image.Load_Image('Close.png')))
            # TODO Verificar rotina para fechar form
            lbSystemClose.mousePressEvent = m_Application.System_End
            
            
            # Define titulo do form principal
            #self.setWindowTitle(m_Var.strSystem.upper())
           
                                             
            # Configura o form      
            m_Form.Form_Config(self)   
                      
           
            
            def System_Information():

                # Exibe HORA
                self.lbHourMinute.setText(datetime.now().strftime("%H:%M")) #:%S" ) 
                self.lbHourMinute.update()
                self.lbHourMinute.repaint()
                # EXibe DATA
                self.lbDateNow.setText(datetime.now().strftime("%d/%m/%Y"))
                self.lbDateNow.update()
                self.lbDateNow.repaint()
                
                # Imagem DATABASE
                if os.path.exists(m_Var.strDirSystem + "\\Database\\" + m_Var.strDatabaseFileName):
                    strDatabaseImage = ["DBOn.png" , "Database Online"]
                else:
                    strDatabaseImage = ["DBOff.png" , "Database Offline"]
                    
                lbSystemDatabase = self.findChild(QtWidgets.QLabel, 'lbDatabase')
                lbSystemDatabase.setPixmap(QPixmap(m_Image.Load_Image(strDatabaseImage[0])))
                lbSystemDatabase.setToolTip(strDatabaseImage[1])
            
            # Exibe hora:minuto no label
            timer = QTimer(self)
            timer.timeout.connect(System_Information)
            timer.start()
            
            
            
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())


def main():
    try:
        
        # Verifica se existe os diretórios necessários para funcionamento do sistema 
        # Caso NÃO exista, cria os diretórios conforme lista       
        m_Directory.checkSystemDirectory(m_Var.getVar('lstDirectory'))
        
        app = QtWidgets.QApplication(sys.argv)
        window = Ui_Main()
        window.show()
                
        QTimer.singleShot(500,frmLogin.main())
        
      

           
        
        app.exec_()
              
        
        
    
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
            
        
'''---------- EXECUÇÃO DO SISTEMA ----------'''
if __name__ == '__main__':
   main()
   
           
        

