from Auth import Auth
from Correo import Correo
from Encrypt import Encryption
from pathlib import Path
import json

#Global Variables
AUTH = Auth()
PUBLICKEY = None
PRIVATEKEY = None
Correo_Persona =""

def menuInicial():
	global Correo_Persona
	print("Digite el numero de la opcion que desea")
	print("1. Inicir sesion", "\t", "\t","2.Salir","\n")
	Eleccion = input()
	print("\n")
	if(Eleccion=="1"):
		print("Ingrese el Correo")
	elif(Eleccion=="2"):
		exit()
	else:
		print ("Digite un valor valido")
		menuInicial()


def menu():
	print("1.ShareKey", "\t", "\t","2. SafeKey")
	print("3.Inbox", "\t", "\t","4. Reset")
	print("5.Reset", "\t", "\t","6. New user")
	print("7 Salir")
	Seleccion = input("\n"+"Eleccion: ")
	print ("\n")
	if(Seleccion=="1"):
		Correo_Persona= input("Ingrese el correo electronico"+"\n")
		prueba()
		ShareKey(Correo_Persona)
	elif(Seleccion=="2"):
		Correo_Persona= input("Ingrese el correo electronico"+"\n")
		## PubKey=input("Ingrese la Llave publica"+"\n")
		## PriKey=input("Ingrese la llave privada"+"\n")
		SafeKey(correo)
	elif(Seleccion=="3"):
		Correo_Persona= input("Ingrese el correo electronico"+"\n")
		Inbox()



def prueba():
	print("Aca correo")
	print(Correo_Persona)

def SelectUser (reset,email=None):
    global AUTH
    # TODO: Select which user to be used if an already existing one or a new
    # one, if a new user is select or RESET the token file shall be deleted
    
    file = 'token.json'
    if not file.is_file():
        AUTH.Authenticate()
    elif reset:
        file.unlink()
        AUTH.Authenticate()
        SaveUser(email)
    else:
        if not CheckUser(email):
            AUTH.Authenticate()
    print(Bienvenido)


def ShareKey(email):
    # TODO: Generate and share a public key with an inputed mail also the mail
    # has to be validated as an exising one
    pass

def SafeKey(email,public=None,private=None):
    # TODO: If a user sends a public key the system has to ask to save it,
    # if two keys are sent the latest one is going to be the saved one

    try:
        #Parsing trying to find the email
        friends = LoadKeys()
        for friend in friends:
            if friend['email'] == email:
                if friend['public'] is None:
                    friend['public'] = public
                if friend['private'] is None:
                    friend['private'] = private
            else:
                new_friend = [{'email':email,'public':public,'private':private}]

        #Appending new user email
        data.append(new_user)
        #Opening json file for writing
        with open('users.json','w') as json_file:
            json.dump(data,json_file)
    except:
        data = {}
        data['friends'] = [{'email':email,'public':public,'private':private}]
        with open('users.json','w') as json_file:
            json.dump(data,json_file)

def LoadKeys ():
    #Opening json file for lecture
    with open('friends.json') as json_file:
        data = json.load(json_file)
        data = data['friends']
    json_file.close()
    return data


def ComposeMessage():
    # TODO: The user can compose a mail and if the sender email has a public key
    # its going to ask the user if he wants to encrypt the message
    pass

def Inbox():
    # TODO: Is going to retrieve al the current mail in the mail box
    mails = AUTH.getInbox()

def FriendsKeys():
    # TODO: visualize all the friends and their respective keys
    pass

def CheckUser(email):
    # TODO: Checks if the user already exists in the is_file
    try:
        #Opening json file for lecture
        with open('users.json') as json_file:
            data = json.load(json_file)
            users = data['users']
        json_file.close()

        #Parsing emails
        for user in data:
            if user['email'] == email:
                return True
        return False
    except:
        return False

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

menuInicial()