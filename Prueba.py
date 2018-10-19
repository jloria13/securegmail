from Encrypt import Encryption

prueba = Encryption()
llaves = prueba.Newkey()
encriptado = prueba.Encrypt(llaves[1],"Hola Mundo!")
print("Encripcion: ")
print(encriptado)
desencriptar = prueba.Decrypt(llaves[0],encriptado)
print("Desencriptado: ")
print(desencriptar)
