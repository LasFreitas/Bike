# imports
import os
import traceback

# imports locais
import m_Text
import m_Err
import m_Var

#import M_Message


def Load_Image(strImage):
   try:
       
       # Verifica se foi passado a extensão do arquivo
       if os.path.splitext(strImage)[1] == "":
            strImage = strImage + ".png"
            
       
       if os.path.exists(m_Var.strDirSystem + '\\Icons\\' + strImage):
           return m_Var.strDirSystem + '\\Icons\\' + strImage
       else:
           if os.path.exists(m_Var.strDirSystem + '\\Icons\\noimg.png'):
               return m_Var.strDirSystem + '\\Icons\\noimg.png'
                
   except Exception as e:
       # Atualiza arquivo de erro com o erro ocorrido
       m_Err.printErr(traceback.format_exc())
   