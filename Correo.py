from email.mime.text import MIMEText
from apiclient import errors as errors
import mimetypes
import base64


class Correo:

	def __init__ (self,sender,recipient,subject,body):
		self.recipient = recipient
		self.subject = subject
		self.body = body
		self.sender = sender

	def CreateMessage (self):
		message = MIMEText(self.body,'plain')
		message['to'] = self.recipient
		message['from'] = self.sender
		message['subject'] = self.subject
		return {'raw': base64.urlsafe_b64encode(bytes(message.as_string(),'UTF-8'))}
