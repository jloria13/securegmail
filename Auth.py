from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import base64
import logging

CLIENTSECRETS_LOCATION = 'credentials.json'
REDIRECT_URI = '<YOUR_REGISTERED_REDIRECT_URI>'
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/gmail.modify'
]

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
    def Auth_User (self):
        #The following scope allows to all read/write operations
        SCOPES = 'https://mail.google.com/'
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.GMAIL = build('gmail', 'v1', http=creds.authorize(Http()))

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
                payload = message['payload']
                headers = payload['headers']

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
                try:
                    message_parts = payload['parts']
                    first_part = message_parts[0]
                    body_part = first_part['body']
                    data_part = body_part['data']
                    print("Data part: ",data_part)
                    first_filter = data_part.replace('-','+')
                    first_filter = first_filter.replace('_','/')
                    second_filter = base64.b64decode(first_filter)
                    message_body = second_filter.decode('UTF-8')
                    temp["Body"] = message_body.replace("\r\n","")
                except:
                    print("An error ocurred retrieving the body the message!")

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
    def sendMessage(self,message):
        try:
            message = self.GMAIL.users().message().send(userId='me',body=message).execute()
            print("Message Sent")
        except errors.HttpError as error:
            print ("An error ocurred: ",error)


# PONCHO
#
# class GetCredentialsException(Exception):
#   """Error raised when an error occurred while retrieving credentials.
#
#   Attributes:
#     authorization_url: Authorization URL to redirect the user to in order to
#                        request offline access.
#   """
#
#   def __init__(self, authorization_url):
#     """Construct a GetCredentialsException."""
#     self.authorization_url = authorization_url
#
#
# class CodeExchangeException(GetCredentialsException):
#   """Error raised when a code exchange has failed."""
#
#
# class NoRefreshTokenException(GetCredentialsException):
#   """Error raised when no refresh token has been found."""
#
#
# class NoUserIdException(Exception):
#   """Error raised when no user ID could be retrieved."""
#
#
# def get_stored_credentials(user_id):
#   """Retrieved stored credentials for the provided user ID.
#
#   Args:
#     user_id: User's ID.
#   Returns:
#     Stored oauth2client.client.OAuth2Credentials if found, None otherwise.
#   Raises:
#     NotImplemented: This function has not been implemented.
#   """
#   # TODO: Implement this function to work with your database.
#   #       To instantiate an OAuth2Credentials instance from a Json
#   #       representation, use the oauth2client.client.Credentials.new_from_json
#   #       class method.
#   raise NotImplementedError()
#
#
# def store_credentials(user_id, credentials):
#   """Store OAuth 2.0 credentials in the application's database.
#
#   This function stores the provided OAuth 2.0 credentials using the user ID as
#   key.
#
#   Args:
#     user_id: User's ID.
#     credentials: OAuth 2.0 credentials to store.
#   Raises:
#     NotImplemented: This function has not been implemented.
#   """
#   # TODO: Implement this function to work with your database.
#   #       To retrieve a Json representation of the credentials instance, call the
#   #       credentials.to_json() method.
#   raise NotImplementedError()
#
#
# def exchange_code(authorization_code):
#   """Exchange an authorization code for OAuth 2.0 credentials.
#
#   Args:
#     authorization_code: Authorization code to exchange for OAuth 2.0
#                         credentials.
#   Returns:
#     oauth2client.client.OAuth2Credentials instance.
#   Raises:
#     CodeExchangeException: an error occurred.
#   """
#   flow = flow_from_clientsecrets(CLIENTSECRETS_LOCATION, ' '.join(SCOPES))
#   flow.redirect_uri = REDIRECT_URI
#   try:
#     credentials = flow.step2_exchange(authorization_code)
#     return credentials
#   except FlowExchangeError, error:
#     logging.error('An error occurred: %s', error)
#     raise CodeExchangeException(None)
#
#
# def get_user_info(credentials):
#   """Send a request to the UserInfo API to retrieve the user's information.
#
#   Args:
#     credentials: oauth2client.client.OAuth2Credentials instance to authorize the
#                  request.
#   Returns:
#     User information as a dict.
#   """
#   user_info_service = build(
#       serviceName='oauth2', version='v2',
#       http=credentials.authorize(httplib2.Http()))
#   user_info = None
#   try:
#     user_info = user_info_service.userinfo().get().execute()
#   except errors.HttpError, e:
#     logging.error('An error occurred: %s', e)
#   if user_info and user_info.get('id'):
#     return user_info
#   else:
#     raise NoUserIdException()
#
#
# def get_authorization_url(email_address, state):
#   """Retrieve the authorization URL.
#
#   Args:
#     email_address: User's e-mail address.
#     state: State for the authorization URL.
#   Returns:
#     Authorization URL to redirect the user to.
#   """
#   flow = flow_from_clientsecrets(CLIENTSECRETS_LOCATION, ' '.join(SCOPES))
#   flow.params['access_type'] = 'offline'
#   flow.params['approval_prompt'] = 'force'
#   flow.params['user_id'] = email_address
#   flow.params['state'] = state
#   return flow.step1_get_authorize_url(REDIRECT_URI)
#
#
# def get_credentials(authorization_code, state):
#   """Retrieve credentials using the provided authorization code.
#
#   This function exchanges the authorization code for an access token and queries
#   the UserInfo API to retrieve the user's e-mail address.
#   If a refresh token has been retrieved along with an access token, it is stored
#   in the application database using the user's e-mail address as key.
#   If no refresh token has been retrieved, the function checks in the application
#   database for one and returns it if found or raises a NoRefreshTokenException
#   with the authorization URL to redirect the user to.
#
#   Args:
#     authorization_code: Authorization code to use to retrieve an access token.
#     state: State to set to the authorization URL in case of error.
#   Returns:
#     oauth2client.client.OAuth2Credentials instance containing an access and
#     refresh token.
#   Raises:
#     CodeExchangeError: Could not exchange the authorization code.
#     NoRefreshTokenException: No refresh token could be retrieved from the
#                              available sources.
#   """
#   email_address = ''
#   try:
#     credentials = exchange_code(authorization_code)
#     user_info = get_user_info(credentials)
#     email_address = user_info.get('email')
#     user_id = user_info.get('id')
#     if credentials.refresh_token is not None:
#       store_credentials(user_id, credentials)
#       return credentials
#     else:
#       credentials = get_stored_credentials(user_id)
#       if credentials and credentials.refresh_token is not None:
#         return credentials
#   except CodeExchangeException, error:
#     logging.error('An error occurred during code exchange.')
#     # Drive apps should try to retrieve the user and credentials for the current
#     # session.
#     # If none is available, redirect the user to the authorization URL.
#     error.authorization_url = get_authorization_url(email_address, state)
#     raise error
#   except NoUserIdException:
#     logging.error('No user ID could be retrieved.')
#   # No refresh token has been retrieved.
#   authorization_url = get_authorization_url(email_address, state)
#   raise NoRefreshTokenException(authorization_url)
