# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sqlite3
import traceback

# imports locais
import m_Err
import m_Var

FlagDbConnection = False


class Database():
       
    try:
        
        
        
        
        def __init__(self):
             
            # Inicializa a variável    
            self.dbConnection = None
            
            # Conecta com o BD
            self.dbConnection = sqlite3.connect(sqlite3.connect(m_Var.strDirSystem + "\\DATA\\" + m_Var.strDatabaseFileName))
            
            global FlagDbConnection
            FlagDbConnection = True
        
        def __del__(self):
            
            # Fecha a conexão
            self.dbConnection.close()
            
            
        def GetDB(self, strTable, strField, strFieldWhere = None, strFieldOrder = None):
            pass
        
            
            
            
           
        
        
        
           
            
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
            
    