

# imports 
from datetime import datetime
from pathvalidate import is_valid_filename, sanitize_filename
#from os import write, path
import os
import traceback

# imports locais
import m_Err
import m_Var



''' DEFINIÇÃO DE VARIÁVEIS PARA UTILIZÇÃO DESTE SCRIPT '''

# Obtêm o diretório do sistema
strPath = os.getcwd() + "\\"
strSubPath = ""

# Define data atual
dtDate = datetime.now()
dtFileDate = dtDate.strftime("%Y%m%d")[-6:]
dtDate = dtDate.strftime("%d/%m/%Y")

# Define hora atual
tmTime = datetime.now()
tmTime = tmTime.strftime("%H:%M:%S")



# Função para gravar texto em arquivo
def write_texto(strFileName, strText, strExtension = "TXT", blnFileNameDate = True):
    try:
        #Obtêm o nome do usuário
        strUsuario = m_Var.getUser()
        # Verifica se nome do arquivo é válido
        if is_valid_filename(strFileName):
            # Verifica se é para incluir data no nome do arquivo
            if blnFileNameDate:
                # Atualiza variável com o nome enviado [3] , data [6] e extensão
                strFileName = strFileName[0:3] + dtFileDate + "." + strExtension
            else:
                # Atualiza variável com o nome enviado 
                strFileName = strFileName + "." + strExtension

            #print(strPath + strFileName)
        else:
            #print("invalido")
            pass

        # Verifica se é arquivo de LOG ou ERRO
        if strFileName[0:3] == "LOG"  or strFileName[0:3] == "ERR":
            # Acrescenta data e hora da gravação do log ou erro
            strText =  dtDate + "|" + tmTime + "|"  + m_Var.strComputer + "|" + m_Var.strIP + "|" + strUsuario + "|" + strText.upper()
        else:
            # Muda texto para maiúscula
            strText = strText.Upper()
            
        # Verifica se diretório existe
        if os.path.exists(strPath):
            # Verifica se existe algum texto para ser incluído
            if not strText == "":
                
                # Define qual o diretório a ser gravado o arquivo
                if strFileName[0:3] == "LOG":
                   # Atualiza a variável - Arquivos de LOG
                   strSubPath= "LOG\\"
                
                elif strFileName[0:3] == "ERR":
                    # Atualiza a variável - Arquivo de ERRO
                   strSubPath= "ERR\\"
                
                elif strFileName[0:3] == "RPT":
                        # Atualiza a variável - Arquivo de RELATÓRIO
                   strSubPath= "REPORT\\"
                
                else:
                     # Atualiza a variável - Outros arquivos 
                   strSubPath= "\\"
                    
                # Abre arquivo para escrita
                f = open(strPath + strSubPath + strFileName, 'a',  encoding = 'utf8')
                f.write(strText + "\n")
                f.close()
                                
            else:
                pass
        else:
            # Não encontrou o diretório
            pass


    except Exception as e:
       # Atualiza arquivo de erro com o erro ocorrido
       m_Err.printErr(traceback.format_exc())
