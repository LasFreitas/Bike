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
        dirfilebackup = (m_Var.strDirSystem + '\\Backup\\').upper()
        
        # Define a data para deleção dos arquivos antigos, conforme quantidade de dias estipulado
        datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpDays))).strftime("%Y%m%d")[-6:]
      
               
        # Deletar arquivos anterior ao período estipulado
        def delete_file(self, lblabel, filetype):
            
            self.lblabel = lblabel
            self.filetype = filetype
            
             # Obtêm/ordena a lista de arquivos de backup selecionando arquivos pela extensão solicitada
            bkpfiles = list(filter(lambda x: x.endswith('.' + self.filetype), os.listdir(self.dirfilebackup)))
            bkpfiles.sort()
                        
            # Exibe mensagem ao usuário 
            self.lblabel.setText('AGUARDE ... VERIFICANDO ARQUIVOS ...' )
            self.lblabel.update()
            self.lblabel.repaint()
                                            
            # Executa loop para exclusão dos arquivos
            for delete_file in bkpfiles:
                
                # Verifica se o arquivo deve ser deletado
                if delete_file[2:-3] <= self.datInicial:
                    
                    # Deleta o arquivo
                    # FIXME Deletar arquivo a ser implementado após testes
                    os.remove(self.dirfilebackup + delete_file)
                    
                    # Atualiza label com a informação do arquivo deletado
                    self.lblabel.setText('DELETANDO ARQUIVO: ' + (self.dirfilebackup + delete_file).upper())
                    self.lblabel.update()
                    self.lblabel.repaint()
                    
                    # NOTE ---- Excluir, utilizado somente para depuração
                    # print('DELETANDO ARQUIVO: ' + (self.dirfilebackup + delete_file).upper())
                    
                    # Atualiza arquivo de log com o nome do arquivo deletado
                    m_Text.write_texto("LOG", "ARQUIVO DE BACKUP APAGADO|" + self.dirfilebackup + delete_file.upper() , "TXT", True)
                    
                    # Pausa método por um tempo
                    time.sleep(1)

                    
            # Exibe mensagem ao usuário 
            self.lblabel.setText('AGUARDE ... CARREGANDO O SISTEMA ...' )
            self.lblabel.update()
            self.lblabel.repaint()
                    
                   
        def BackupDelete():
            
            # TODO Criar nova rotina de BACKUP / DELETE de arquivos
            
            try:
                pass
            except Exception as e:
                # Atualiza arquivo de erro com o erro ocorrido
                m_Err.printErr(traceback.format_exc())



            
    except Exception as e:
        # Atualiza arquivo de erro com o erro ocorrido
        m_Err.printErr(traceback.format_exc())