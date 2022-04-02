from msilib.schema import File
import os
import datetime
import traceback
import time
import shutil


import m_Err
import m_Text
import m_Var


class Backup:
               
    # Deletar arquivos anterior ao período estipulado
    def delete_file(self, lblabel):
    
        try:   
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
                    
                    intLenBkpFiles = int(m_Var.intBkpDays)
                                    
                    
                elif FileExtension.upper()=='ERR':
                    # Aquivo: ERROS
                    dirfilebackup = (m_Var.strDirSystem + '\\Err\\').upper()
                    
                    intLenBkpFiles = int(m_Var.intBkpLogErr)
                                      
                    
                elif FileExtension.upper() == 'LOG':
                    
                    # Aquivo: LOG's
                    dirfilebackup = (m_Var.strDirSystem + '\\Log\\').upper()
                    
                    intLenBkpFiles = int(m_Var.intBkpLogErr)
                                                            
                # Obtêm/ordena a lista de arquivos de backup selecionando arquivos pela extensão solicitada
                bkpfiles = list(filter(lambda x: x.endswith('.' + FileExtension), os.listdir(dirfilebackup)))
                bkpfiles.sort()
                            
                # Exibe mensagem ao usuário 
                self.lblabel.setText('AGUARDE ... VERIFICANDO ARQUIVOS ...' )
                self.lblabel.update()
                self.lblabel.repaint()
                   
                   
                # Verifica se o número de arquivos de backup é maior que o número de dias especificados de backup
                if len(bkpfiles) > intLenBkpFiles:
                    
                    # Calcula quantos itens serão deletados
                    intDeleteFileNumber = (len(bkpfiles) - intLenBkpFiles)
                    
                    # Se for MAIOR que o número especificado de dias, DELETA o arquivo
                    for intDeleteFile in range(intDeleteFileNumber):
                                               
                        # Deleta o arquivo
                        os.remove(dirfilebackup + bkpfiles[intDeleteFile])
                        
                        # Atualiza label com a informação do arquivo deletado
                        self.lblabel.setText('DELETANDO ARQUIVO: ' + (dirfilebackup + bkpfiles[intDeleteFile]).upper())
                        self.lblabel.update()
                        self.lblabel.repaint()
                        
                        # Atualiza arquivo de log com o nome do arquivo deletado
                        m_Text.write_texto("LOG", "ARQUIVO " + FileExtension.upper()  + " APAGADO|" + dirfilebackup + bkpfiles[intDeleteFile].upper() ,"LOG", True)
                        
                        # Pausa método por um tempo
                        time.sleep(1)
                        
            # Exibe mensagem ao usuário 
            self.lblabel.setText('AGUARDE ... CARREGANDO O SISTEMA ...' )
            self.lblabel.update()
            self.lblabel.repaint()

        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())                
                    
   
    # Realiza backup do banco de dados 
    def backup_file(self, lblabel):
        
        try:
             
            self.lblabel = lblabel
        
            ''' DATAS '''
        
            # Define a data INICIAL dos arquivos (DATABASE)
            datInicial = (datetime.datetime.now() - datetime.timedelta(days=int(m_Var.intBkpDays))).strftime("%Y%m%d")[-6:]
                   
            ''' DIRETÓRIOS '''
                         
            # ORIGEM 
            dirFileDatabase = (m_Var.strDirSystem + '\\Database\\').upper()
            # DESTINO
            dirfileBackup = (m_Var.strDirSystem + '\\Backup\\').upper()
            
            ''' ARQUIVO   '''
       
            # Nome do arquivo do banco de dados
            strDatabaseFileName = m_Var.strDatabaseFileName.upper()
            
            # Excuta loop para manter sempre a quantidade mínima de backup's do banco de dados
            for intDays in range(int(m_Var.intBkpDays)-1,-1,-1):
                
                # Define a data para copiar o arquivo de backup
                datInicial = (datetime.datetime.now() - datetime.timedelta(days = intDays)).strftime("%Y%m%d")[-6:]
            
                # Define o nome do arquivo
                strFileNameBackup = (m_Var.strDatabaseFile + datInicial + "." + m_Var.strDatabaseExension).upper()
            
                # Verifica se já foi realizado o backup do dia
                if os.path.exists(dirfileBackup + strFileNameBackup) == False:
                   
                    # Realiza cópia de backup
                    shutil.copy(dirFileDatabase + strDatabaseFileName, dirfileBackup + strFileNameBackup)
                    
                     # Atualiza label com a informação do arquivo copiadu
                    self.lblabel.setText('COPIANDO ARQUIVO: ' + (dirfileBackup + strFileNameBackup))
                    self.lblabel.update()
                    self.lblabel.repaint()
                    
                    # Atualiza arquivo de log com o nome do arquivo deletado
                    m_Text.write_texto("LOG", "BACKUP DO BANCO DE DADOS REALIZADO|" + (dirfileBackup + strFileNameBackup).upper() ,"LOG", True)
            
                    # Pausa método por um tempo
                    time.sleep(1)
                    
            # Exibe mensagem ao usuário 
            self.lblabel.setText('AGUARDE ... CARREGANDO O SISTEMA ...' )
            self.lblabel.update()
            self.lblabel.repaint()    

        except Exception as e:
            # Atualiza arquivo de erro com o erro ocorrido
            m_Err.printErr(traceback.format_exc())



   