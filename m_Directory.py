# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import os
import traceback

# imports locais
import m_Text
import m_Err
#import m_Message


# FUNÇÃO PARA CHECAR DIRETÓRIOS DO SISTEMA
def checkSystemDirectory(strDirectory):
   
   try:
       # Itera lista para verificação dos diretórios
       for dir in strDirectory:
          # Se não existir o diretório, cria automaticamente
           if not createDirectory(os.getcwd() + '\\' + dir.capitalize(), True):
              pass
          
   except Exception as e:
       # Atualiza arquivo de erro com o erro ocorrido
      m_Err.printErr(traceback.format_exc())
   
   
   

# FUNÇÃO PARA A CRIAÇÃO DE DIRETÓRIOS DO SISTEMA
def createDirectory(strDirectory, blnCreate = False):
  
  try:
      # Verifica se diretório não existe
      if not os.path.exists(strDirectory):
           # Verifica se e para criar o diretório
           if blnCreate:
               # Cria o diretório
               os.makedirs(str(strDirectory))
               # Atualiza arquivo de log
               m_Text.write_texto("LOG","CRIAÇÃO DE DIRETÓRIO DO SISTEMA|" + strDirectory)
      else:
          #M_Message.window("CRIAÇÃO DE DIRETÓRIO DO SISTEMA|")
          pass
  
  except Exception as e:
      # Atualiza arquivo de erro com o erro ocorrido
      m_Err.printErr(traceback.format_exc())
  