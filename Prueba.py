from Encrypt import Encryption

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
