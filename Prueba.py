from Encrypt import Encryption
from Auth import Auth
from Correo import Correo

correo = Correo('securemailpython@gmail.com','jloria1305@gmail.com','[PlainText]','Hola Mundo!')
message = correo.CreateMessage()
print(message)
auten = Auth()
auten.Auth_User()
auten.sendMessage(message)
"""

prueba = Encryption()
llaves = prueba.Newkey()
encriptado = prueba.Encrypt(llaves[1],bytes("Hola Mundo!",'UTF-8'))
print ("Llave publica: ")
print(prueba.ViewKey(llaves[1]))
print("\n*3")
print("Encripcion: ")
print(encriptado)
desencriptar = prueba.Decrypt(llaves[0],encriptado)
print("Desencriptado: ")
print(desencriptar.decode())
"""
