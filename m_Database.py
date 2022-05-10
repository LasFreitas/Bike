# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sqlite3
import traceback

# imports locais
import m_Err
import m_Var





def Open_Database():
    try:

        if m_Var._dbConnection == None:
            
            # Conecta com o BD
            m_Var._dbConnection = sqlite3.connect(m_Var.strDirSystem + "\\DATABASE\\" + m_Var.strDatabaseFileName)

            #
            return True
            
        else:       
           
            # Fecha a conexão
            m_Var._dbConnection.close()
            
            #
            return False
        
    except Exception as e:
    
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())
        
    

    
    
    
def Get_Database(strTable, strField, strFieldWhere = None, strFieldOrder = None):
    try:
        
        
        
        
        
        # Realiza a conexão com o banco de dados
        if Open_Database() == True:
            
            # Atualiza string para conexão com a tabela desejada
            m_Var._dbCommandText +=  strTable.lower()
                        
            # Verifica se é para selecionar registros
            if strFieldWhere is not None:
                
                m_Var._dbCommandText += " WHERE " + strFieldWhere.lower() + " = "
                
                print(m_Var._dbCommandText)
                
                if strTable.upper() == "CADSYSUSER":
                    pass
                    
            
        
        else:
            
            #   NÃO CONECTOU O BANCO DE DADOS
            pass
        
    
    
    
    
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())  
    
    
    
    


    
        
        

