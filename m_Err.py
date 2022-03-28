# imports
import os
import sys
import traceback

# imports locais
import m_Text



def printErr(strErro, blnShowForm = False):
    try:
        # Verifica se foi passado algum texto
        if  strErro!="":
              
            # Define variável temporária e divite o texto          
            strerr = strErro.split('\n')
            
            # Limpavariável 
            strErro =""
            
            # Itera os itens para formatação do texto
            for id, item in enumerate(strerr):
                 
                 # Verifica se foi passado algum texto
                 if item.strip()!="":
                     
                    # Verifica se é o primeiro item
                   if id == 0:
                        # Formata o texto sem TAB
                       strErro += "\n\t" + item.strip() + "\n"
                   else:                
                        # Formata o texto com TAB
                        strErro += "\t" + item.strip() + "\n"
                      
            # Escreve erro no arquivo de erro
            m_Text.write_texto("ERR", strErro)
            
    except Exception as e:
       # Atualiza arquivo de erro com o erro ocorrido
       printErr(traceback.format_exc())