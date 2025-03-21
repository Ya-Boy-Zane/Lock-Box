import Coder as coder
import os
import json

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
    enc_pass = coder.encrypt(pas)
    store(name_of_site,user,enc_pass)

#Find Password
def find_pass(name_of_site):
    try:
        with open(data,'r') as of:
            passes = json.load(of)
            spec_data = passes.get(name_of_site)
        if spec_data == None:
            user,pas = None,None
            print("ERROR:PASSWORD DOES NOT EXSIST")
            return user,pas
        else:
            for i in spec_data.keys():
                user = i
            for i in spec_data.values():
                pas = i
            pas = coder.decrypt(pas)
            return user,pas
    except FileNotFoundError:
        print("ERROR : FILE NOT FOUND")
    except Exception as e:
        print(f"UNKNOWN ERROR: {e}")

add_pass("Roblox","Miyon12b","Sanban123")

user,pas = find_pass("gayblox")
print(user)
print(pas)


