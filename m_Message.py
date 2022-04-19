import sys
import traceback
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets

from enum import Enum

# imports locais
import m_Var
import m_Image
import m_Err
  

def window(strMessage, strTittle = m_Var.strSystem, typeButtons = m_Var.Button_Message.m_OkCancel, typeIcon = m_Var.Icon_Message.m_Information):

    #app = QApplication(sys.argv)


    msgBox = QMessageBox()
    msgBox.setWindowIcon(QtGui.QIcon(m_Image.Load_Image('BikeSys.png')))

    msgBox.setText(strMessage)
    
    
    # Verifica se foi passado o título da mensagem
    if strTittle == '':
      strTittle = m_Var.strSystem
    
    
    msgBox.setWindowTitle(strTittle)

    if typeIcon.value == 0:
        msgBox.setIcon(QMessageBox.Critical)
    elif typeIcon.value == 1:
        msgBox.setIcon(QMessageBox.Warning)
    elif typeIcon.value == 2:
        msgBox.setIcon(QMessageBox.Information)
    elif typeIcon.value == 3:
        msgBox.setIcon(QMessageBox.Question)


    # Verifica qual(is) botão(ões) será(ão) exibido(s)
    if typeButtons.value == 0:
        msgBox.setStandardButtons(QMessageBox.Ok)
    elif typeButtons.value == 1:
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
    elif typeButtons.value == 2:
           msgBox.setStandardButtons(QMessageBox.Yes)     
    elif typeButtons.value == 3:
           msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)     
    elif typeButtons.value == 4:
           msgBox.setStandardButtons(QMessageBox.Open)  
    elif typeButtons.value == 5:
           msgBox.setStandardButtons(QMessageBox.Save)  
    elif typeButtons.value == 10:
           msgBox.setStandardButtons(QMessageBox.NoButton) 
           
           


    if typeButtons.value == 10:
        
        
        #msgBox.exec_()
               
        QTimer.singleShot(2000, msgBox.exec(), msgBox.accept())
#
# 
# QTimer.singleShot(5000,  msgBox.done(1))
        
        
        
        #QTimer.singleShot(50,  msgBox.accept())
        
        
        print(True)
        
    else:
        ReturnMSG = msgBox.exec_()

        if ReturnMSG == QMessageBox.Ok:
            print(True)
        elif ReturnMSG == QMessageBox.Cancel:
            print(False)
        else:
            pass    
    



    
    
    
    
   
    
   
  
  
  
  
  #print("Button clicked is:",i.text())




