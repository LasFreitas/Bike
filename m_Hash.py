# imports
import hashlib
import traceback
from enum import Enum

# imports locais
import m_Err

# Criação de variável para utilização deste script
strTmp = ""


class EnumCrypt(Enum):
   # Método de criação de CRYPT (SOMENTE UNIX - NÃO FUNCIONA NO WWINDOWS)
   m_MD5 = 0
   m_BLOWFISH = 1
   m_CRYPT = 2
   m_SHA256 = 3
   m_SHA512 = 4
   
class EnumHash(Enum):
   # Método de criação de HASH
   m_BYTE = 0
   m_MD5 = 1


""" FUNÇÃO PARA CRIAR HASH """

# FIXME PENDÊNCIA: RETIRAR b'.....' DA STRING BYTES (LINHA 23)

def CreateHash(strHash, enmHash = EnumHash.m_MD5):
   # strHash - string a ser codificada
   # blnByte - método de codificação byte a byte (True) ou hexadecimal (False)
   try:
       # Verifica qual o método a ser utilizado
       if enmHash.value == 0:
           # Codifica usando byte a byte
           strTmp = hashlib.md5(b'strHash')
           strTmp = strTmp.digest()
       elif enmHash.value == 1:
           # Codifica em MD5
           strTmp = hashlib.md5(strHash.encode())
           strTmp = strTmp.hexdigest()
       # retorna hash
       return strTmp

   except Exception as e:
      # Atualiza arquivo de erro com o erro ocorrido
      m_Err.printErr(traceback.format_exc())

