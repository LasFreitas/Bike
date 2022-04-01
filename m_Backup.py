from msilib.schema import File
import os
import datetime
import traceback
import time

import m_Err
import m_Text
import m_Var



class Backup:
      
    try:
               
        # Deletar arquivos anterior ao período estipulado
        def delete_file(self, lblabel):
           
            # 
            self.lblabel = lblabel
                                    
            # Obtêm a lista de extensões dos arquivos a serem deletados
            lstFileExtension = m_Var.strBkpDelFiles.split('|')
            
            # Loop para deletar arquivos desnecessários
            for FileExtension in lstFileExtension:
                           
            
                # Verifica qual o tipo do arquivo e seleciona diretório correspondente
                if FileExtension.upper()=="DB":
                    # Arquivo: BANCO DE DADOS
                    dirfilebackup = (m_Var.strDirSystem + '\\Backup\\').upper()
                    
                    # Define a data para deleção dos arquivos antigos, conforme quantidade de dias estipulado
                    datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpDays))).strftime("%Y%m%d")[-6:]
                    
                elif FileExtension.upper()=='ERR':
                    # Aquivo: ERROS
                    dirfilebackup = (m_Var.strDirSystem + '\\Err\\').upper()
                    
                    # Define a data para deleção dos arquivos antigos, conforme quantidade de dias estipulado
                    datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpLogErr))).strftime("%Y%m%d")[-6:] 
                    
                elif FileExtension.upper() == 'LOG':
                    # Aquivo: LOG's
                    dirfilebackup = (m_Var.strDirSystem + '\\Log\\').upper()
                    
                    # Define a data para deleção dos arquivos antigos, conforme quantidade de dias estipulado
                    datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpLogErr))).strftime("%Y%m%d")[-6:] 
                
                        
                # Obtêm/ordena a lista de arquivos de backup selecionando arquivos pela extensão solicitada
                bkpfiles = list(filter(lambda x: x.endswith('.' + FileExtension), os.listdir(dirfilebackup)))
                bkpfiles.sort()
                            
                # Exibe mensagem ao usuário 
                self.lblabel.setText('AGUARDE ... VERIFICANDO ARQUIVOS ...' )
                self.lblabel.update()
                self.lblabel.repaint()
                                                
                # Executa loop para exclusão dos arquivos
                for delete_file in bkpfiles:
                    
                    # Obtêm o comprimento do início do arquivo
                    intLenFileName = len(FileExtension)
                    
                    # Verifica se o arquivo deve ser deletado
                    if delete_file[intLenFileName:-3] <= datInicial:
                        
                        # Deleta o arquivo
                        os.remove(dirfilebackup + delete_file)
                        
                        # Atualiza label com a informação do arquivo deletado
                        self.lblabel.setText('DELETANDO ARQUIVO: ' + (dirfilebackup + delete_file).upper())
                        self.lblabel.update()
                        self.lblabel.repaint()
                        
                        # Atualiza arquivo de log com o nome do arquivo deletado
                        m_Text.write_texto("LOG", "ARQUIVO " + FileExtension.upper()  + " APAGADO|" + dirfilebackup + delete_file.upper() ,"LOG", True)
                        
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