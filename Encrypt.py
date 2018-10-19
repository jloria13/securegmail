from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from base64 import b64encode,b64decode

class Encryption:

	#Specified long of the encrption key
	key_long = 2048

	def __init__ (self):
		pass

	def Newkey (self):
		#Generates a random object for encryption
		random = Random.new().read
		key = RSA.generate(self.key_long,random)
		private = key;
		public = key.publickey()
		return [private,public]

	def Encrypt (self,public_key,message):
		#Generates padding using standard PKCS1_OAEP for the public key
		cypher = PKCS1_OAEP.new(public_key)
		#Encrypts the message with the cypher and converts it to base64
		encrypted = b64encode(cypher.encrypt(message))
		return encrypted

	def Decrypt (self,private_key,message):
		#Generates padding using standard PKCS1_OAEP for the private key
		cypher = PKCS1_OAEP.new(private_key)
		#Converts the message from base64 and the decrypts it
		decrypted = cypher.decrypt(b64decode(message))
		return decrypted
