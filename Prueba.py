from Encrypt import Encryption
from Auth import Auth

auten = Auth()
auten.Auth_User()
auten.getInbox(['INBOX'])


"""
prueba = Encryption()
llaves = prueba.Newkey()
encriptado = prueba.Encrypt(llaves[1],"Hola Mundo!")
print ("Llave publica: ")
print(prueba.ViewKey(llaves[1]))
print("\n*3")
print("Encripcion: ")
print(encriptado)
desencriptar = prueba.Decrypt(llaves[0],encriptado)
print("Desencriptado: ")
print(desencriptar)
"""
