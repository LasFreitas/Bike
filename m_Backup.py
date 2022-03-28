import os
import datetime
import traceback
import time

import m_Err
import m_Var



def delDB(objObject):
    try:
        # Obtêm a lista de arquivos de backup
        bkpFiles = os.listdir(os.getcwd() + '\\Backup\\')
        # Define a data para deleção dos arquivos antigos
        datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpDays))).strftime("%Y%m%d")[-6:]
        # Executa loop para exclusão dos arquivos
        for i in bkpFiles:
            # Verifica se o arquivo deve ser deletado
            if i[2:-3] <= datInicial:
                # DEleta o arquivo
                # os.remove(os.getcwd()+ '\\Backup\\' + i)
                # MS('DELETANDO ARQUIVO: ' + i)
                # F000Splash.setMessage()
                objObject.setText('DELETANDO ARQUIVO: ' + i)
                objObject.update()
                objObject.repaint()
                time.sleep(1)
                # print('deletar ' + i)

    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())