import os
import socket  
import enum


import m_Color

''' NOME DO USUÁRIO '''
strUser = "SYSTEM"    

''' NOME DO SISTEMA '''
strSystem = "Bike - Estatísticas"

''' NOME DO COMPUTADOR e IP '''
# Obtêm o nome e ip do computador
strComputer = socket.gethostname()    
strIP = socket.gethostbyname(strComputer)    

''' DATABASE '''
strDatabaseFile = 'BK'
strDatabaseExension = 'DB'
strDatabaseFileName = "BIKE.DB"

''' DIRETÓRIOS DE TRABALHO '''
lstDirectory = ['DATABASE', 'EXPORT', 'IMPORT','LOG', 'ERR', 'ICONS', 'REPORT', 'BACKUP']


''' BACKUP '''
# Dias para guardar os arquivos de DADOS
intBkpDays = 5

# Dias para guardar os arquivos de LOG/ERR
# FIXME Mudar data para 180 dias
intBkpLogErr = 10

# Tipos de arquivos a serem controlados pelo BACKUP/DELETE
# DB = DATABASE
# ERR = Arquivo de ERROS do sistema
# LOG = Arquivo de LOG do sistema
strBkpDelFiles = 'DB|ERR|LOG'


''' DIRETÓRIOS DO SISTEMA '''

# Diretório do sistema
strDirSystem = os.getcwd()


''' CORES DO SISTEMA '''
clrColorClear = "#f5f5f5"
clrColorDark = "#fdd835" #00695c"

clrColor10 = m_Color.screenshades(clrColorDark,0.1)
clrColor20 = m_Color.screenshades(clrColorDark,0.2)
clrColor30 = m_Color.screenshades(clrColorDark,0.3)
clrColor40 = m_Color.screenshades(clrColorDark,0.4)
clrColor50 = m_Color.screenshades(clrColorDark,0.5)
clrColor60 = m_Color.screenshades(clrColorDark,0.6)
clrColor70 = m_Color.screenshades(clrColorDark,0.7)
clrColor80 = m_Color.screenshades(clrColorDark,0.8)
clrColor90 = m_Color.screenshades(clrColorDark,0.9)

clrFontClear = "#ffffff" 
clrFontDark = "#311b92"

''' FONTES DO SISTEMA '''
#fntSystem font family, size, Weight, style
fntSystem = 'Consolas,14,normal,normal'
fntReport = 'Courier,9'










''' FUNÇÃO ATRIBUIÇÃO NOME DO USUÁRIO A VARIÁVEL '''
def setUser(strUsuario):
    try:
        global strUser
        strUser = strUsuario
    except Exception as e:
        pass
    
''' FUNÇÃO RETORNO NOME DO USUÁRIO '''    
def getUser():
    try:
        # Verifica se variável já foi definida
        if not strUser:
            return "SYSTEM"   
        else:
            return strUser
        
    except Exception as e:
        pass
    
    
''' ERROR ''' 
blnError = False
    
    
def setVar(strKey, strValor):
    try:
        globals() [strKey] 
        [strKey]= strValor
       
        #print(strVersion)
    except Exception as e:
        raise e

def getVar(strKey):
    try:
        
        #globals() [strKey] 
        return   globals() [strKey]
       
    except Exception as e:
        raise e