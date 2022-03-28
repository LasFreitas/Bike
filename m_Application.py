# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sys
import traceback


# imports locais
import m_Err





'''---------- FUNÇÕES ----------'''
# Encerra a aplicação
def endApplication():
    
    try:
       sys.exit()
    
    except Exception as e:
       # Atualiza arquivo de erro com o erro ocorrido
       m_Err.printErr(traceback.format_exc())
