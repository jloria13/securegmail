from Auth import Auth
from Correo import Correo
from Encrypt import Encryption
from pathlib import Path
import json

AUTH = Auth()
PUBLICKEY = None
PRIVATEKEY = None

def SelectUser (option):
    global AUTH
    # TODO: Select which user to be used if an already existing one or a new
    # one, if a new user is select or RESET the token file shall be deleted
    file = 'token.json'
    if not file.is_file():
        AUTH.Authenticate()
    elif option == 1:
        file.unlink()
        AUTH.Authenticate()
    else:
        print("Bienvenido")

def ShareKey():
    # TODO: Generate and share a public key with an inputed mail also the mail
    # has to be validated as an exising one
    pass

def SafeKey():
    # TODO: If a user sends a public key the system has to ask to save it,
    # if two keys are sent the latest one is going to be the saved one
    pass

def ComposeMessage():
    # TODO: The user can compose a mail and if the sender email has a public key
    # its going to ask the user if he wants to encrypt the message
    pass

def Inbox():
    # TODO: Is going to retrieve al the current mail in the mail box
    pass

def FriendsKeys():
    # TODO: visualize all the friends and their respective keys
    pass

def SaveUser(email):
    # TODO: Saves a new user in a json file
    new_user = {'email':email}
    try:
        #Opening json file for lecture
        with open('users.json') as json_file:
            data = json.load(json_file)
            data = data['users']
        json_file.close()
        #Appending new user email
        data.append(new_user)
        #Opening json file for writing
        with open('users.json','w') as json_file:
            json.dump(data,json_file)
    except:
        data = {}
        data['users'] = [new_user]
        with open('users.json','w') as json_file:
            json.dump(data,json_file)
