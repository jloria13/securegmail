from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import logging

class Auth:

    """
    * Class Auth Constructor
    """
    def __init__(self):
        pass

    """
     * Auth_user authenticates the user in case it is a new user it will pop up
     * in the browser to login and give permission to the user in case its a not
     * new user it will load the already exising token
    """
    def Authenticate (self):
        #The following scope allows to all read/write operations
        SCOPES = 'https://mail.google.com/'
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        http = creds.authorize(Http())
        print("Http: ",http)
        self.GMAIL = build('gmail', 'v1', http=http)
        print("Build: ",self.GMAIL)
    """
     * getInbox retrieves all the messages in the inbox that have the inputed
     * labels on it
     * @labels {list} list of strings with the labels to look for
     * Returns a list with dictionaries containing the information from the mails
     * like subject,date,sender and body of the mail
    """
    def getInbox(self,labels):
        mails = []
        messages= self.GMAIL.users().messages().list(userId='me',labelIds=labels).execute()
        if messages['resultSizeEstimate'] != 0:
            messages = messages['messages']
            print("Mensajes totales: ",str(len(messages)))
            for message in messages:
                temp = {}
                message_id = message['id']
                message = self.GMAIL.users().messages().get(userId='me',id=message_id).execute()
                temp['ID'] = message_id
                payload = message['payload']  #This is where is contained the information of the message
                headers = payload['headers']   #Contained attributes like subject,sender and text

                #Retrieves main information of the message
                for header in headers:
                    if header['name'] == 'Subject':
                        subject = header['value']
                        temp['Subject'] = subject
                    else:
                        pass
                    if header['name'] == 'Date':
                        date = header['value']
                        temp['Date'] = str(date)
                    else:
                        pass
                    if header['name'] == 'From':
                        sender = header['value']
                        temp['Sender'] = sender
                    else:
                        pass

                #Snippet is the summary of the body of the mail
                temp['Snippet'] = message['snippet']

                #Fetch the body of the message
                if subject == '[PlainText]':
                    try:
                        message_parts = payload['parts']
                        first_part = message_parts[0]
                        body_part = first_part['body']
                        data_part = body_part['data']
                        first_filter = data_part.replace('-','+')
                        first_filter = first_filter.replace('_','/')
                        second_filter = base64.b64decode(first_filter)
                        message_body = second_filter.decode('UTF-8')
                        temp["Body"] = message_body.replace("\r\n","")
                    except:
                        print("An error ocurred retrieving the body the plain text message!")
                else:
                    try:
                        body_part = payload["body"]
                        body = body_part["data"]
                        first_filter = body.replace('-','+')
                        first_filter = first_filter.replace('_','/')
                        second_filter = base64.b64decode(first_filter)
                        body = second_filter.decode('UTF-8')
                        temp["Body"] = body
                    except:
                        print("An error ocurred retrieving the body the encrypted message!")

                print(temp)
                mails.append(temp)
                #Removes UNREAD label from the message NOT WORKING YET
                try:
                    self.GMAIL.users().modify(userId='me',id=message_id,body={'removeLabelIds':['UNREAD']}).execute()
                except:
                    pass

        else:
            print("There are no messages")

        return mails

    """
     * sendMessage sends the message created by the user
     * @message {object} Is a json object which contains the message to be sent
     * encoded in a base64 format
    """
    def sendMessage(self,body):
        try:
            message = self.GMAIL.users().messages().send(userId='me',body=body).execute()
            print("Message Sent")
        except errors.HttpError as error:
            print ("An error ocurred: ",error)
