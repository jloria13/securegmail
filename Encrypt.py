from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from base64 import b64encode,b64decode

class Encryption:

	#Specified long of the encrption key
	key_long = 2048

	"""
	 * Constructor for Encryption
	"""
	def __init__ (self):
		pass

	"""
	 * Generates both private and public keys, using the default key key_long
	 * Returns a list with the private and public keys
	"""
	def Newkey (self):
		#Generates a random object for encryption
		random = Random.new().read
		key = RSA.generate(self.key_long,random)
		private = key;
		public = key.publickey()
		print ("Type: ")
		print(type(public))
		return [private,public]

	"""
	 * Encrypt generates the padding using the standar PKCS1_OAEP for the public
	 * key and the encrypts the message to later convert it into base64 encode
	 * @public_key Public Key from the user
	 * @message Message to be encrypted
	 * Return the message encrypted in base64
	"""
	def Encrypt (self,public_key,message):
		#Generates padding using standard PKCS1_OAEP for the public key
		cypher = PKCS1_OAEP.new(public_key)
		#Encrypts the message with the cypher and converts it to base64
		encrypted = b64encode(cypher.encrypt(message))
		return encrypted

	"""
	 * Decrypt takes the private key, decodes the message from base64 and then
	 * decrypts it using the key
	 * @type {[type]}
	 * Return the message decrypted
	"""
	def Decrypt (self,private_key,message):
		#Generates padding using standard PKCS1_OAEP for the private key
		cypher = PKCS1_OAEP.new(private_key)
		#Converts the message from base64 and the decrypts it
		decrypted = cypher.decrypt(b64decode(message))
		return decrypted

	"""
	 * ViewKey exports the key so it can be visualized
	 * @key key from the user
	 * Returns the key vor visualization

	"""
	def ViewKey (self,key):
		return key.exportKey('PEM')
