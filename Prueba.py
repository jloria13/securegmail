from Encrypt import Encryption

prueba = Encryption()
llaves = prueba.Newkey()
encriptado = prueba.Encrypt(llaves[1],b"Hola Mundo!")
print(encriptado)
desencriptar = prueba.Decrypt(llaves[0],encriptado)
print(desencriptar)
