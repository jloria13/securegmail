from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiclient import errors as errors
import mimetypes
import base64


class Correo:

	def __init__ (self,sender,to,subject,body):
		self.to = to
		self.subject = subject
		self.body = body
		self.sender = sender

	def CreateMessage (self):
		message = MIMEMultipart('alternative')
		message['to'] = self.to
		message['from'] = self.sender
		message['subject'] = self.subject
		message.attach(MIMEText(self.body,'plain'))
		message.attach(MIMEText(self.body,'html'))
		raw_message = base64.urlsafe_b64encode(message.as_bytes())
		raw_message = raw_message.decode()
		print("Message: ",raw_message)
		return {'raw': raw_message}
