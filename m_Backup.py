import os
import datetime
import traceback
import time

import m_Err
import m_Text
import m_Var



class Backup:
      
    try:
              
        # Definição do diretório de BACKUP´s
        dirfilebackup = (os.getcwd() + '\\Backup\\').upper()
        
        # Define a data para deleção dos arquivos antigos, conforme quantidade de dias estipulado
        datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpDays))).strftime("%Y%m%d")[-6:]
      
               
        # Deletar arquivos anterior ao período estipulado
        def delete_file(self, lblabel, filetype):
            
            self.lblabel = lblabel
            self.filetype = filetype
            
             # Obtêm a lista de arquivos de backup
            bkpfiles = list(filter(lambda x: x.endswith('.' + self.filetype), os.listdir(self.dirfilebackup)))
            
            bkpfiles.sort()
            
            #bkpFiles = os.listdir(self.dirfilebackup + '*.' + self.filetype).upper()
            
            
            
            # Exibe mensagem ao usuário 
            self.lblabel.setText('AGUARDE ... VERIFICANDO ARQUIVOS ...' )
            self.lblabel.update()
            self.lblabel.repaint()
            
           
                                
            # Executa loop para exclusão dos arquivos
            for delete_file in bkpfiles:
                
                # Verifica se o arquivo deve ser deletado
                if delete_file[2:-3] <= self.datInicial:
                    
                    # Deleta o arquivo
                    # TODO Deletar arquivo a ser implementado após testes
                    # os.remove(self.dirfilebackup + delete_file).upper())
                    
                    # Atualiza label com a informação do arquivo deletado
                    self.lblabel.setText('DELETANDO ARQUIVO: ' + (self.dirfilebackup + delete_file).upper())
                    self.lblabel.update()
                    self.lblabel.repaint()
                    
                    print('DELETANDO ARQUIVO: ' + (self.dirfilebackup + delete_file).upper())
                    
                    # Atualiza arquivo de log com o nome do arquivo deletado
                    m_Text.write_texto("LOG", "ARQUIVO DE BACKUP APAGADO|" + os.getcwd()+ '\\Backup\\' + delete_file.upper() , "TXT", True)
                    
                    # Pausa método por um tempo
                    time.sleep(1)
                    
            def backup_db(self):
                # TODO Rotina de backup a ser implementada
                pass
            
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())