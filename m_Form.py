# !/usr/bin/python
# -*- coding: UTF-8 -*-

# imports
import traceback
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QListWidgetItem, QTableWidgetItem, QDialog, QDesktopWidget, QWidget,QGroupBox, QPushButton,QFontComboBox,QFontDialog
from PyQt5.QtGui import QColor, QFont

# imports locais
import m_Var
import m_Err
import m_Color
import m_Form

 # Definição de variáveis
       
''' ---------- FONTE ---------- '''
fntControl = m_Var.fntSystem.split(',')

fntControlFamily = fntControl[0]
fntControlSize = fntControl[1]
fntContolWeigth = fntControl[2]
fntControlBold = fntControl[3]

''' ---------- COR ---------- '''
clrControlBackcolor = m_Var.clrColorClear
clrControlForecolor = m_Var.clrColorDark





def Form_Center(object):
    # Centraliza form na tela
    qtRectangle = object.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    return(qtRectangle.topLeft())

def Form_Config(objForm):
    try:
             
        # Centraliza o form
        objForm.move(m_Form.Form_Center(objForm))    
              
        # Executa loop para configurar os controles
        for objForm in dict(objForm.__dict__).items():
              
            try:
                                          
               # Verifica se é para formatar o controle
               if objForm[1].accessibleName()> "":
                    
                   # Configura o controle conforme as especifícações
                   Form_Config_Control(objForm[1].accessibleName().upper().split("|"))
                   
                   
                   
                   print(objForm[1])
                   
                   if type(objForm[1]) == QLabel:
                  
                        objForm[1].setStyleSheet('QLabel {'   
                                    + 'font-family:' + fntControlFamily + ';' 
                                    + 'font-size:' +  fntControlSize + 'px ;'
                                    + 'font-Weight:' + fntContolWeigth + ';'
                                    + 'font-style:' + fntControlBold + ';'
                                    + 'background-color: ' + clrControlBackcolor + ';'
                                    + 'color: ' + clrControlForecolor + ';'
                                    + ';}' )
                  
                   elif type(objForm[1]) == QFrame:
                      
                        objForm[1].setStyleSheet('QFrame {'   
                                    + 'background-color: ' + clrControlBackcolor + ';'
                                    + ';}' )
                    
                   
            
            except:
                pass
            
       
    
    
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
def Form_Config_Control(strConfigControl):
    try:
        
        print(strConfigControl)
        
        # Executa loop para configurar controle
        for i in range(len(strConfigControl)):
           
            print(strConfigControl[i])
            
            if strConfigControl[i] == "SYS": # CORES DO SISTEMA
               
                m_Form.clrControlBackcolor = m_Var.clrColorDark
               
                m_Form.clrControlForecolor = m_Var.clrFontClear #m_Color.textcontrast(clrControlBackcolor)
                
                
                
                '''
                
                strFormatBackground ='background-color: ' + str(m_Var.clrColorDark)
                strFormatForeground = 'color: ' + str(m_Color.textcontrast(m_Var.clrColorDark))
                             
                '''
            
            # return True
            #return False        


                    


    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    



