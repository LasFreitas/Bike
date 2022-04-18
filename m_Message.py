import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets

from enum import Enum

# imports localis
import m_Var
import m_Image
#import F000Splash





   

def window(strMessage, strTittle = m_Var.strSystem, typeButtons = m_Var.Button_Message.m_OkCancel, typeIcon = m_Var.Icon_Message.m_Information):

    app = QApplication(sys.argv)


    msgBox = QMessageBox()
    msgBox.setWindowIcon(QtGui.QIcon(m_Image.Load_Image('BikeSys.png')))

    msgBox.setText(strMessage)
    msgBox.setWindowTitle(strTittle)

    if typeIcon.value == 0:
        msgBox.setIcon(QMessageBox.Critical)
    elif typeIcon.value == 1:
        msgBox.setIcon(QMessageBox.Warning)
    elif typeIcon.value == 2:
        msgBox.setIcon(QMessageBox.Information)
    elif typeIcon.value == 3:
        msgBox.setIcon(QMessageBox.Question)

    if typeButtons.value == 0:
        msgBox.setStandardButtosns(QMessageBox.Ok)
    elif typeButtons.value == 2:
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
    elif typeButtons.value == 3:
           msgBox.setStandardButtons(QMessageBox.Yes)     
    elif typeButtons.value == 4:
           msgBox.setStandardButtons(QMessageBox.Open)  
    elif typeButtons.value == 5:
           msgBox.setStandardButtons(QMessageBox.Save)  


    msgBox.buttonClicked.connect(msgButtonClick)




    returnValue = msgBox.exec()



  
def msgButtonClick(i):
  print("Button clicked is:",i.text())

#if __name__ == '__main__':
#   window()


