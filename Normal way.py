
from cryptography.fernet import Fernet



def generate_key():
    key = Fernet.generate_key()
    with open("Secret.key","wb") as key_file :
        key_file.write(key)


def load_key():
    return open("Secret.key","rb").read()

def encrpt(filename,key):
    f = Fernet(key)
    with open(filename ,"rb") as file :
        filedata = file.read()
        en_data = f.encrypt(filedata)
    with open(filename , "wb") as file :
        file.write(en_data)

def decrypt(filename ,key) :
    f = Fernet(key)
    with open(filename ,"rb") as file: 
        en_data = file.read()
        try :
            decrypt_data = f.decrypt(en_data)
        except :
            print("Invalid key")
            return
    with open(filename ,"wb") as file :
        file.write{decrypt_data}
    
ch = input(" Enter  E to Encrypt  or D to Decrypt : ").lower
if ch == 'e':
    filename = input
