# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sys
import traceback


# imports locais
import m_Err





'''---------- FUNÇÕES ----------'''
# Encerra a aplicação
def System_End():
    
    try:
      quit()
      #sys.exit()
    
    except Exception as e:
       # Atualiza arquivo de erro com o erro ocorrido
       m_Err.printErr(traceback.format_exc())
       


# Função para minimizar form
# TODO Refazer esta função para minimizar o form
def Form_Minimized(objForm):
       try:
          
          objForm.showMinimized()
          
          
       except Exception as e:
         # Atualiza arquivo de erro com o erro ocorrido
         m_Err.printErr(traceback.format_exc())