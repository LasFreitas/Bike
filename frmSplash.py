# encoding: utf-8
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
import time
import traceback

import sys
import os
import time
import threading
import m_Var
import m_Text
import m_Form
#import m_Image
import m_Backup
import frmMain
import m_Err


class Ui_Splash(QtWidgets.QDialog):
    
    def __init__(self):
       
        super(Ui_Splash, self).__init__()
       
        uic.loadUi(m_Var.strDirSystem + '\\Screen\\FrmSplash.ui', self)

        self.setStyleSheet("QDialog { background-color:" + m_Var.clrColorClear + " }");
       

        # Instância label título e modifica texto
        lbTittle = self.findChild(QtWidgets.QLabel, 'lbTittle')
        lbTittle.setText(m_Var.strSystem)

        lbMessage = self.findChild(QtWidgets.QLabel, 'lbMessage')
        lbMessage.setText('')

        # Instância e carrega imagem
        # lbImage = self.findChild(QtWidgets.QLabel, 'lbImage')
        # lbImage.setText('')

        # Atualiza label 
        lbMessage.setText('AGUARDE... VERIFICANDO O SISTEMA')

        # Esconde a barra de título e mantêm o form por cima 
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
       

    def execBackup(self):
        try:
            # Executa rotina de Backup e Deleta arquivos antigos
            # FIXME Implementar rotina de BACKUP 
               
            # Cria instância do módulo de BACKUP 
            classBackup = m_Backup.Backup()
    
            # Deleta os arquivos de backup dos dados (DATABASE/ERROS/LOG) antigos
            classBackup.delete_file(self.lbMessage)
            
            # Realiza backup do banco de dados (DATABASE/ERROS/LOG) antigos
            classBackup.backup_file(self.lbMessage)
            
            
            
            
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
    
           
        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
        #

def main():
    
    try:
        # Atualiza arquivo de log com a data e hora da inicialização do sistema
        m_Text.write_texto("LOG", "INICIALIZAÇÃO DO SISTEMA", "LOG", True)
    
        app = QtWidgets.QApplication(sys.argv) 
        window = Ui_Splash()
        window.show()
        
        QTimer.singleShot(50, window.execBackup)
                   
        QTimer.singleShot(5000, window.close)
        
        app.exec_()
        
        frmMain.main()
        
      
      
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())


if __name__ == '__main__':
    main()
    