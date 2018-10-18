from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

class Encryption:

	key_long = 2048

	def __init__ (self):
		pass

	def Newkey ():
		random = Random.new().read
		key = RSA.generate(key_long,random)
		private = key;
		public = key.publickey()
		return [private,public]

	def Encrypt (public_key,message):
		cypher = PKCS1_OAEP.new(public_key)
		return cypher.encrypt(message)

	def Decrypt (private_key,message):
		cypher = PKCS1_OAEP.new(private_key)
		return cyper.decrypt(message)
