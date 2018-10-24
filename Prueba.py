from Encrypt import Encryption
from Auth import Auth
from Correo import Correo

"""
correo = Correo('securemailpython@gmail.com','jloria1305@gmail.com','[PlainText]','Hola Mundo!',False)
message = correo.CreateMessage()
print(message)
auten = Auth()
auten.Auth_User()
auten.getInbox('INBOX')
#auten.sendMessage(message)
"""

#prueba = Encryption()
#llaves = prueba.Newkey()
#encriptado = prueba.Encrypt(llaves[1],bytes("Hola Mundo!",'UTF-8'))
#correo = Correo('securemailpython@gmail.com','securemailpython@gmail.com','[Encrypted]',str(encriptado.decode("UTF-8")),True)
#message = correo.CreateMessage()
#print(message)
#print("-----------------")
auten = Auth()
auten.Authenticate()
# auten.sendMessage(message)
correos = auten.getInbox('INBOX')
# encriptado = correos[0]["Body"]
# print(encriptado)
# print("--------------")
# des = prueba.Decrypt(llaves[0],encriptado)
# print("Desencriptado: ")
# print(des.decode())
#print ("Llave publica: ")
#print(prueba.ViewKey(llaves[1]))
#print("Tipo: ",type(prueba.ViewKey(llaves[1])))
#print("Encripcion: ")
#print(encriptado)
#desencriptar = prueba.Decrypt(llaves[0],encriptado)
#print("Desencriptado: ")
#print(desencriptar.decode())
