# !/usr/bin/python
# -*- coding: UTF-8 -*-

# imports
import sys
import traceback
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QLabel, QSlider, QColorDialog, QApplication, QDesktopWidget)
from PyQt5.QtGui import QColor, QFont
from PyQt5 import QtWidgets, uic, Qt, QtCore
from colorsys import rgb_to_hsv, hsv_to_rgb

# imports locais
import m_Var
import m_Text
import m_Err


# Definição de varíaveis para utilização deste script
cor = ""
clrFont = ""

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        self.btn.clicked.connect(self.showDialog)

        self.lbl = QLabel(self)
        self.lbl.setText("CONTRAST")
        self.lbl.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.lbl.setFont(QFont('Arial', 60)) 
        self.lbl.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lbl.setGeometry(130, 22, 500, 300)
        
        self.sli = QSlider(self)
        self.sli.maximum=9
        self.sli.minimum=0
        self.sli.value=0
        self.sli.setGeometry(20,20,20,200)
        self.sli.move(20,70)
        self.sli.setTickPosition(QSlider.TicksBelow)
        self.sli.setTickInterval(10)               
        self.sli.valueChanged.connect(self.qsi)
       
        self.setGeometry(300, 300, 650, 350)
        self.setWindowTitle('Color dialog')
        self.center()
        self.show()

    def showDialog(self):
        
        try:
            # Define o valor do slider
            #self.sli.valueChanged=0
            #self.sli.valueChanged.connect(self.qsi)
            
            # Obtêm a cor
            col = QColorDialog.getColor()

            # Verifica se a cor é válida
            if col.isValid():
                
                # Atualiza variável com a nova cor
                global cor
                cor = col.name()
                    
                # Atualiza variável com a cor da fonte contrastante 
                global clrFont
                clrFont = textcontrast(cor)
                        
                # Atualiza cor do controle
                self.lbl.setStyleSheet("QLabel { background-color :"+col.name()+" ; color :" + clrFont + "}")
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
    """ Função para checar as modificações de valor do Slider """
    def qsi(self, value):
        
        
        try:
            # Define a nova cor de acordo com valor
            corShade = screenshades(cor,value / 100)
        
            # Atualiza varíavel com a fonte de contraste
            global clrFont
            clrFont =  textcontrast(corShade)
        
            # Aplica as novas cores ao controle             
            self.lbl.setStyleSheet("QLabel { background-color :"+ corShade +" ; color :" + clrFont + "}")
        
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
    """ Função para centralizar o form """
    def center(self):
        try:
           qr = self.frameGeometry()
           cp = QDesktopWidget().availableGeometry().center()
           qr.moveCenter(cp)
           self.move(qr.topLeft())
           
        except Exception as e:
             # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())




""" Função para converter cor em Hexadecimal """             
def hex_to_rgb(value):
        
        try:
            # Converte o valor da cor em Hexadecimal
            value = value.lstrip('#')
            lv = len(value)
            return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))  
        
        except Exception as e:
             # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())

""" Função para definir cor de contraste do controle """  
def textcontrast(color):
    try:
        """ Recebe valor da cor em HEXADECIMAL """
        # Convert cor HEX em RGB
        color = hex_to_rgb(color)
        
        # Obtêm os valores de cada cor
        clrRed =color[0]
        clrGreen=color[1]
        clrBlue =color[2]
        
        # Atualiza variável  
        intLimite = 105
        
        # Calcula o grau da cor
        intDelta = int((clrRed * 0.299) + (clrGreen * 0.587) + (clrBlue * 0.114))
        
        # Verifica se o valor calculado é menor que o limite estipulado
        if 255 - intDelta <= intLimite:
            # Retorna a cor escura
            return m_Var.clrFontDark
        else:
            # Retorna a cor clara
            return m_Var.clrFontClear
                    
    except Exception as e:
         # Atualiza arquivo de erro com o erro ocorrido
         m_Err.printErr(traceback.format_exc())

""" Função para definir cor do fundo de acordo com o valor correção de fator """
def screenshades(color, correctionfactor, blnRed = True, blnGreen = True, blnBlue = True):
      try:
          
        
        """ Recebe valor da cor em HEXADECIMAL e retorna o valor da cor em HEXADECIMAL """
         # Convert cor HEX em RGB
        color = hex_to_rgb(color)
                
        # Obtêm os valores de cada cor
        clrRed =color[0]
        clrGreen=color[1]
        clrBlue =color[2]
        
        # Verifica se o fator de correção é menor que zero
        if correctionfactor < 0:
            
            # Se for menor que zero acrescenta 1 ao valor
            correctionfactor = 1 + correctionfactor
            
            # Verifica se é para considerar a cor Vermelho            
            if blnRed:
                # Atualiza a variável
                clrRed *= correctionfactor
            # Verifica se é para considerar a cor Verde
            if blnGreen:
                # Atualiza a variável
                clrGreen *= correctionfactor
            # Verifica se é para considerar a cor Azul
            if blnBlue:
                # Atualiza a variável
                clrBlue *= correctionfactor
                
        else:
            
            # Verifica se é para considerar a cor Vermelho
            if blnRed:
                # Atualiza a variável
                clrRed = int((255 - clrRed) * correctionfactor + clrRed)

            # Verifica se é para considerar a cor Verde                
            if blnGreen:
                # Atualiza a variável
                clrGreen = int((255 - clrGreen) * correctionfactor + clrGreen)
            
            # Verifica se é para considerar a cor Azul
            if blnBlue:
                # Atualiza a variável
                clrBlue = int((255 - clrBlue) * correctionfactor + clrBlue)
                   
        # Atualiza a varíavel
        corShade = (clrRed, clrGreen, clrBlue)
        
        # Converte a cor em Hexadecimal
        hex_result = "".join([format(val, '02X') for val in corShade])
        
        # Retorna o valor da nova cor em Hexadecimal
        return (f"#{hex_result}")
        
        
      except Exception as e:
           # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()    
