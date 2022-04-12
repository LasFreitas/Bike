# !/usr/bin/python
# -*- coding: UTF-8 -*-

# imports
import traceback
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QListWidgetItem, QTableWidgetItem, QDialog, QDesktopWidget, QWidget,QGroupBox, QPushButton,QFontComboBox,QFontDialog
from PyQt5.QtGui import QColor, QFont, QPixmap

# imports locais
import m_Var
import m_Err
import m_Color
import m_Form
import m_Image

 # Definição de variáveis
       
''' ---------- FONTE ---------- '''
fntControl = m_Var.fntSystem.split(',')

fntControlFamily = fntControl[0]
fntControlSize = fntControl[1]
fntControlWeigth = fntControl[2]
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
          
        # Configura cor de fundo do form
        objForm.setStyleSheet('background-color: ' + str(m_Var.clrColorClear))     
              
        # Executa loop para configurar os controles
        for objForm in dict(objForm.__dict__).items():
            
            
            
            try:
                                          
               # Verifica se é para formatar o controle
               if objForm[1].accessibleName()> "":
                    
                   # Configura o controle conforme as especifícações
                   Form_Config_Control(objForm[1].accessibleName().upper().split("|"))
                   
                   # Verifica qual é o tipo do controle e formata
                   if type(objForm[1]) == QLabel: # LABEL
                  
                        objForm[1].setStyleSheet('QLabel {'   
                                    + 'font-family:' + fntControlFamily + ';' 
                                    + 'font-size:' +  fntControlSize + 'px ;'
                                    + 'font-Weight:' + fntControlWeigth + ';'
                                    + 'font-style:' + fntControlBold + ';'
                                    + 'background-color: ' + clrControlBackcolor + ';'
                                    + 'color: ' + clrControlForecolor + ';'
                                    + ';}' )
                        
                   elif type(objForm[1]) == QPushButton: # QPUSHBUTTON
                    
                        objForm[1].setStyleSheet('QPushButton {' 
                                    + 'font-family:' + fntControlFamily + ';' 
                                    + 'font-size:' +  fntControlSize + 'px ;'
                                    + 'font-Weight:' + fntControlWeigth + ';'
                                    + 'font-style:' + fntControlBold + ';'
                                    + 'background-color: ' + clrControlBackcolor + ';'
                                    + 'color: ' + clrControlForecolor + ';'
                                    + ';}' )
                        
                   elif type(objForm[1]) == QFrame: # QFRAME
                      
                        objForm[1].setStyleSheet('QFrame {'   
                                    + 'background-color: ' + clrControlBackcolor + ';'
                                    + ';}' )
                   
                   elif type(objForm[1]) == QGroupBox: # QGROUPBOX
                      
                        objForm[1].setStyleSheet('QGroupBox {'   
                                    + 'background-color: ' + clrControlBackcolor + ';'
                                    + ';}' )
                            
                   elif type(objForm[1]) ==  QRadioButton: # RADIOBUTTON
                                    
                        objForm[1].setStyleSheet('QRadioButton {'   
                                            + 'font-family:' + fntControlFamily + ';' 
                                            + 'font-size:' +  fntControlSize + 'px ;'
                                            + 'font-Weight:' + fntControlWeigth + ';'
                                            + 'font-style:' + fntControlBold + ';'
                                            + 'background-color: ' + clrControlBackcolor + ';'
                                            + 'color: ' + clrControlForecolor + ';'
                                            + ';}' )
                                                
                   elif type(objForm[1]) ==  QCheckBox: # CHECKBOX
                                    
                        objForm[1].setStyleSheet('QCheckBox {'   
                                            + 'font-family:' + fntControlFamily + ';' 
                                            + 'font-size:' +  fntControlSize + 'px ;'
                                            + 'font-Weight:' + fntControlWeigth + ';'
                                            + 'font-style:' + fntControlBold + ';'
                                            + 'background-color: ' + clrControlBackcolor + ';'
                                            + 'color: ' + clrControlForecolor + ';'
                                            + ';}' )
                    
                  
            except:
                pass
               
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
def Form_Config_Control(strConfigControl):
    try:
        
        # Reseta as configurações com o padrão do sistema
        ''' ---------- FONTE ---------- '''
        m_Form.fntControl = m_Var.fntSystem.split(',')

        m_Form.fntControlFamily = fntControl[0]
        m_Form.fntControlSize = fntControl[1]
        m_Form.fntControlWeigth = fntControl[2]
        m_Form.fntControlBold = fntControl[3]

        ''' ---------- COR ---------- '''
        m_Form.clrControlBackcolor = m_Var.clrColorClear
        m_Form.clrControlForecolor = m_Var.clrColorDark
        
        
        # Executa loop para configurar controle
        for i in range(len(strConfigControl)):
           
            #print(strConfigControl[i])
            
            ''' ---------- CORES ---------- '''
            
            if strConfigControl[i] == "SYS": # CORES DO SISTEMA
               
                # Configura com a cor de fundo do sistema
                m_Form.clrControlBackcolor = m_Var.clrColorDark
                
            elif strConfigControl[i] == "BUT": # CORES DOS BOTÕES

                # Configura cor de fundo do botão
                m_Form.clrControlBackcolor = m_Var.clrColor90
               
            
                ''' ---------- FONTE ---------- '''
            
            elif strConfigControl[i] == "FB": # FONTE BOLD DOS BOTÕES  
               
                # Configura fonte como negrito      
                m_Form.fntControlWeigth = 'bold'
                
            elif strConfigControl[i][:2] == "FS": # TAMANHO DA FONTE DOS BOTÕES  
               
                # Configura fonte como negrito      
                m_Form.fntControlSize = (strConfigControl[i][2:5]).strip()
                
                
                
            # Configura fonte conforme o fundo do controle
            m_Form.clrControlForecolor = m_Color.textcontrast(clrControlBackcolor)
            
            
            

                    


    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    



