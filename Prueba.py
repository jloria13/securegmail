from Encrypt import *

prueba = Encrypt.new()
llaves = prueba.Newkeys()
print(prueba.Encrypt(llaves[1],"Hola Mundo!"))