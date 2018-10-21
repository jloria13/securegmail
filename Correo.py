from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class Correo:

	def __init__ (self,recipient,matter,body):
		self.recipient = recipient
		self.matter = matter
		self.body = body
