# imports
import sqlite3
import traceback

# imports locais
import m_Err


# Cria conexão com o BD e retorna conexão
def createConnection(databasefile):
           
    # Inicializa a variável    
    connDB = None
    
    try:
        # Conecta com o BD
        connDB = sqlite3.connect(databasefile)
        
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())
     
       
    # Retorna a conexão
    return connDB



# TODO Criar rotina para criação de tabelas, caso não existam
'''
    CREATE TABLE "cadSysUser" (
        "UserID"	INTEGER NOT NULL UNIQUE,
        "UserNickName"	TEXT NOT NULL UNIQUE,
        "UserAccessNumber"	INTEGER NOT NULL,
        "UserLastAccess"	TEXT NOT NULL,
        "UserPassword"	TEXT NOT NULL UNIQUE,
        PRIMARY KEY("UserID")
    );

'''