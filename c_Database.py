# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import sqlite3
import traceback
import enum
#import logging

# imports locais
import m_Err
import m_Var

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog
from PyQt5 import QtWidgets, uic, Qt, QtCore, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class Type_Operation(enum.Enum):
    m_Insert = 0
    m_Update = 1
    m_Delete = 2
    
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)    


class Database(object):
    
      
    
    try:
        
        
        
        instance = None
        
        db_location = m_Var.strDirSystem + "\\DATABASE\\" + m_Var.strDatabaseFileName
        
        
        def __new__(cls, *args, **kwargs):
            
            if cls.instance is None:
                cls.instance = super().__new__(Database)
                return cls.instance
            return cls.instance
        
        
        def __init__(self):
        
            try:
                self.conn = sqlite3.connect(Database.db_location)
                self.cursor = self.conn.cursor()
                #self.conn.set_trace_callback(logging.debug)
                                    
            except sqlite3.Error as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())    
           
    
        def __enter__(self):
            
            return self

        def __exit__(self, ext_type, exc_value, traceback):
            
            self.cursor.close()
            if isinstance(exc_value, Exception):
                self.conn.rollback()
            else:
                self.conn.commit()
            self.conn.close()
    
        
        ''' ---------- PESQUISA NO BANCO DE DADOS ---------- '''
        def Search_Row(self, strTable, strField, strValue):
            try:
               
                # Monta instru????o SQL
                strSql = 'SELECT * FROM ' + strTable.lower() + ' WHERE ' + strField.lower() + ' = "' + strValue + '"'
                
                 # Seleciona registro conforme solicitado
                self.cursor.execute(strSql) #'SELECT * FROM cadSysUser WHERE userPassword="' + strValue + '"')
                dataRow = self.cursor.fetchone()
                
                # Retorna dados solicitados
                return dataRow
                                
            except sqlite3.Error as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())      
    
        ''' ---------- OPERA????ES COM REGISTRO ---------- '''
        def Crud_Record(self, strTable, lstData, strWhere, typeOperation = Type_Operation):
            
             
            try:
                # Vari??vel para montagen de instru????o SQL      
                strSql = ''
                              
                # Executa for para obten????o dos nomes dos campos
                lstFieldName = [i[0] for i in self.cursor.description]
                
                 # Insere o nome da tabela na primeira posi????o               
                lstFieldName.insert(0, strTable)
                
                # Atualiza vari??vel com a instru????o SQL
                strSql = self.Create_Sql(lstFieldName, typeOperation.value)
                                
                # Verifica se existe cl??usula WHERE e adiciona na string sql
                if strWhere is not None:
                     
                     strSql +=  ' WHERE ' + strWhere 
                     
                
                # Executa a instru????o SQL   
                self.cursor.execute(strSql, lstData)   
                # Grava as altea????es no BD
                self.conn.commit()
                
                # 
                return True
                
            except sqlite3.Error as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())       
                # Em caso de erro retorna FALSE
                return False
            
        def Create_Sql(self, lstFields, intTypeOperation):
            
            try:
                
                # Inicializa vari??vel
                str_Sql =''
                
                # Verifica qual o tipo de opera????o
                if intTypeOperation == 0:       # --- INSERT ---
                   
                    ''' INSERT INTO nome_da_tabela (coluna1, coluna2, coluna3,..) VALUES ( valor1, valor2, valor3,..); '''
                    
                    # Executa for para obten????o dos nomes
                    for i in range(len(lstFields)):
                        
                        # Verifica se ?? o primeiro item da lista
                        if i == 0:
                            
                            # Atualiza instru????o SQL    
                            str_Sql = 'INSERT INTO ' + lstFields[i].lower() + ' ( '
                        
                        # Outros Itens da lista
                        elif i > 0:
                            
                            # Atualiza instru????o SQL com os outros itens                    
                            str_Sql += lstFields[i] + ', '
                        
                    # Retorna sintru????o SQL atualizada
                    return str_Sql[0:-2] + ") VALUES "  
                    
   
                elif intTypeOperation == 1:     # --- UPDATE ---
                   
                    ''' UPDATE table_name SET column1 = value1, column2 = value2...., columnN = valueN WHERE [condition]; '''
                    
                    # Executa for para obten????o dos nomes
                    for i in range(len(lstFields)):
                        
                        # Verifica se ?? o primeiro item da lista
                        if i == 0:
                            
                            # Atualiza instru????o SQL    
                            str_Sql = 'UPDATE ' + lstFields[i].lower() + ' SET '
                        
                        # Outros Itens da lista
                        elif i > 0:
                            
                            # Atualiza instru????o SQL com os outros itens                    
                            str_Sql += lstFields[i] + ' = ?, '
                        
                    # Retorna sintru????o SQL atualizada
                    return str_Sql[0:-2]
                
                elif intTypeOperation == 2:     # --- DELETE ---
                   
                    ''' DELETE FROM table_name WHERE [condition]; '''
                    
                    # FIXME VERIFICAR MONTAGEM INSTRU????O SQL
                    
                    # Atualiza instru????o SQL    
                    str_Sql = 'DELETE FROM ' + lstFields[0].lower() 
                    
                    
                
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())    
                
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())
    

