# !/usr/bin/python
# -*- coding: UTF-8 -*-


# imports
import os
import traceback
import yaml

#imports locais
import m_Err
import m_Var

def Read_Config():
    try:
        # Verifica se existe o arquivo de configuração
        if os.path.exists(m_Var.strDirSystem + '\\DATABASE\\Config.yml'):
            pass
            
    except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())  