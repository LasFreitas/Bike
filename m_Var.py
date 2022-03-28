import os
import socket  


import m_Color

''' NOME DO USUÁRIO '''
strUser = ""    

''' NOME DO SISTEMA '''
strSystem = "Bike - Estatísticas"

''' NOME DO COMPUTADOR e IP '''
# Obtêm o nome e ip do computador
strComputer = socket.gethostname()    
strIP = socket.gethostbyname(strComputer)    

''' DATABASE '''
strVersion = ''

''' DIRETÓRIOS DE TRABALHO '''
lstDirectory = ['DATA', 'EXPORT', 'IMPORT','LOG', 'ERR', 'ICONS', 'REPORT', 'BACKUP']

''' BACKUP '''
intBkpDays = 5


''' DIRETÓRIOS DO SISTEMA '''
# Formulários
strScreen = os.getcwd() + '\\Screen\\'
# Database
strDatabase = os.getcwd() + '\\Data\\'

''' CORES DO SISTEMA '''
clrColorClear = "#f5f5f5"
clrColorDark = "#004d40" #00695c"

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
fntSystem = 'Tahoma,16,normal,normal'
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
    
    
    
    
    
def setVar(strKey, strValor):
    try:
        globals() [strKey] 
        [strKey]= strValor
       
        print(strVersion)
    except Exception as e:
        raise e

def getVar(strKey):
    try:
        
        #globals() [strKey] 
        return   globals() [strKey]
       
    except Exception as e:
        raise e