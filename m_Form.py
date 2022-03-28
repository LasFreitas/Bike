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


def formConfigControl(objForm):
    try:
               
        fntDefault = m_Var.fntSystem.split(',')
           
        # Configura cor de fundo do form
        objForm.setStyleSheet('background-color: ' + str(m_Var.clrColorClear)) 
             
        # Centraliza o form
        objForm.move(m_Form.centerForm(objForm))    
           
           
        # Percorre os controles do form para configuração
        for widget in objForm.children():
             
            # Configura BUTTON           
            if isinstance(widget, QPushButton):
                
               widget.setStyleSheet('QPushButton {'   
                                     + 'font-family:' + str(fntDefault[0]) + ';' 
                                     + 'font-size:' +  fntDefault[1] + 'px ;'
                                     + 'font-Weight:' + str(fntDefault[2]) + ';'
                                     + 'font-style:' + str(fntDefault[3]) + ';'
                                     + "background-color: " + str(m_Var.clrColor90) + ';'
                                     + 'color:' + str(m_Color.textcontrast(m_Var.clrColor90)) + ';'
                                     + ';}' )

             # Configura LABEL           
            elif isinstance(widget, QLabel):
                              
               widget.setStyleSheet('QLabel {'   
                                     + 'font-family:' + str(fntDefault[0]) + ';' 
                                     + 'font-size:' +  fntDefault[1] + 'px ;'
                                     + 'font-Weight:' + str(fntDefault[2]) + ';'
                                     + 'font-style:' + str(fntDefault[3]) + ';'
                                     + "background-color: " + str(m_Var.clrColorClear) + ';'
                                     + 'color:' + str(m_Color.textcontrast(m_Var.clrColorClear)) + ';'
                                     + ';}' )
            
            # Configura LINE           
            elif isinstance(widget, QFrame):
                              
               widget.setStyleSheet('QFrame {'   
                                     + 'color:' + str(m_Var.clrColorDark) + ';'
                                     + ';}' )
                
            
                
            else:
                pass
               
                                   
                
                
                
              
       
    
    
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    






''' Função para configurar o form '''
def formConfig1(strFormat):
    try:
        # Divide a configuração em itens
        fconfig = strFormat.split('|')
        
        fntDefault = m_Var.fntSystem.split(',')
    
        objFormat =''
    
        if strFormat != "":
            
            for i in  fconfig:
                ''' formata as cores do controle '''            
                if i.upper() == 'SYS':
                    objFormat =  "background-color: " + m_Var.clrColorDark + ';'
                    objFormat += "color: " + m_Color.textcontrast(m_Var.clrColorDark) + ';'
                
                elif i.upper()[:2] == 'FS':
                    objFormat += "font: " + i[2:] + "pt " + fntDefault[0] + ";"
                
                elif i.upper() == 'MSG':
                    objFormat += "color: " + 'Red' + ';'
        else:
            objFormat =  "background-color: " + m_Var.clrColorClear + ';'
            objFormat += "color: " + m_Color.textcontrast(m_Var.clrColorClear) + ';'
            objFormat += "font: " + fntDefault[1] + "pt " + fntDefault[0] + ";"        
                          
                    
            
        return objFormat
               
        # "background-color: rgb(85, 170, 0);color: rgb(0, 85, 255);font: 87 12pt \"Arial Black\";"
                   
    except Exception as e:
        raise e
    


def centerForm(object):
    # Centraliza form na tela
    qtRectangle = object.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    return(qtRectangle.topLeft())
