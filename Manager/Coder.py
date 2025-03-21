from cryptography.fernet import Fernet as fer
import os

#Key Generator
storage = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__,".."))),"Storage")
file = os.path.join(storage,"key.key")
try:
        if os.path.exists(file):
            with open(file,'rb') as f:
                key = f.read()

            cypher = fer(key)
        else:
            key_file = f"{storage}/key.key"
            with open(key_file,'wb') as f1:
                key = fer.generate_key()
                f1.write(key)
                cypher = fer(key)
except Exception as e:
     print(f"UNKNOW ERROR: {e}")

#Encryptor
def encrypt(pas):
    pas = pas.encode()
    enc_pass = cypher.encrypt(pas)
    enc_pass = enc_pass.decode()
    return enc_pass

#Decryptor
def decrypt(pas):
    pas = pas.encode()
    try:
        decr_pass = cypher.decrypt(pas)
    except Exception as e:
         print("KEY ERROR:CURRENT KEY DOES NOT MATCH ENCRYPTION KEY OF CURRENT ENCRYPTED DATA")
    decr_pass = decr_pass.decode()
    return decr_pass