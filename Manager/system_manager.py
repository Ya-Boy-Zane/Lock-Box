from data_manager import encrypt as encrypt
from data_manager import decrypt as decrypt
import os
import json
from colorama import Fore
import time

#Path to storage
storage = os.path.join(os.path.dirname(os.path.abspath(os.path.join(__file__,".."))),"Storage")
data = os.path.join(storage,"data.json")

#Storage
def store(site,user,pas):
    try:
        inp = {str(site):{str(user):str(pas)}}
        with open(data,'r') as d:
            passes = json.load(d)
            passes.update(inp)
        with open(data,'w') as op:
            json.dump(passes,op)
    except FileNotFoundError:
        print("DATA FILE WAS NOT FOUND")
    except Exception as e:
        print(f"UNKNOWN ERROR : {e}")

#Add Password
def add_pass(name_of_site,user,pas):
    enc_pass = encrypt(pas)
    store(name_of_site,user,enc_pass)

#Find Password
def find_pass(name_of_site):
    try:
        with open(data,'r') as of:
            passes = json.load(of)
            spec_data = passes.get(name_of_site)
        if spec_data == None:
            user,pas = None,None
            print(Fore.YELLOW+"Error:Site not found")
            return user,pas
        else:
            for i in spec_data.keys():
                user = i
            for i in spec_data.values():
                pas = i
            pas = decrypt(pas)
            return user,pas
    except FileNotFoundError:
        print(Fore.YELLOW+"Error:File not found")
    except Exception as e:
        print(Fore.YELLOW+f"Unknown Error: {e}")

us,pas  = find_pass("Netflix")
print(us,pas)
